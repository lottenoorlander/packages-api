# load the file
# create endpoint
# create search mechanics


from flask import Flask
import data

 
app = Flask(__name__)

@app.route("/search")
def hello(): 
    return "Hello I'm Lotty!"