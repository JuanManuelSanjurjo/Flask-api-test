from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def get_user(user_id):
    data = {
        "name":"Juan Manuel",
        "surname": "Sanjurjo",
        "birth": "20-11-1989"
    }

    extra = request.args.get("extra")
    if extra:
        data["extra"] = extra

    return jsonify(data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
    
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)