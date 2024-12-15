from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/post", methods=["POST"])
def handle_post():
    data = request.json
    return jsonify({"message": "POST request received", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

