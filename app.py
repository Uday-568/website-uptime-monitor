from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "uptime_data.json"

# Create JSON file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


# Function to check website status
def check_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if 200 <= response.status_code < 400:
            return "Online"
        elif 400 <= response.status_code < 500:
            return "Client Error"
        else:
            return "Server Error"

    except requests.exceptions.RequestException:
        return "Offline"


@app.route("/", methods=["GET", "POST"])
def index():

    status = None
    url = None

    if request.method == "POST":
        url = request.form["url"]

        status = check_website(url)

        entry = {
            "url": url,
            "status": status,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        # Safely read JSON data
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(entry)

        # Save updated data
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    # Load data for display
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    return render_template("index.html", status=status, data=data, url=url)


@app.route("/chart-data")
def chart_data():

    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
    except:
        data = []

    online = sum(1 for d in data if d["status"] == "Online")
    offline = sum(1 for d in data if d["status"] == "Offline")
    error = sum(1 for d in data if "Error" in d["status"])

    return jsonify({
        "online": online,
        "offline": offline,
        "error": error
    })


if __name__ == "__main__":
    app.run(debug=True)