#local imports
from app.database.database import BooksDB

db = BooksDB()

class BooksModel():
    """
    Class for the query methods
    """
    # def __init__(self,book_name,author,category):
    #     """
    #     Method for instatiating the class BooksModel
    #     """
    #     self.book_name = book_name
    #     self.author = author
    #     self.category = category

    def add_book(self,book_name,author,category):
        """
        Method of adding a book
        """
        payload = {
            "book_name":book_name,
            "author":author,
            "category":category
        }
        create_db = db.create_tables()
        query = """INSERT INTO books(book_name,author,category) VALUES (%s,%s,%s);"""
        tuple_data = (book_name,author,category)
        response = db.add_book(query,tuple_data)
        query2 = """SELECT id FROM books WHERE id = (select max(id) from books);"""
        result = db.get_one(query2)
        # print(result)
        return result

    def check_book(self,title):
        """
        Method for checking if a book already exists
        """
        payload = {
            'title':title
        }
        query = """SELECT book_name FROM books WHERE book_name='{}'""".format(title)
        response = db.get_one(query)
        # print(response)
        if not response:
            return False
        return True