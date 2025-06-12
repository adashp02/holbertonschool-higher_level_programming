#!/usr/bin/python3
"""Building simple web server with Flask"""

from flask import Flask, jsonify, request

"""Instantiate a Flask web server from the Flask module"""
app = Flask(__name__)

users = {}

"""Define a route for the root URL (“/”)
and create a function with flask decorator
"""
@app.route("/")
def home():
    return("Welcome to the Flask API!")

#handle /data endpoint - return the list of users with jsonify
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

#handle /status
@app.route("/status")
def get_status():
    return "OK"

#handle /users/<username> return full object corresponding to the username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "user not found"}), 404
    
#/add_user - function with POST method, parsing incoming data into the list of users
@app.route("/add_user", methods=["POST"])
def add_user():
    req_data = request.get_json
    if req_data is None or req_data("username") is None:
        return jsonify({"error": "Username is required"}), 400
    user = {
        "username": req_data("username"),
        "name": req_data("name"),
        "age": req_data("age"),
        "city": req_data("city")
    }
    users[req_data("username")] = user
    return jsonify({"message": "User added", "user": user}), 201

"""initialize the Flask server"""
if __name__ == "__main__":
    app.run()
