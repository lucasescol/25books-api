from server.config import config
import sqlite3

class BaseDao:
    def connect(self):
        self.conn = sqlite3.connect(config.DATABASE_NAME)
        self.cursor = self.conn.cursor()
    
    def disconnect(self):
        self.cursor.close()
        self.conn.close()
        
    def queryParam(self, query, params):
        self.connect()
        self.cursor.execute(query, (params))
        result = self.cursor.fetchone()
        self.disconnect()
        return result
    
    def queryParams(self, query, params):
        self.connect()
        self.cursor.execute(query, (params))
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    def query(self, query):
        self.connect()
        self.cursor.execute(query)
        list = self.cursor.fetchall()
        self.disconnect()
        return list
    
    def execute_dml(self, dml_command, params):
        self.connect()
        response = self.cursor.execute(dml_command, (params))
        affected_rows = response.rowcount
        self.conn.commit()
        self.disconnect()
        return affected_rows