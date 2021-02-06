from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def execute():
    if request.is_json:
        data = request.get_json()
        left = data["terms"][0]
        right = data["terms"][1]
        return jsonify(left - right)
    return jsonify({"error":"request is not json"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
