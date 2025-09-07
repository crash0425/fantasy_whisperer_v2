import os
import time

print("\n[✓] Fantasy Whisperer is live on Render 🎉")

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
print(f"🧁 SWID: {'✅ Loaded' if swid else '❌ MISSING'}")

# Infinite loop to simulate bot running
while True:
    print("\n[🔁] Checking fantasy football data...")
    # Future logic will go here
    time.sleep(60)
