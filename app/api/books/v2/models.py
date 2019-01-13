import datetime 
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
        db.create_tables()
        query = """INSERT INTO books(book_name,author,category) VALUES (%s,%s,%s);"""
        tuple_data = (book_name,author,category)
        db.add_book(query,tuple_data)
        query2 = """SELECT id FROM books WHERE id = (select max(id) from books);"""
        result = db.get_one(query2)
        return result

    def check_book(self,title):
        """
        Method for checking if a book already exists
        """
        query = """SELECT book_name FROM books WHERE book_name='{}'""".format(title)
        response = db.get_one(query)
        # print(response)
        if not response:
            return False
        return True

    def get_all_books(self):
        """
        Method to retrieve all the books
        """
        query = """SELECT * FROM books """
        response = db.get_all(query)
        return response

    def get_one_book(self,id):
        """
        Method for getting one book
        """
        query = """SELECT * FROM books WHERE id = '{}'""".format(id)
        response = db.get_one(query)
        return response
    
    def edit_book_title(self,title,id):
        """
        Method for editing the book title
        """
        check_query = """SELECT book_name FROM books WHERE id = '{}'""".format(id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        query = """UPDATE books SET book_name = '{}' WHERE id = '{}'""".format(title,id)
        db.edit_book(query)
        get_query = """SELECT * FROM books WHERE id = '{}'""".format(id)
        response = db.get_one(get_query)
        return response

    def edit_book_author(self,author,id):
        """
        Method for editing the book author
        """
        check_query = """SELECT author FROM books WHERE id = '{}'""".format(id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        query = """UPDATE books SET author = '{}' WHERE id = '{}'""".format(author,id)
        db.edit_book(query)
        get_query = """SELECT * FROM books WHERE id = '{}'""".format(id)
        response = db.get_one(get_query)
        return response

    def edit_book_category(self,category,id):
        """
        Method for editing the book category
        """
        check_query = """SELECT category FROM books WHERE id = '{}'""".format(id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        query = """UPDATE books SET category = '{}' WHERE id = '{}'""".format(category,id)
        db.edit_book(query)
        get_query = """SELECT * FROM books WHERE id = '{}'""".format(id)
        response = db.get_one(get_query)
        return response

    def check_status(self,book_id):
        """
        Method for checking book status
        """
        check_query = """SELECT status FROM books WHERE id = '{}'""".format(book_id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        for key,value in check_response.items():
            if value == 'Unavailable':
                return False
            else:
                return True
        
    def borrow_book(self,status,book_id):
        """
        Method to borrow book
        """
        db.create_borrow_table()
        check_query = """SELECT book_name FROM books WHERE id = '{}'""".format(book_id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        if status == 'borrow':
            status = 'Unavailable'
        date_return = datetime.datetime.now() + datetime.timedelta(days=7)
        query = """INSERT INTO borrow (book_id,status,date_return) VALUES(%s,%s,%s);"""
        tuple_data = (book_id,status,date_return)
        db.borrow_book(query,tuple_data)
        query = """UPDATE books SET status = '{}' WHERE id = '{}'""".format(status,book_id)
        db.edit_book(query)
        query = """UPDATE borrow SET status = '{}' WHERE book_id = '{}'""".format(status,book_id)
        db.edit_book(query)
        get_query = """ SELECT * FROM borrow WHERE book_id = '{}'""".format(book_id)
        response = db.get_one(get_query)
        return response

    def return_book(self,status,book_id):
        """
        Method to return a borrowed book
        """
        check_query = """SELECT book_name FROM books WHERE id = '{}'""".format(book_id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        if status == 'return':
            status = 'Available'
        query = """ UPDATE books SET status = '{}' WHERE id  = '{}'""".format(status,book_id)
        db.return_book(query)
        query2 = """ UPDATE borrow SET status = '{}' WHERE book_id  = '{}'""".format(status,book_id)
        db.return_book(query2)
        get_query = """ SELECT * FROM books WHERE id = '{}'""".format(book_id)
        response = db.get_one(get_query)
        return response

    def delete_book(self,book_id):
        """
        Method to remove a book
        """
        check_query = """SELECT book_name FROM books WHERE id = '{}'""".format(book_id)
        check_response = db.get_one(check_query)
        if not check_response:
            return False
        query = """ DELETE FROM books where id = '{}'""".format(book_id)
        db.delete_book(query)
