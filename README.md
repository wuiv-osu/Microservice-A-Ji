# Microservice-A-Ji

Microservice that saves, loads, and deletes recipes from/to a JSON file using REST API

Requesting Data:
1. Get recipe information from main program
2. Send ID, title, and image URL to microservice with POST and DELETE, depending on required usage
3. Send data in JSON format via "requests"

Example call for POST-
import requests

recipe = {
    "id": 123,
    "title": "Spaghetti Carbonara",
    "image": "https://example.com/image.jpg"
}

response = requests.post("http://localhost:5001/save-recipe", json=recipe)


Receiving Data:
1. Send GET request using "requests" to microservice
2. Microservice will dump JSON file and return it

Example call for GET:
import requests

response = requests.get("http://localhost:5001/saved-recipes")
recipes = response.json()
