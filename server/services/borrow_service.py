from server.dao.base_dao import BaseDao

class BorrowService(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)
    
    def saveBorrow(self, userId, bookId):
        params = [userId, bookId]
        return self.execute_dml("INSERT INTO borrow (fk_User_id, fk_Book_id) VALUES (?, ?)", params)
    
    def getBorrows(self):
        return self.query("SELECT Br.fk_Book_id, Br.fk_User_id, Bk.title, U.name FROM borrow AS Br INNER JOIN Book AS Bk ON Br.fk_Book_id = Bk.id INNER JOIN User AS U ON Br.fk_User_id = U.id;")
    
    def getBorrow(self, bookId):
        params = [bookId]
        return self.queryParam("SELECT Br.fk_Book_id, Br.fk_User_id, Bk.title, U.name FROM borrow AS Br INNER JOIN Book AS Bk ON Br.fk_Book_id = Bk.id INNER JOIN User AS U ON Br.fk_User_id = U.id WHERE fk_Book_id = ?", params)
    
    def isBorrowed(self, bookId):
        params = [bookId]
        result = self.queryParam("SELECT COUNT(*) FROM borrow WHERE fk_Book_id = ?", params)
        res = list(result)
        return res[0] == 1
    
    def removeBorrow(self, bookId):
        params = [bookId]
        return self.execute_dml("DELETE FROM borrow WHERE fk_Book_id = ?", params)