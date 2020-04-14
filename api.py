from flask import Flask
from flask import request
import json
import data

app = Flask(__name__)


@app.route("/search", methods=['GET'])
def returnSearchResults():
    searchQuery = request.args.get('searchQuery')
    result = [
        package for package in data.packages if package.contains(searchQuery)]
    return json.dumps(result, default=obj_dict)


def obj_dict(obj):
    return obj.__dict__
