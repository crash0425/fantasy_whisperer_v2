import time
from fantasy_whisperer_v2 import config

def simulate_analysis():
    print(f"[INFO] Running fantasy football check for Team {config.TEAM_ID} in League {config.LEAGUE_ID}")
    print("[SIMULATION] Checking lineup, injuries, waivers, and sending email alerts to", config.EMAIL)

if __name__ == "__main__":
    while True:
        simulate_analysis()
        time.sleep(3600)  # Wait for 1 hour
