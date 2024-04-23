from server.controller.book_controller import BookController
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

book_routes = Blueprint("book", __name__)
bookCtrl = BookController()

@book_routes.route("/api/book/search", methods=['POST'])
@cross_origin()
def searchBookTitle():
    try:
        if request.json and 'title' in request.json:
            title = request.json["title"]
            books = bookCtrl.searchBookByTitle(title)
            bookList = []
            if books != None:
                for book in books:
                    bookObj = {}
                    bookObj["id"] = book[0]
                    bookObj["isEbook"] = book[1]
                    bookObj["company"] = book[2]
                    bookObj["release"] = book[3]
                    bookObj["author"] = book[4]
                    bookObj["title"] = book[5]
                    bookObj["location"] = book[6]
                    bookObj["borrowed"] = book[7]
                    bookList.append(bookObj)
                return {"search": bookList}, 200
            else:
                return {"msg": "Book not found"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500

@book_routes.route("/api/book/search", methods=['PUT'])
@cross_origin()
def searchBookAuthor():
    try:
        if request.json and 'author' in request.json:
            author = request.json["author"]
            books = bookCtrl.searchBookByAuthor(author)
            bookList = []
            if books != None:
                for book in books:
                    bookObj = {}
                    bookObj["id"] = book[0]
                    bookObj["isEbook"] = book[1]
                    bookObj["company"] = book[2]
                    bookObj["release"] = book[3]
                    bookObj["author"] = book[4]
                    bookObj["title"] = book[5]
                    bookObj["location"] = book[6]
                    bookObj["borrowed"] = book[7]
                    bookList.append(bookObj)
                return {"search": bookList}, 200
            else:
                return {"msg": "Book not found"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500

@book_routes.route("/api/book/<string:id>", endpoint="get-book", methods=['GET'])
@cross_origin()
def getBook(id):
    try:
        book = bookCtrl.getBookById(id)
        if book != None:
            bookObj = {}
            bookObj["id"] = book[0]
            bookObj["isEbook"] = book[1]
            bookObj["company"] = book[2]
            bookObj["release"] = book[3]
            bookObj["author"] = book[4]
            bookObj["title"] = book[5]
            bookObj["location"] = book[6]
            bookObj["borrowed"] = book[7]
            return jsonify(bookObj)
        else:
            return {"msg": "Book not found"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
    
@book_routes.route("/api/book", endpoint="get-all-books", methods=['GET'])
@cross_origin()
def getBooks():
    try:
        books = bookCtrl.getAllBooks()
        bookList = []
        if len(books) > 0:
            for book in books:
                bookObj = {}
                bookObj["id"] = book[0]
                bookObj["isEbook"] = book[1]
                bookObj["company"] = book[2]
                bookObj["release"] = book[3]
                bookObj["author"] = book[4]
                bookObj["title"] = book[5]
                bookObj["location"] = book[6]
                bookObj["borrowed"] = book[7]
                bookList.append(bookObj)
        return jsonify(bookList)
    except Exception as e:
        return {"msg": str(e)}, 500
    
@book_routes.route("/api/book", endpoint="post-book", methods=['POST'])
@cross_origin()
def saveBook():
    try:
        if request.json and 'book' in request.json:
            book = request.json['book']
            bookCtrl.postBook(book['title'], book['author'], book['company'], book['release'], book['isEbook'], book['location'], book['borrowed'])
            return {"msg": "Book successfully saved"}, 200
        else:
            return {"msg": "Book is empty"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
     
@book_routes.route("/api/book", endpoint="update-book", methods=['PUT'])
@cross_origin()
def updateBook():
    try:
        if request.json and 'book' in request.json:
            book = request.json['book']
            rows = bookCtrl.putBook(book["id"], book['title'], book['author'], book['company'], book['release'], book['isEbook'], book['location'], book['borrowed'])
            if rows == 0:
                return {"message": "Update failed"}, 500
            return {"msg": "Book successfully updated"}, 200
        else:
            return {"msg": "Book is empty"}, 500
    except Exception as e:
        return {"msg": str(e)}, 500
    
@book_routes.route("/api/book/<string:id>", endpoint="remove-book", methods=['DELETE'])
@cross_origin()
def removeBook(id):
    try:
        rows = bookCtrl.deleteBook(id)
        if rows == 0:
            return {"msg": "Delete failed"}, 200
        return {"msg": "Book successfully deleted"}, 200
    except Exception as e:
        return {"msg": str(e)}
    
    
