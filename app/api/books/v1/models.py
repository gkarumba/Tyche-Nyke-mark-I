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
        check_book = self.is_added(title)
        if check_book ==  True:
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
