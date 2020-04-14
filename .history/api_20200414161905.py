# load the file
# create endpoint
# create search mechanics


from flask import Flask
import json
import data

app = Flask(__name__)


@app.route("/search")
def hello():
    print(json.dumps(data.adduser.__dict__))
    return data.adduser
