import requests
import time
import json

API_KEY = "api ahh"
REGION = "americas"  # use 'americas' for NA/LATAM, 'asia' for KR/JP, 'europe' for EU
PLAYER_NAME = "Kungpowji"
TAG_LINE = "chikn"

#  Get PUUID
account_url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{PLAYER_NAME}/{TAG_LINE}?api_key={API_KEY}"
account_data = requests.get(account_url).json()
puuid = account_data["puuid"]

# Get match IDs (100 at a time, up to full year)
match_url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key={API_KEY}"
match_ids = requests.get(match_url).json()

# Loop over match IDs and get details
matches = []
for match_id in match_ids:
    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}"
    data = requests.get(url).json()
    matches.append(data)
    time.sleep(1.2)  # avoid hitting rate limits

# Step 4: Save locally
with open("matches.json", "w") as f:
    json.dump(matches, f, indent=2)
