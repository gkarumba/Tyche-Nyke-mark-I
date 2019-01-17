import re,string
# from string import maketrans

def check_space(mystring):
    """
        Function for validating whitespaces/blanks
    """
    if mystring and mystring.strip():
        return True
    else:
        return False

def check_words(mystring):
    """
        Function for validating words
    """
    if not re.search(r'([A-Za-z] ?)+[A-Za-z]', mystring):
        return False
    else: 
        return True

def check_borrow(mystring):
    """
        Function for validating the status type
    """
    status = r'\b' + 'borrow' + r'\b'
    if re.findall(status,mystring) :
        return True
    else:
        return False

def check_return(mystring):
    """
        Method for checking the return book value
    """
    status = r'\b' + 'return' + r'\b' 
    if re.findall(status,mystring):
        return True
    else:
        return False

def check_email(mystring):
    """
    Method for checking the user's email
    """
    EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if not EMAIL_REGEX.match(mystring):
        return False
    else:
        return True

def check_password(mystring):
    """
    Method for checking the user's password
    """
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', mystring):
        return True
    else:
        return False
    