import json
import os
from datetime import datetime

REF_FILE = "referrals.json"

def load_referrals():
    if not os.path.exists(REF_FILE):
        return []
    with open(REF_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_referrals(data):
    with open(REF_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("\n✅ referrals.json successfully updated!")

def add_referral_group():
    data = load_referrals()
    print("\n--- CAMILLA SWEEPS REFERRAL MANAGER ---")
    
    referrer_name = input("Enter Referrer Real Name/Username: ").strip()
    if not referrer_name:
        print("Error: Referrer name cannot be empty.")
        return
        
    referrer_link = input("Enter Referrer Facebook Link (press Enter to skip): ").strip() or "#"
    
    print("\nNow enter the referred players (press Enter on empty name when done):")
    players = []
    while True:
        p_name = input("  Referred Player Name: ").strip()
        if not p_name:
            break
        p_link = input(f"  {p_name}'s Facebook Link (press Enter to skip): ").strip() or "#"
        players.append({"name": p_name, "link": p_link})
        
    status = input("Status [1: Active & Verified, 2: Pending, 3: Bonus Claimed]: ").strip()
    status_map = {"1": "Active & Verified", "2": "Pending Verification", "3": "Bonus Claimed"}
    status_str = status_map.get(status, "Active & Verified")
    
    new_entry = {
        "id": int(datetime.now().timestamp()),
        "referrerName": referrer_name,
        "referrerLink": referrer_link,
        "players": players,
        "status": status_str,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    
    data.append(new_entry)
    save_referrals(data)

if __name__ == "__main__":
    add_referral_group()
