from server.services.borrow_service import BorrowService
from server.services.book_service import BookService

class BorrowController(BorrowService, BookService):
    def __init__(self):
        BorrowService.__init__(self)
    
    def borrowBook(self, userId, bookId):
        if self.isBorrowed(bookId): 
            return 0
        affected = self.saveBorrow(userId, bookId)
        self.plusBorrowed(bookId)
        return affected
    
    def getBorrowByBookId(self, bookId):
        return self.getBorrow(bookId)

    def getAllBorrows(self):
        return self.getBorrows()
        
    def deleteBorrow(self, bookId):
        return self.removeBorrow(bookId)
    
    def plusBorrowed(self, bookId):
        book = list(self.getBook(bookId))
        brr = book[7] + 1
        book[7] = brr
        bookObj = {}
        bookObj["id"] = book[0]
        bookObj["isEbook"] = book[1]
        bookObj["company"] = book[2]
        bookObj["release"] = book[3]
        bookObj["author"] = book[4]
        bookObj["title"] = book[5]
        bookObj["location"] = book[6]
        bookObj["borrowed"] = book[7]
        self.updateBook(bookObj)