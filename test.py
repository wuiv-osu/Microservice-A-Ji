import requests

BASE_URL = "http://localhost:5001"

test_recipe = {
    "id": 999,
    "title": "Test Pancakes",
    "image": "https://example.com/pancakes.jpg"
}

def test_save_recipe():
    print("Testing POST /save-recipe...")
    res = requests.post(f"{BASE_URL}/save-recipe", json=test_recipe)
    print("Status Code:", res.status_code)

def test_get_recipes():
    print("Testing GET /saved-recipes...")
    res = requests.get(f"{BASE_URL}/saved-recipes")
    print("Status Code:", res.status_code)
    print("Data:", res.json())

def test_delete_recipe():
    print("Testing DELETE /saved-recipe/<id>...")
    res = requests.delete(f"{BASE_URL}/saved-recipe/{test_recipe['id']}")
    print("Status Code:", res.status_code)

if __name__ == "__main__":  # What the status codes should be
    test_save_recipe()      # Status code: 201
    test_get_recipes()      # Status code: 200
    test_delete_recipe()    # Status code: 204
    test_get_recipes()      # Status code: 200
