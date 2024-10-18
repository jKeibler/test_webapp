from flask import Flask
import os


#Creating the flask app
app = Flask(__name__)

#To run this app from terminal execute the following command
#flask --run app run --host=0.0.0.0

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"