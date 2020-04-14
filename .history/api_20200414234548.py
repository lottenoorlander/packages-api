from flask import Flask
import json
import data

app = Flask(__name__)


@app.route("/search")
def returnSearchResults():

    return json.dumps(data.packages[2].__dict__)
