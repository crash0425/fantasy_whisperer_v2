import os
import time
from datetime import datetime

print("\n✅ Fantasy Whisperer is live on Render 🎉")

# Read environment variables
email = os.getenv("EMAIL")
team_id = os.getenv("TEAM_ID")
league_id = os.getenv("LEAGUE_ID")
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

# Display loaded environment variables
print(f"📧 Email: {email}")
print(f"🏈 Team ID: {team_id}")
print(f"🏆 League ID: {league_id}")
print(f"🍪 ESPN_S2: {'✅ Loaded' if espn_s2 else '❌ MISSING'}")
print(f"🍪 SWID: {'✅ Loaded' if swid else '❌ MISSING'}")

# Heartbeat loop
while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"💓 [{now}] Fantasy Whisperer is running... checking fantasy football data.")
    time.sleep(30)  # check every 30 seconds for now
