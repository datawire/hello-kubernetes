#!/usr/bin/env python

import os
import datetime

from flask import Flask, jsonify
app = Flask(__name__)


# ----------------------------------------------------------------------------------------------------------------------
# SUPPLEMENTAL CODE
# ----------------------------------------------------------------------------------------------------------------------

#@app.route("/quote", methods=["GET"])
#def hello_with_quote():
#    import urllib.request
#    import json
#
#    res = urllib.request.urlopen("http://qotm")
#    data = res.read()
#
#    return jsonify(message="Hello from Kubernetes!",
#                   quote=json.loads(data.decode('utf-8')),
#                   hostname=os.getenv("HOSTNAME"),
#                   time=datetime.datetime.now().isoformat())


@app.route("/", methods=["GET"])
def hello():
    return jsonify(message="Hello from Kubernetes!",
                   hostname=os.getenv("HOSTNAME"),
                   time=datetime.datetime.now().isoformat()),


@app.route("/health", methods=["GET", "HEAD"])
def health():
    return "", 200


def main():
    app.run(debug=False, host="0.0.0.0")


if __name__ == "__main__":
    main()
