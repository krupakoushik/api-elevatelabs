from flask import Flask, request, jsonify

app = Flask(__name__)
users = []
uid = 1

@app.route("/users", methods=["GET"])
def all_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    global uid
    data = request.json
    u = {"id": uid, "name": data["name"], "email": data["email"]}
    users.append(u)
    uid += 1
    return jsonify(u)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    for u in users:
        if u["id"] == id:
            return jsonify(u)
    return jsonify({"error":"not found"}), 404

@app.route("/users/<int:id>", methods=["DELETE"])
def del_user(id):
    for u in users:
        if u["id"] == id:
            users.remove(u)
            return jsonify({"status":"deleted"})
    return jsonify({"error":"not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
