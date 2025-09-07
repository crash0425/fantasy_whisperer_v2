import os
from datetime import datetime
import time

print("🔥🔥🔥 STARTING Fantasy Whisperer TEST 🔥🔥🔥")

# Read env variables
email = os.getenv("EMAIL", "Not Set")
team_id = os.getenv("TEAM_ID", "Not Set")
league_id = os.getenv("LEAGUE_ID", "Not Set")
espn_s2 = os.getenv("ESPN_S2", "Not Set")
swid = os.getenv("SWID", "Not Set")

print("📦 ENV VARIABLES LOADED:")
print(f"📧 EMAIL: {email}")
print(f"🏈 TEAM_ID: {team_id}")
print(f"📘 LEAGUE_ID: {league_id}")
print(f"🍪 ESPN_S2: {'Loaded' if espn_s2 != 'Not Set' else 'Missing'}")
print(f"🍪 SWID: {'Loaded' if swid != 'Not Set' else 'Missing'}")

print("\n⏳ Pausing for 5 seconds...")
time.sleep(5)

print("✅ Diagnostic test completed. You ARE seeing this from main.py ✅")
