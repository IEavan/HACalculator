import functools
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def execute():
    if request.is_json:
        data = request.get_json()
        return jsonify(functools.reduce((lambda x,y: x * y), data["terms"]))
    return jsonify({"error":"request is not json"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)
