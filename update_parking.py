import requests
import json
import os

# Načtení tajného URL z GitHub Secrets
url_auth = os.getenv("AUTH_URL")

try:
    # 1. Získání tokenu
    res_auth = requests.get(url_auth)
    if res_auth.status_code == 200:
        token = res_auth.text.strip().replace('"', '')
    else:
        print(f"Chyba auth: {res_auth.status_code}")
        exit(1)

    # 2. Stažení dat
    url_spots = "https://api.urbiotica.net/v2/organisms/org0e833a/projects/prj0cf247/spots"
    headers = {"accept": "application/json", "IDENTITY_KEY": token}
    
    res_data = requests.get(url_spots, headers=headers)
    if res_data.status_code == 200:
        # Uložení do souboru
        with open("parking_data.json", "w", encoding="utf-8") as f:
            json.dump(res_data.json(), f, ensure_ascii=False, indent=4)
        print("Hotovo, data uložena.")
    else:
        print(f"Chyba dat: {res_data.status_code}")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
