from flask import Flask
import json
import data

app = Flask(__name__)


@app.route("/search", methods=['GET'])
def returnSearchResults(searchQuery):
    result = data.packages[2].__dict__
    return json.dumps(result)
