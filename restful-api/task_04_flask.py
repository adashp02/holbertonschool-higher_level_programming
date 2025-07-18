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
        return jsonify({"error": "User not found"}), 404
    
#/add_user - function with POST method, parsing incoming data into the list of users
@app.route("/add_user", methods=["POST"])
def add_user():
    if request.get_json is None:
        return jsonify({"error": "Username is required"}), 400
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

"""initialize the Flask server"""
if __name__ == "__main__":
    app.run()
