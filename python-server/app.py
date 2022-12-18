import flask
from flask import request,json, jsonify
from flask_mysqldb import MySQL

app=flask.Flask(__name__)

app.config["DEBUG"]=True

@app.route('/home',methods=['GET'])
def welcome():
    return("welcome to my programmeaaa")


if __name__=='__main__':
    app.run()
