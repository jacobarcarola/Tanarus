import openmeteo_requests
import requests_cache
import pandas as pd
import json
from retry_requests import retry
import setup

print("Starting Tanarus... Please wait...")
# Check for new user with settings JSON file and launch setup script if new:
with open('settings.json', 'r') as file:
    settings = json.load(file)

if(settings['new_user'] == True):
    print("running setup script...")
    setup.setup()

# As per open-meteo documentation,
# setup API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor= 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

