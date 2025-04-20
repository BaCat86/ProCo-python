import requests

BASE_URL = "http://127.0.0.1:8000/items"

def create_item(item_id, name, price):
    response = requests.post(f"{BASE_URL}/{item_id}", json={"name": name, "price": price})
    return response.json()

def read_item(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}")
    return response.json()

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}")
    return response.json()

if __name__ == "__main__":
    # Create an item
    print(create_item(1, "Apple", 0.99))
