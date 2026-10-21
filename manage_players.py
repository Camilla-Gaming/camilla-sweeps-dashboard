import json
import os

DB_FILE = "players.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(players):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2)
    print("Database successfully updated and saved locally!")

def add_or_update_player():
    players = load_data()
    
    print("\n--- CAMILLA SWEEPS PLAYER MANAGER ---")
    name = input("Enter player username/name: ").strip()
    
    # Check if player already exists
    player = next((p for p in players if p["name"].lower() == name.lower()), None)
    
    if player:
        print(f"Found existing player: {player['name']}. Updating values...")
        deposits_add = float(input(f"Add to deposits (current: ${player['deposits']}): $") or 0)
        cashouts_add = float(input(f"Add to cashouts (current: ${player['cashouts']}): $") or 0)
        
        player["deposits"] += deposits_add
        player["cashouts"] += cashouts_add
    else:
        print("Creating new player entry...")
        tier = input("Enter Tier (e.g. VIP Gold, Standard): ").strip() or "Standard"
        deposits = float(input("Initial Deposit ($): ") or 0)
        cashouts = float(input("Initial Cashout ($): ") or 0)
        channel = input("Payout Handle (Cash App / Chime / Venmo): ").strip() or "Cash App"
        fb_link = input("Facebook Profile Link: ").strip() or "#"
        notes = input("Notes: ").strip() or "Added via Python tool."
        
        new_player = {
            "name": name,
            "fbProfile": fb_link,
            "tier": tier,
            "deposits": deposits,
            "cashouts": cashouts,
            "cashoutChannel": channel,
            "matchUsed": 1,
            "notes": notes
        }
        players.append(new_player)
    
    save_data(players)

if __name__ == "__main__":
    add_or_update_player()
