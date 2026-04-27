import json
import random
from datetime import datetime

# A small sample of the "10,000" potential targets
cities = ["New York", "London", "Tokyo", "Paris", "Dubai", "Miami", "Las Vegas", "Rome"]
deals = [40, 45, 50, 55]

def generate_inventory():
    inventory = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "featured_deals": []
    }
    
    # Generate 5 fresh "sniped" deals for the day
    for _ in range(5):
        deal = {
            "city": random.choice(cities),
            "discount": random.choice(deals),
            "active_users": random.randint(10, 100)
        }
        inventory["featured_deals"].append(deal)
    
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)
    
    print(f"Vulture 10K: Inventory updated at {inventory['last_updated']}")

if __name__ == "__main__":
    generate_inventory()
