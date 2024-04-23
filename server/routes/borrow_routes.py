from server.controller.borrow_controller import BorrowController
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

borrow_routes = Blueprint("borrow", __name__)
borrowCtrl = BorrowController()

@borrow_routes.route("/api/book/borrow", methods=['POST'])
@cross_origin()
def borrow():
    try:
        if request.json and 'borrow' in request.json:
            borrow = request.json["borrow"]
            affected = borrowCtrl.borrowBook(borrow["userId"], borrow["bookId"])
            print(affected)
            if affected == 1:
                return {"msg": "Successfully borrowed"}, 200
            else:
                return {"msg": "Borrow failed"}
        else:
            return {"msg": "Borrow not found"}, 500
    except Exception as e:
        return {"msg": "teste" + str(e)}, 500   
    
    
@borrow_routes.route("/api/book/borrow", methods=['GET'])
@cross_origin()
def getBorrows():
    try:
        borrows = borrowCtrl.getAllBorrows()
        borrowList = []
        if len(borrows) > 0:
            for borrow in borrows:
                borrowObj = {}
                borrowObj["bookId"] = borrow[0]
                borrowObj["userId"] = borrow[1]
                borrowObj["book"] = borrow[2]
                borrowObj["user"] = borrow[3]

                borrowList.append(borrowObj)
        return jsonify(borrowList)
    except Exception as e:
        return {"msg": str(e)}, 500
    
@borrow_routes.route("/api/book/borrow/<string:id>", methods=['GET'])
@cross_origin()
def getBorrow(id):
    try:
        borrow = borrowCtrl.getBorrowByBookId(id)
        borrowObj = {}
        borrowObj["bookId"] = borrow[0]
        borrowObj["userId"] = borrow[1]
        borrowObj["book"] = borrow[2]
        borrowObj["user"] = borrow[3]
        
        return jsonify(borrowObj)
    except Exception as e:
        return {"msg": str(e)}, 500
    
@borrow_routes.route("/api/book/borrow/<string:id>", methods=['DELETE'])
@cross_origin()
def deleteBorrow(id):
    try:
        rows = borrowCtrl.deleteBorrow(id)
        if rows == 0:
            return {"msg": "Delete failed"}, 500
        return {"msg": "Successfully deleted"}, 200
    except Exception as e:
        return {"msg": str(e)}