from server.dao.base_dao import BaseDao

class BookService(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)
        
    def getBookByTitle(self, title):
        params = [f'%{title}%']
        return self.queryParams("SELECT * FROM Book WHERE title LIKE ?", params)
    
    def getBookByAuthor(self, author):
        params = [f'%{author}%']
        return self.queryParams("SELECT * FROM Book WHERE author LIKE ?", params)
        
    def getBook(self, id):
        params = [id]
        return self.queryParam("SELECT * FROM Book WHERE id = ?", params)
    
    def getBooks(self):
        return self.query("SELECT * FROM Book")
    
    def saveBook(self, book):
        params = [book['title'], book['author'], book['company'], book['release'], book ['isEbook'], book['location'], book['borrowed']]
        return self.execute_dml("INSERT INTO Book (title, author, company, release, isEbook, location, borrowed) VALUES (?, ?, ?, ?, ?, ?, ?)", params)
    
    def updateBook(self, book):
        params = [book['title'], book['author'], book['company'], book['release'], book['isEbook'], book['location'], book['borrowed'], book['id']]
        return self.execute_dml("UPDATE Book SET title = ?, author = ?, company = ?, release = ?, isEbook = ?, location = ?, borrowed = ? WHERE id = ?", params)
    
    def removeBook(self, id):
        params = [id]
        return self.execute_dml("DELETE FROM Book WHERE id = ?", params)
    