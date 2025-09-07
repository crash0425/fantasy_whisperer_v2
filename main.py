import os
from espn_api.football import League
from datetime import datetime
import time

def main():
    # Load from environment variables
    email = os.getenv('EMAIL')
    team_id = os.getenv('TEAM_ID')
    league_id = os.getenv('LEAGUE_ID')
    year = 2025
    swid = os.getenv('SWID')
    espn_s2 = os.getenv('ESPN_S2')

    print("🏈 Fantasy Whisperer is Live on Render 🟢")
    print(f"📧 Email: {email}")
    print(f"📘 League ID: {league_id}")
    print(f"🏈 Team ID: {team_id}")

    print("🧠 ESPN_S2 ✅ Loaded" if espn_s2 else "❌ ESPN_S2 MISSING")
    print("🧠 SWID ✅ Loaded" if swid else "❌ SWID MISSING")

    # Debug logs
    print(f"[DEBUG] Using League ID: {league_id}")
    print(f"[DEBUG] Using Season: {year}")
    print(f"[DEBUG] SWID: {swid}")
    print(f"[DEBUG] ESPN_S2: {espn_s2[:15]}...(truncated)")

    # Connect to league (add debug=True for more info)
    print("📡 Connecting to ESPN league...")
    try:
        league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid, debug=True)
        print("✅ Connected to ESPN API")

        # Sample usage — get team names
        for team in league.teams:
            print(f"🏆 Team: {team.team_name} | Owner: {team.owner}")

        print("🎉 Fantasy Whisperer is running...")

    except Exception as e:
        print("❌ ERROR connecting to ESPN League API")
        print(str(e))

if __name__ == "__main__":
    while True:
        main()
        print(f"🔁 Sleeping 24h... [{datetime.now()}]")
        time.sleep(86400)  # Run once per day
