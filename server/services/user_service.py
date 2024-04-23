from server.dao.base_dao import BaseDao

class UserService(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)
        
    def getUser(self, id):
        params = [id]
        return self.queryParam("SELECT * FROM User WHERE id = ?", params)
    
    def getUsers(self):
        return self.query("SELECT * FROM User")
    
    def saveUser(self, user):
        params = [user['name'], user['email'], user['cpf'], user['telephone']]
        return self.execute_dml("INSERT INTO User (name, email, cpf, telephone) VALUES (?, ?, ?, ?)", params)
    
    def updateUser(self, user):
        params = [user['name'], user['email'], user['cpf'], user['telephone'], user['id']]
        return self.execute_dml("UPDATE User SET name = ?, email = ?, cpf = ?, telephone = ? WHERE id = ?", params)
    
    def removeUser(self, id):
        params = [id]
        return self.execute_dml("DELETE FROM User WHERE id = ?", params)