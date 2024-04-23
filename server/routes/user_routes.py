from server.controller.user_controller import UserController
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

user_routes = Blueprint("user", __name__)
userCtrl = UserController()

@user_routes.route("/api/user/<string:id>", endpoint="get-user", methods=['GET'])
@cross_origin()
def getUser(id):
    try:
        user = userCtrl.getUserById(id)
        if user != None:
            userObj = {}
            userObj["id"] = user[4]
            userObj["name"] = user[3]
            userObj["email"] = user[0]
            userObj["telephone"] = user[1]
            userObj["cpf"] = user[2]
            return jsonify(userObj)
        else:
            return {"msg": "User not found"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
    
@user_routes.route("/api/user", endpoint="get-all-users", methods=['GET'])
@cross_origin()
def getUsers():
    try:
        users = userCtrl.getAllUsers()
        userList = []
        if len(users) > 0:
            for user in users:
                userObj = {}
                userObj["id"] = user[4]
                userObj["name"] = user[3]
                userObj["email"] = user[0]
                userObj["cpf"] = user[2]
                userObj["telephone"] = user[1]
                userList.append(userObj)
        return jsonify(userList)
    except Exception as e:
        return {"msg": str(e)}, 500
    
@user_routes.route("/api/user", endpoint="post-user", methods=['POST'])
@cross_origin()
def saveUser():
    try:
        if request.json and 'user' in request.json:
            user = request.json['user']
            userCtrl.postUser(user['name'], user['email'], user['cpf'], user['telephone'])
            return {"msg": "User successfully saved"}, 200
        else:
            return {"msg": "User is empty"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
     
@user_routes.route("/api/user", endpoint="update-user", methods=['PUT'])
@cross_origin()
def updateUser():
    try:
        if request.json and 'user' in request.json:
            user = request.json['user']
            rows = userCtrl.putUser(user["id"], user["name"], user["email"], user["cpf"], user["telephone"])
            if rows == 0:
                return {"msg": "Update failed"}, 500
            return {"msg": "User successfully updated"}, 200
        else:
            return {"msg": "User is empty"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
    
@user_routes.route("/api/user/<string:id>", endpoint="remove-user", methods=['DELETE'])
@cross_origin()
def removeUser(id):
    try:
        rows = userCtrl.deleteUser(id)
        if rows == 0:
            return {"msg": "Delete failed"}, 500
        return {"msg": "User successfully deleted"}, 200
    except Exception as e:
        return {"msg": str(e)}