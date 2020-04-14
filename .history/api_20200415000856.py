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
    return result

#     • Package name
    # • Version
    # • Description
    # • SHA256 hash
    # • Dependencies, Recommends, Conflicts.
    # ◦ May have specific versions denoted by the syntax (>= 5.2).
    # ◦ May be fulfilled by multiple packages denoted by the | symbol.
