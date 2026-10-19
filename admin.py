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
    print("\n--- CURRENT REGISTERED PLAYERS ---")
    for idx, p in enumerate(players):
        net = p['deposits'] - p['cashouts']
        fb = p.get('fbProfile', 'No FB Link')
        print(f"[{idx + 1}] {p['name']} ({p['tier']}) | FB: {fb} | Dep: ${p['deposits']} | Cashout: ${p['cashouts']}")

def record_transaction():
    players = load_data()
    if not players:
        print("No players found!")
        return
    show_players(players)
    choice = int(input("\nSelect Player # for transaction: ")) - 1
    player = players[choice]
    
    print(f"\nQuick Transaction for {player['name']}:")
    print("1. Add Deposit")
    print("2. Add Cashout")
    print("3. Update Notes")
    action = input("Select action (1-3): ")
    
    if action == "1":
        amt = float(input("Deposit Amount ($): "))
        player['deposits'] += amt
        if player.get('matchUsed', 0) < 5:
            player['matchUsed'] = player.get('matchUsed', 0) + 1
            print(f"🎉 Deposit match applied! ({player['matchUsed']}/5 used)")
    elif action == "2":
        amt = float(input("Cashout Amount ($): "))
        player['cashouts'] += amt
    elif action == "3":
        note = input("Enter new notes: ")
        player['notes'] = note
        
    save_data(players)

def edit_player_profile():
    players = load_data()
    if not players:
        print("No players found!")
        return
    show_players(players)
    choice = int(input("\nSelect Player # to EDIT: ")) - 1
    p = players[choice]
    
    print(f"\n--- EDITING PROFILE: {p['name']} ---")
    print(f"1. Name (Current: {p['name']})")
    print(f"2. Facebook Profile Link (Current: {p.get('fbProfile', 'None')})")
    print(f"3. VIP Tier (Current: {p['tier']})")
    print(f"4. Preferred Cashout Channel (Current: {p['cashoutChannel']})")
    print(f"5. Total Deposits (Current: ${p['deposits']})")
    print(f"6. Total Cashouts (Current: ${p['cashouts']})")
    print(f"7. Signup Match Used Count (Current: {p.get('matchUsed', 0)}/5)")
    print("8. Cancel")
    
    field = input("\nSelect field to edit (1-8): ")
    if field == "1":
        p['name'] = input("New Name: ")
    elif field == "2":
        p['fbProfile'] = input("New Facebook Profile URL (https://facebook.com/...): ")
    elif field == "3":
        p['tier'] = input("New VIP Tier (Bronze/Silver/Gold/Platinum VIP): ")
    elif field == "4":
        p['cashoutChannel'] = input("New Cashout Handle (e.g. Chime / Cash App): ")
    elif field == "5":
        p['deposits'] = float(input("Set Total Deposits ($): "))
    elif field == "6":
        p['cashouts'] = float(input("Set Total Cashouts ($): "))
    elif field == "7":
        p['matchUsed'] = int(input("Set Signup Match Count (0-5): "))
    elif field == "8":
        return
        
    save_data(players)

def add_new_player():
    players = load_data()
    print("\n--- ADD NEW VIP PLAYER ---")
    name = input("Player Full Name: ")
    fb_link = input("Facebook Profile URL (e.g. https://facebook.com/username): ")
    tier = input("VIP Tier (Bronze / Silver / Gold / Platinum VIP) [Default: Gold VIP]: ") or "Gold VIP"
    channel = input("Preferred Cashout Channel (e.g. Chime / Cash App): ")
    
    new_p = {
        "id": f"CS-{1000 + len(players) + 1}",
        "name": name,
        "fbProfile": fb_link,
        "tier": tier,
        "deposits": 0.0,
        "cashouts": 0.0,
        "matchUsed": 0,
        "cashoutChannel": channel,
        "notes": "New registration"
    }
    players.append(new_p)
    save_data(players)

def main():
    while True:
        print("\n====================================")
        print("  CAMILLA SWEEPS VIP MANAGER (PYTHON)")
        print("====================================")
        print("1. View All Players & Financials")
        print("2. Quick Deposit / Cashout / Note")
        print("3. Edit Existing Player Profile")
        print("4. Add New VIP Player")
        print("5. Exit")
        
        choice = input("Select choice (1-5): ")
        if choice == "1":
            show_players(load_data())
        elif choice == "2":
            record_transaction()
        elif choice == "3":
            edit_player_profile()
        elif choice == "4":
            add_new_player()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
