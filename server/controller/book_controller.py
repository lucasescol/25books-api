from server.services.book_service import BookService

class BookController(BookService):
    def __init__(self):
        BookService.__init__(self)
        
    def searchBookByTitle(self, title):
        return self.getBookByTitle(title)
    
    def searchBookByAuthor(self, author):
        return self.getBookByAuthor(author)
        
    def getBookById(self, id):
        return self.getBook(id)
    
    def getAllBooks(self):
        return self.getBooks()
    
    def postBook(self, title, author, company, release, isEbook, location, borrowed):
        book = {"title": title, "author": author, "company": company, "release": release, "isEbook": isEbook, "location": location, "borrowed": borrowed}
        return self.saveBook(book)
    
    def putBook(self, id, title, author, company, release, isEbook, location, borrowed):
        book = {"id": id, "title": title, "author": author, "company": company, "release": release, "isEbook": isEbook, "location": location, "borrowed": borrowed}
        return self.updateBook(book)
    
    def deleteBook(self, id):
        book = self.getBookById(id)
        book = list(book)
        if book[7] == 0:
            return self.removeBook(id)
        return 0
        