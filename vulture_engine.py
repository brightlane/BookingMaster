import json
import random
from datetime import datetime

# Vulture 10K Target List: 2026 Host Cities
host_cities = [
    {"city": "Miami", "stadium": "Hard Rock Stadium", "region": "South"},
    {"city": "Los Angeles", "stadium": "SoFi Stadium", "region": "West"},
    {"city": "New York", "stadium": "MetLife Stadium", "region": "East"},
    {"city": "Dallas", "stadium": "AT&T Stadium", "region": "Central"},
    {"city": "Mexico City", "stadium": "Estadio Azteca", "region": "Mexico"}
]

def generate_vulture_content():
    # 1. Generate the Daily Sniped Inventory
    inventory = {
        "sync_time": datetime.now().strftime("%B %d, %Y"),
        "timestamp": datetime.now().isoformat(),
        "deals": []
    }

    for item in host_cities:
        discount = random.choice([35, 40, 45, 50, 55])
        inventory["deals"].append({
            "location": item["city"],
            "venue": item["stadium"],
            "saving": f"{discount}%",
            "urgency": f"Only {random.randint(2, 9)} rooms left at this rate",
            "headline": f"2026 Inventory Alert: {item['city']} Stays Near {item['stadium']}"
        })

    # 2. Save for the UI to consume
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)
    
    print(f">> Vulture 10K: Content matrix regenerated for {len(host_cities)} cities.")

if __name__ == "__main__":
    generate_vulture_content()
