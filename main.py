# Required libraries
from flask import Flask, request
from gevent.pywsgi import WSGIServer

# App setup
app = Flask(__name__)
appHost = "127.0.0.1" # IP Address
appPort = 13337       # Port

# Secret token shared with gameintegration cfg
secretKey = "a9sdua0sd9ia09sdia09sid"

# Tell the server to listen on /gameint and only accept POST requests
@app.route("/gameint", methods=["POST"])
def gameint():
    # Use a try statement to see if the data is valid
    try:
        data = request.json
    except:
        return "Invalid data"
    # Make sure the secret key is valid
    if "auth" not in data or "token" not in data["auth"]:
        return ""
    if data["auth"]["token"] != secretKey:
        return ""

    # Do stuff with the data
    print(data)

# Run the server
server = WSGIServer((appHost, 13337), app)
server.serve_forever()
