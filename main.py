import os
from espn_api.football import League
from datetime import datetime
import time

print("🔥 Fantasy Whisperer is running...")

# Load environment variables
email = os.getenv("EMAIL")
team_id = int(os.getenv("TEAM_ID"))
league_id = int(os.getenv("LEAGUE_ID"))
year = 2025
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

print("📧 Email:", email)
print("🏈 Team ID:", team_id)
print("📘 League ID:", league_id)
print("🍪 ESPN_S2:", "Loaded" if espn_s2 else "Missing")
print("🍪 SWID:", "Loaded" if swid else "Missing")

try:
    print("🔌 Connecting to ESPN league...")
    league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
    print("✅ League connected.")
    print(f"💥 Team Name: {league.teams[team_id - 1].team_name}")
    print(f"🏆 League Name: {league.settings.name}")
    print(f"📅 Week: {league.current_week}")

except Exception as e:
    print("❌ ERROR connecting to ESPN league:")
    print(e)

print("✅ Fantasy Whisperer has finished setup.")
