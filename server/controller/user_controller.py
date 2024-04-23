from server.services.user_service import UserService

class UserController(UserService):
    def __init__(self):
        UserService.__init__(self)
        
    def getUserById(self, id):
        return self.getUser(id)
    
    def getAllUsers(self):
        return self.getUsers()
    
    def postUser(self, name, email, cpf, telephone):
        user = {"name": name, "email": email, "cpf": cpf, "telephone": telephone}
        return self.saveUser(user)
    
    def putUser(self, id, name, email, cpf, telephone):
        user = {"id": id, "name": name, "email": email, "cpf": cpf, "telephone": telephone}
        return self.updateUser(user)
    
    def deleteUser(self, id):
        return self.removeUser(id)