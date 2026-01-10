from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    if not name:
        return "Missing query parameter"

    return f"HELLO, {name.upper()}"

if __name__ == "__main__":
    app.run(debug=True)
