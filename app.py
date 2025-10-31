import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "APP_MESSAGE not set")
    return f"<h1>{message}</h1>"

@app.route("/health")
def health():
    return os.getenv("APP_HEALTH", "APP_HEALTH not set")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
