from werkzeug.security import generate_password_hash,check_password_hash
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
        hash_password = generate_password_hash(password)
        db.create_users_table()
        query = """INSERT INTO users(email,password,username) VALUES (%s,%s,%s);"""
        tuple_data = (email,hash_password,username)
        db.add_user(query,tuple_data)
        query2 = """SELECT id FROM users WHERE id = (select max(id) from users);"""
        result = db.get_one(query2)
        return result
    
    def set_role(self,user_id):
        """
        Method for creating Admin role
        """
        role = 'Admin'
        ID = 1
        query = """SELECT id FROM users WHERE id = 1;"""
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
        db.create_users_table()
        query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        response = db.get_one(query)
        return response

    def validate_password(self,email,password):
        """
        Method to validate the hash_password
        """
        query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        response = db.get_one(query)
        if response:
            if check_password_hash(response['password'],password):
                return True
            return False

    def get_unreturned_books(self,user_id):
        """
        Method to retrieve all books not returned by user
        """
        status = 'Unavailable'
        check_query = """SELECT * FROM borrow WHERE user_id = '{}' AND status = '{}'""".format(user_id,status)
        response = db.get_all(check_query)
        # print(response)
        return response

    def get_borrowing_history(self,user_id):
        """
        Method to retrieve the borrowing history of a user
        """
        check_query = """SELECT * FROM borrow WHERE user_id = '{}' """.format(user_id)
        response = db.get_all(check_query)
        # print(response)
        return response

    def check_role(self,user_id):
        """
        Method for checking user role
        """
        check_query = """SELECT role FROM users WHERE id = '{}'""".format(user_id)
        response = db.get_one(check_query)
        # print(response)
        for key,value in response.items():
            if value == 'Admin':
                return True
            return False