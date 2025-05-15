# Code is taken from Ji's original main program. The implementation of this microservice is to replace the functions in the main code.
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
SAVED_FILE = "saved_recipes.json"

# Saves a recipe to the local JSON file
@app.route("/save-recipe", methods=["POST"])
def save_recipe():
    data = request.get_json()
    recipe_data = {
        "id": data["id"],
        "title": data["title"],
        "image": data["image"]
    }

    # Check if the file already exists in local directory. If no, create empty list.
    if os.path.exists(SAVED_FILE):
        with open(SAVED_FILE, "r") as f:
            saved = json.load(f)
    else:
        saved = []

    # If item not in list, add it. Program will redirect to "My Recipes" regardless.
    if all(r["id"] != recipe_data["id"] for r in saved):
        saved.append(recipe_data)
        with open(SAVED_FILE, "w") as f:
            json.dump(saved, f)

    return '', 201

# Loads all saved recipes from JSON file
@app.route("/saved-recipes", methods=["GET"])
def get_saved_recipes():
    # Check if the file already exists in local directory. If no, create empty list.
    if os.path.exists(SAVED_FILE):
        with open(SAVED_FILE, "r") as f:
            saved = json.load(f)
    else:
        saved = []

    return jsonify(saved), 200


# Delete saved recipe from JSON file
@app.route("/saved-recipe/<int:recipe_id>", methods=["DELETE"])
def delete_saved_recipe(recipe_id):
    if os.path.exists(SAVED_FILE):
        with open(SAVED_FILE, "r") as f:
            saved = json.load(f)
    else:
        saved = []

    # Remove recipe from list using it's ID
    saved = [r for r in saved if str(r["id"]) != str(recipe_id)]

    # Update the list for the JSON file
    with open(SAVED_FILE, "w") as f:
        json.dump(saved, f)

    return '', 204

if __name__ == "__main__":
    app.run(port=5001, debug=True)