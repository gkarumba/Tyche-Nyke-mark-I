import os 
import psycopg2
from psycopg2.extras import RealDictCursor
#local import 
from instance.config import config

env = os.getenv('FLASK_ENV')
url = config[env].DATABASE_URL

class BooksDB():
    """
    Class for methods to handle databse queries 
    """
    def __init__(self):
        """
        Method for initializing the class BooksDB
        """
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_tables(self):
        """
        Method for creating tables in the database
        """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS books(
                id SERIAL PRIMARY KEY,
                book_name varchar(42) NOT NULL,
                author varchar(42) NOT NULL,
                category varchar(42) NOT NULL,
                status varchar(42) default 'Available'
                );""",
            """CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                username varchar(42) NOT NULL,
                email varchar(42) NOT NULL,
                role varchar(42) NOT NULL,
                password varchar(42) NOT NULL,
                books_borrowed INT REFERENCES books(id)
            );""")
        self.conn.commit()

    def create_borrow_table(self):
        """
        Method to create the borrow table
        """
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS borrow(
                book_id INT,
                user_id INT ,
                date_borrowed VARCHAR(100) default current_timestamp,
                date_return VARCHAR(42),
                status VARCHAR(42)
            );"""
        )

    def drop_tables(self):
        """
        Method for dropping the tables after running tests
        """
        queries = (
            """DROP TABLE IF EXISTS books CASCADE;""",
            """DROP TABLES IF EXISTS users CASACADE;"""
        )
        for q in queries:
            self.cur.execute(q)
            self.conn.commit()

    def add_book(self,query_string,tuple_data):
        """
        Method for adding to the database
        """
        self.cur.execute(query_string,tuple_data)
        self.conn.commit()
        # response = self.cur.fetchone()
        # return response

    def get_all(self,query):
        """
        Method for retrieving all the books
        """
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def get_one(self,query):
        """
        Method for retrieving a single book
        """
        self.cur.execute(query)
        return self.cur.fetchone()

    def edit_book(self,query):
        """
        Method for editing a book
        """
        self.cur.execute(query)
        self.conn.commit()

    def borrow_book(self,query,tuple_data):
        """
        Method for borrowing a book
        """
        self.cur.execute(query,tuple_data)
        self.conn.commit()

    def return_book(self,query):
        """
        Method for returning a book
        """
        self.cur.execute(query)
        self.conn.commit()

    def unreturned_book(self,query):
        """
        Method for retrieving unreturned books
        """
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def delete_book(self,query):
        """
        Method for deleting a book
        """
        self.cur.execute(query)
        self.conn.commit()

    
