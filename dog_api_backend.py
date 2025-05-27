from flask import Flask, jsonify
from flask_cors import CORS
import urllib.request
import json

app = Flask(__name__)
CORS(app)

BASE_DOG_API = 'https://dogapi.dog/api/v2'

# Helper function to make requests with a valid User-Agent header
def fetch_dog_api(endpoint):
    try:
        url = f"{BASE_DOG_API}{endpoint}"
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        return {"error": str(e)}

@app.route("/breeds")
def get_breeds():
    return jsonify(fetch_dog_api("/breeds"))

@app.route("/breeds/<breed_id>")
def get_breed_by_id(breed_id):
    return jsonify(fetch_dog_api(f"/breeds/{breed_id}"))

@app.route("/facts")
def get_facts():
    return jsonify(fetch_dog_api("/facts"))

@app.route("/groups")
def get_groups():
    return jsonify(fetch_dog_api("/groups"))

@app.route("/groups/<group_id>")
def get_group_by_id(group_id):
    return jsonify(fetch_dog_api(f"/groups/{group_id}"))

@app.route("/group-details/<group_id>")
def get_group_details(group_id):
    group = fetch_dog_api(f"/groups/{group_id}")
    all_breeds = fetch_dog_api("/breeds")
    if "data" in all_breeds:
        breeds = [
            b for b in all_breeds["data"]
            if b["relationships"]["group"]["data"]["id"] == group_id
        ]
        return jsonify({"group": group, "breeds": breeds})
    return jsonify({"group": group, "breeds": []})

@app.route("/group-details/<group_id>/breed/<breed_id>")
def get_group_breed_detail(group_id, breed_id):
    group = fetch_dog_api(f"/groups/{group_id}")
    breed = fetch_dog_api(f"/breeds/{breed_id}")
    return jsonify({"group": group, "breed": breed})

if __name__ == "__main__":
    app.run(debug=True)
