from flask import Flask
from flask import request
import json
import data

app = Flask(__name__)


@app.route("/search", methods=['GET'])
def returnSearchResults():
    searchQuery = request.args.get('searchQuery')
    result = data.packages[2].__dict__
    # return json.dumps(result)
    return searchQuery
