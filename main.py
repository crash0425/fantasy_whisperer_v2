import os
import time
from datetime import datetime
import sys

print("\n✅ Fantasy Whisperer is live on Render 🎉", flush=True)

# Read environment variables
email = os.getenv("EMAIL")
team_id = os.getenv("TEAM_ID")
league_id = os.getenv("LEAGUE_ID")
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

# Display loaded environment variables
print(f"📧 Email: {email}", flush=True)
print(f"🏈 Team ID: {team_id}", flush=True)
print(f"🏆 League ID: {league_id}", flush=True)
print(f"🍪 ESPN_S2: {'✅ Loaded' if espn_s2 else '❌ MISSING'}", flush=True)
print(f"🍪 SWID: {'✅ Loaded' if swid else '❌ MISSING'}", flush=True)

# Heartbeat loop
while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"💓 [{now}] Fantasy Whisperer is running...", flush=True)
    time.sleep(5)
