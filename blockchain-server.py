from flask import Flask
from ecdsa import SigningKey
import json

app = Flask(__name__)


@app.route("/")
def hello():
    privateKey = SigningKey.generate()
    publicKey = privateKey.get_verifying_key()
    data = "data".encode('utf-8')
    signature = privateKey.sign(data)
    assert publicKey.verify(signature, data)
    publicKey = "".join(publicKey.to_pem().decode().split("\n")[1:-2])

    txn = {
        'txnIndex': 1,
        'signature': signature.hex(),
        'previousSignature': signature.hex(),
        'publicKey': publicKey,
        'data': data.decode()
    }

    block = {
        'blockNumber': 1,
        'txns': [txn]
    }

    blockSign = privateKey.sign(json.dumps(block).encode('utf-8'))

    return json.dumps({
        'signature': blockSign.hex(),
        'block': block
    })
