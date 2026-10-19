import json
import os

DATA_FILE = "players.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("\n✅ Database updated locally!")

def show_players(players):
    print("\n--- CURRENT PLAYERS ---")
    for idx, p in enumerate(players):
        net = p['deposits'] - p['cashouts']
        print(f"[{idx + 1}] {p['name']} ({p['handle']}) | Dep: ${p['deposits']} | Cashout: ${p['cashouts']} | Net Win: ${net}")

def record_transaction():
    players = load_data()
    show_players(players)
    choice = int(input("\nSelect Player # to update: ")) - 1
    player = players[choice]
    
    print(f"\nUpdating {player['name']}:")
    print("1. Add Deposit")
    print("2. Add Cashout")
    print("3. Update Notes")
    action = input("Select action (1-3): ")
    
    if action == "1":
        amt = float(input("Deposit Amount ($): "))
        player['deposits'] += amt
        if player['matchUsed'] < 5:
            player['matchUsed'] += 1
            print(f"🎉 Deposit match applied! ({player['matchUsed']}/5 used)")
    elif action == "2":
        amt = float(input("Cashout Amount ($): "))
        player['cashouts'] += amt
    elif action == "3":
        note = input("Enter new notes: ")
        player['notes'] = note
        
    save_data(players)

def add_new_player():
    players = load_data()
    print("\n--- ADD NEW VIP PLAYER ---")
    name = input("Player Full Name: ")
    handle = input("Social Handle (e.g. @username): ")
    tier = input("Tier (Bronze / Silver / Gold / Platinum VIP): ") or "Gold VIP"
    channel = input("Preferred Cashout Channel (e.g. Chime / Cash App): ")
    
    new_p = {
        "id": f"CS-{1000 + len(players) + 1}",
        "name": name,
        "handle": handle,
        "tier": tier,
        "deposits": 0.0,
        "cashouts": 0.0,
        "matchUsed": 0,
        "platformAccounts": {},
        "cashoutChannel": channel,
        "notes": "New registration"
    }
    players.append(new_p)
    save_data(players)

def reset_database():
    confirm = input("\n⚠️ Are you sure you want to RESET database to 0? (type 'YES'): ")
    if confirm == "YES":
        initial_data = [
            {
                "id": "CS-1001",
                "name": "Trinia Hoolan",
                "handle": "@trinia_k",
                "tier": "Gold VIP",
                "deposits": 0.0,
                "cashouts": 15.0,
                "matchUsed": 1,
                "platformAccounts": {"OS": "TriniaOS777"},
                "cashoutChannel": "Chime",
                "notes": "Left $10 balance on Orionstars with freeplay bonus."
            },
            {
                "id": "CS-1002",
                "name": "Christi Ranson",
                "handle": "@christi_r",
                "tier": "Silver VIP",
                "deposits": 0.0,
                "cashouts": 0.0,
                "matchUsed": 0,
                "platformAccounts": {"OS": "ChristiOrion"},
                "cashoutChannel": "Cash App",
                "notes": "Referred boyfriend via Telegram @Camilla777."
            }
        ]
        save_data(initial_data)
        print("✅ Database reset to clean state!")

def main():
    while True:
        print("\n====================================")
        print("  CAMILLA SWEEPS VIP MANAGER (PYTHON)")
        print("====================================")
        print("1. View All Players & Financials")
        print("2. Record Deposit / Cashout / Note")
        print("3. Add New VIP Player")
        print("4. Reset Database to Clean State")
        print("5. Exit")
        
        choice = input("Select choice (1-5): ")
        if choice == "1":
            show_players(load_data())
        elif choice == "2":
            record_transaction()
        elif choice == "3":
            add_new_player()
        elif choice == "4":
            reset_database()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
