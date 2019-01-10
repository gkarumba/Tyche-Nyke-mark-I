from datetime import datetime

books_list = []
"""
    List for storing the books added
"""

class BooksModel():
    """
        Class for the books endpoints
    """
    def __init__(self):
        """
            Constructor method for the class BooksModel
        """
        self.db = books_list

    def add_book(self,title,author,category):
        """
            Method for serializing the data of a book
        """
        status = 'Available'
        payload = {
            'status' : status,
            'title' : title,
            'author' : author,
            'category' : category,
            'id' : len(books_list) + 1,
            'added_on'  : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        } 
        check_title = self.is_added(title)
        if check_title == True:
            return 'Book already exists'
        else:
            self.db.append(payload)
            return self.db
            
    def is_added(self,title):
        """
            Method for checking if a book is already in the library
        """
        for book in books_list:
            if title == book['title']:
                return True
            else:
                return False

    def get_all(self):
        """
            Method for retrieving all the books
        """
        return books_list

    def get_one(self,id):
        """
            Method for retrieving one book
        """
        for book in books_list:
            if id == book['id']:
                return book
    
    def edit_book(self,id,author,title,category):
        """
            Method for editing a book's details 
        """
        payload = {
            'title' : title,
            'author' : author,
            'category' : category
        }
        for pos,book in enumerate(books_list):
            if id == book['id']:
                updated_book = book.update(payload)
                self.db[pos] == updated_book
                return self.db[id]
    
    def borrow_book(self,id,status):
        """
            Method for allowing user to borrow book
        """
        payload = {
            'status':status
        }
        for pos,book in enumerate(books_list):
            if id == book['id']:
                updated_book = book.update(payload)
                self.db[pos] == updated_book
                return self.db[id]

    def return_book(self,id,status):
        """
            Method of allowing user to return borrowed books
        """
        payload = {
            'status':status
        }
        for book in books_list:
            if id == book['id']:
                book.update(payload)
                self.db.append(book)
                return self.db[id]

    def get_unreturned(self):
        """
            Method for getting unreturned books
        """
        unreturned = []
        for book in books_list:
            if book['status'] == 'Borrowed':
                unreturned.append(book)
                return unreturned

