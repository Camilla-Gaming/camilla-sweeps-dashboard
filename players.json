import json
import os

DATA_FILE = "players.json"

def load_players():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_players(players):
    with open(DATA_FILE, "w") as f:
        json.dump(players, f, indent=2)
    print("✅ Player database updated successfully!")

def add_player():
    players = load_players()
    print("\n--- ➕ Add New VIP Player ---")
    name = input("Player Name: ")
    tier = input("Tier (Bronze / Silver / Gold / Platinum VIP): ") or "Gold VIP"
    messenger = input("Messenger Name/Handle: ")
    telegram = input("Telegram Handle: ")
    cashout_handle = input("Preferred Cashout Channel (e.g. Chime / Cash App): ")
    
    new_player = {
        "id": f"CS-{1001 + len(players)}",
        "name": name,
        "tier": tier,
        "status": "Active",
        "contact": {
            "messenger": messenger,
            "telegram": telegram,
            "preferred": "Messenger"
        },
        "platforms": [],
        "financials": {
            "totalDeposits": 0.00,
            "totalCashouts": 0.00,
            "preferredCashout": cashout_handle,
            "signupMatchUsed": 0,
            "signupMatchMax": 5
        },
        "rules": {
            "minCashoutMultiplier": 4,
            "maxCashoutMultiplier": 10
        },
        "referrals": {
            "referredBy": None,
            "invitedPlayers": [],
            "bonusEarned": 0.00
        },
        "notes": ""
    }
    
    players.append(new_player)
    save_players(players)

def main():
    while True:
        print("\n=== CAMILLA SWEEPS VIP COMMAND CENTER ===")
        print("1. View All Players")
        print("2. Add New Player")
        print("3. Exit")
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            players = load_players()
            print(f"\nTotal Registered Players: {len(players)}")
            for p in players:
                print(f"• [{p['id']}] {p['name']} ({p['tier']}) - Cashout: {p['financials']['preferredCashout']}")
        elif choice == "2":
            add_player()
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
