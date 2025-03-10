from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, CI/CD!"

# New /status endpoint


@app.route('/status')
def status():
    return jsonify({"status": "OK", "message": "Service is running"}), 200


if __name__ == "__main__":
    app.run()
