# load the file
# create endpoint
# create search mechanics


from flask import Flask
import json
import data

app = Flask(__name__)


@app.route("/search")
def hello():
    # return json.dumps(data.data.__dict__)
    return json.dumps(data.packages[2].__dict__)
