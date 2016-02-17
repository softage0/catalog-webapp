import json

DB_URL = "postgres://oiuhydyuipflby:wA2Dn17rl-Y_ckX6krEHMcHITG@ec2-54-83-29-133.compute-1.amazonaws.com:5432/d8quo2rmar6mro"  # noqa
# DB_URL = "sqlite:///catalog/catalog.db"

GOOGLE_CLIENT_ID = json.loads(open('catalog/config/client_secrets.json', 'r').read())['web']['client_id']

FB_APP_ID = "1530577940605500"
FB_APP_SECRET = "e64b02652902fa21d885808387255113"
