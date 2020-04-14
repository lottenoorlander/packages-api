# load the file
# create endpoint
# create search mechanics


from flask import Flask
from data.adduser import adduser

 
app = Flask(__name__)

@app.route("/search")
def hello(): 
    return adduser