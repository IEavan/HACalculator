import requests
import re
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

MULTIPLICATIVE = re.compile(r"(?P<left>.*?)(?P<operator>\*|\/)(?P<right>.*)")
ADDIDITIVE     = re.compile(r"(?P<left>.*?)(?P<operator>\+|\-)(?P<right>.*)")
NUM            = re.compile(r"\s*(\d+)\s*")


URLS = {
        "+": "http://adder",
        "-": "http://subtractor",
        "*": "http://multiplier",
        "/": "http://divider"
}

@app.route("/", methods=["POST"])
def execute():
    if request.is_json:
        data = request.get_json()
        expression = data["expression"]

        match = ADDIDITIVE.fullmatch(expression)
        if match is not None:
            left = int(match.group("left"))
            op = match.group("operator").strip()
            right = int(match.group("right"))
            

        
        match = MULTIPLICATIVE.fullmatch(expression)
        if match is not None:
            left = int(match.group("left"))
            op = match.group("operator").strip()
            right = int(match.group("right"))


        print(f"left = {left}, op = {op}, right = {right}")
        request_data = {
                "terms": [left, right]
        }
        response = requests.post(URLS[op], data=json.dumps(request_data))

        return jsonify(response.body)

    return jsonify({"error":"Nothing to do"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)