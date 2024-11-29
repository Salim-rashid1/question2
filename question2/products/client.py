import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def add_product(name, description, price):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}products", json=data)
    print(f"Response: {response.status_code}, {response.json()}")

def list_products():
    response = requests.get(f"{BASE_URL}products")
    print(f"Response: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    # Add a product
    add_product("Laptop", "A high-performance laptop", 999.99)

    # List all products
    list_products()
