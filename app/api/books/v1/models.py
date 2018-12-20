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
            for pos in self.db:
                return pos
            
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
        if len(books_list) > 0:
            for pos,book in enumerate(books_list):
                if id == book['id']:
                    updated_book = book.update(payload)
                    self.db[pos] == updated_book
                    return book['id']
        return False
    
    def borrow_book(self,id):
        """
            Method for allowing user to borrow book
        """
        payload = {
            'status':'Unavailable'
        }
        for pos,book in enumerate(books_list):
            if id == book['id']:
                updated_book = book.update(payload)
                self.db[pos] == updated_book
                return book

    def return_book(self,id):
        """
            Method of allowing user to return borrowed books
        """
        payload = {
            'status':'Available' 
        }
        for pos,book in enumerate(books_list):
            if id == book['id']:
                updated_book = book.update(payload)
                self.db[pos] == updated_book
                return book

    def get_unreturned(self):
        """
            Method for getting unreturned books
        """
        unreturned = []
        for pos in self.db:
            if pos['status'] == 'Unavailable':
                response = unreturned.append(pos)
        return unreturned
