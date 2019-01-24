
#local imports
from app.database.database import BooksDB

db = BooksDB()

class UsersModel():
    """
    Class for the query methods
    """
    def add_user(self,email,password,username):
        """
        Method of adding a user
        """
        db.create_tables()
        
        query = """INSERT INTO users(email,password,username) VALUES (%s,%s,%s);"""
        tuple_data = (email,password,username)
        db.add_user(query,tuple_data)
        query2 = """SELECT id FROM users WHERE id = (select max(id) from users);"""
        result = db.get_one(query2)
        return result
    
    def set_role(self,user_id):
        """
        Method for creating Admin role
        """
        role = 'Admin'
        ID = 4
        query = """SELECT id FROM users WHERE id = 4;"""
        result  = db.get_one(query)
        if result:
            query2 = """UPDATE users SET role = '{}' WHERE id = '{}'""".format(role,ID)
            db.update_role(query2)
            query3 = """ SELECT * FROM users WHERE id = '{}'""".format(ID)
            response = db.get_one(query3)
            return response


    def get_user_id(self,user_id):
        """
        Method for retrieving user_id
        """
        query = """SELECT * FROM users WHERE id = '{}'""".format(user_id)
        response = db.get_one(query)
        return response
    
    def check_email(self,email):
        """
        Method for checking email
        """
        query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        response = db.get_one(query)
        return response

