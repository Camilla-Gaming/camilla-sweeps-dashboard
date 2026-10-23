import json
import os

# The 50 master passcodes hardcoded into halloween.html
MASTER_CODES = [
    "CAMILLA-1011", "CAMILLA-1022", "CAMILLA-1033", "CAMILLA-1044", "CAMILLA-1055",
    "CAMILLA-1066", "CAMILLA-1077", "CAMILLA-1088", "CAMILLA-1099", "CAMILLA-1100",
    "CAMILLA-2011", "CAMILLA-2022", "CAMILLA-2033", "CAMILLA-2044", "CAMILLA-2055",
    "CAMILLA-2066", "CAMILLA-2077", "CAMILLA-2088", "CAMILLA-2099", "CAMILLA-2200",
    "CAMILLA-3011", "CAMILLA-3022", "CAMILLA-3033", "CAMILLA-3044", "CAMILLA-3055",
    "CAMILLA-3066", "CAMILLA-3077", "CAMILLA-3088", "CAMILLA-3099", "CAMILLA-3300",
    "CAMILLA-4011", "CAMILLA-4022", "CAMILLA-4033", "CAMILLA-4044", "CAMILLA-4055",
    "CAMILLA-4066", "CAMILLA-4077", "CAMILLA-4088", "CAMILLA-4099", "CAMILLA-4400",
    "CAMILLA-5011", "CAMILLA-5022", "CAMILLA-5033", "CAMILLA-5044", "CAMILLA-5055",
    "CAMILLA-5066", "CAMILLA-5077", "CAMILLA-5088", "CAMILLA-5099", "CAMILLA-5500"
]

JSON_FILE = "halloween.json"

def load_used_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def main():
    used_records = load_used_data()
    burned_codes = {item["passcode"] for item in used_records if "passcode" in item}
    
    available_codes = [code for code in MASTER_CODES if code not in burned_codes]

    print("\n==================================================")
    print("      🎃 CAMILLA PROMOS PASSCODE STATUS 🎃      ")
    print("==================================================")
    print(f" Total Master Passcodes: {len(MASTER_CODES)}")
    print(f" 🟢 Available Passcodes: {len(available_codes)}")
    print(f" 🔴 Burned/Used Passcodes: {len(burned_codes)}")
    print("--------------------------------------------------\n")

    print("🟢 AVAILABLE PASSCODES TO SEND TO PLAYERS:")
    if available_codes:
        # Display in 5 columns for easy copying
        for i in range(0, len(available_codes), 5):
            chunk = available_codes[i:i+5]
            print("  " + "   ".join(chunk))
    else:
        print("  None left! All passcodes have been used.")

    print("\n--------------------------------------------------")
    print("🔴 BURNED / USED PASSCODES LOG:")
    if used_records:
        for item in used_records:
            print(f"  • Passcode: {item.get('passcode', 'N/A')} | Player: {item.get('username', 'N/A')} | Bonus: {item.get('bonus', 'N/A')} | Date: {item.get('date', 'N/A')}")
    else:
        print("  No passcodes logged as burned in halloween.json yet.")

    print("\n==================================================\n")

if __name__ == "__main__":
    main()
