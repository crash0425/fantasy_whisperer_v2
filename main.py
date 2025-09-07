from espn_api.football import League
import os
import time

print("\n🚀 Fantasy Whisperer is live on Render 🎉")

# Read environment variables
email = os.getenv("EMAIL")
team_id = int(os.getenv("TEAM_ID"))
league_id = int(os.getenv("LEAGUE_ID"))
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

# Confirm environment variables
print(f"📧 Email: {email}")
print(f"🆔 Team ID: {team_id}")
print(f"🏆 League ID: {league_id}")
print(f"🍪 ESPN_S2: {'✅ Loaded' if espn_s2 else '❌ MISSING'}")
print(f"🍪 SWID: {'✅ Loaded' if swid else '❌ MISSING'}")

# Connect to league
print("🔌 Connecting to ESPN league...")
league = League(league_id=league_id, year=2025, espn_s2=espn_s2, swid=swid)
print("✅ Connected to league.")

# Get your team object
my_team = next(team for team in league.teams if team.team_id == team_id)

# Print your team info
print(f"\n🧠 Team Name: {my_team.team_name}")
print(f"👑 Owner: {my_team.owner}")
print(f"💥 Record: {my_team.wins}-{my_team.losses}, Streak: {my_team.streak}")
print("📋 Roster:")
for player in my_team.roster:
    print(f" - {player.name} ({player.position})")

# Bot running loop
while True:
    print(f"\n🧠 [{time.strftime('%Y-%m-%d %H:%M:%S')}] Fantasy Whisperer is running...")
    time.sleep(60)
