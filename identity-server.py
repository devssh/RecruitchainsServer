from flask import Flask
from ecdsa import SigningKey
import json

app = Flask(__name__)


@app.route("/user/<username>q   ")
def profile():
    publicKey = 1
    privateKey = 1
    return json.dumps({
        'publicKey': publicKey,
        'privateKey': privateKey
    })


@app.route('/register', methods=['POST'])
def register():
    privateKey = SigningKey.generate()
    publicKey = privateKey.get_verifying_key()
    return False
