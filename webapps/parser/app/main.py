import requests
import re
from flask import Flask, jsonify, request
app = Flask(__name__)

MULTIPLICATIVE = re.compile(r"(?P<left>.*?)(?P<operator>\*|\/)(?P<right>.*)")
ADDIDITIVE     = re.compile(r"(?P<left>.*?)(?P<operator>\+|\-)(?P<right>.*)")
NUM            = re.compile(r"\s*(\d+(?:\.\d+)?)\s*")


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

        return str(evaluate(expression)) + "\n"

    return jsonify({"error":"Nothing to do"})


def evaluate(expression):
    match = ADDIDITIVE.fullmatch(expression)
    if match is None:
        match = MULTIPLICATIVE.fullmatch(expression)
    if match is None:
        print(f"Expression '{expression}' not understood")
        return 0

    left = match.group("left").strip()
    op = match.group("operator").strip()
    right = match.group("right").strip()

    if NUM.fullmatch(left):
        left = float(left)
    else:
        left = evaluate(left)


    if NUM.fullmatch(right):
        right = float(right)
    else:
        right = evaluate(right)

    request_data = {
            "terms": [left, right]
    }
    response = requests.post(URLS[op], json=request_data)
    return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
