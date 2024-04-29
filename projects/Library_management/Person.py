from Library import Library
class Person:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
    

        
class User(Person):
    
    def __init__(self, name, email, password) -> None:
        self.__is_login = False
        self.library = None
        self.pawna_books = []
        super().__init__(name, email, password)
        
    @property   
    def is_login(self):
        return self.__is_login
    

    @is_login.setter
    def is_login(self,bool_type):
        if bool_type=='True':
            self.__is_login = True
        else:
            self.__is_login = False
    
    def show_books(self):
        self.library.show_books()
    
    def borrow_books(self, books):
        if not self.__is_login:
            print('Sorry! You are not loggedin!')
            return
        else:
            for book in books:
                if self.library.book_quantity.get(book,0)==0:
                    print(f'Sorry!{book}-This book is not available')
                else:
                    self.pawna_books.append(book)
    
    def return_books(self,books):
        if not self.__is_login:
            print('Sorry! You are not loggedin!')
            return
        else:
            for book in books:
                self.pawna_books.remove(book)
        

class Admin(Person):
    def __init__(self, name, email, password) -> None:
        self.__is_login = False
        self.library = None
        super().__init__(name, email, password)
        
    def add_book(self, book_name, quantity):
        if self.is_login == True:
            self.library.add_book(book_name, quantity)
        else:
            print(f'Sorry!{book_name} is not added!You are not loggedin!')
            
            
    @property   
    def is_login(self):
        return self.__is_login
    

    @is_login.setter
    def is_login(self,bool_type):
        if bool_type=='True':
            self.__is_login = True
        else:
            self.__is_login = False
            
    def __repr__(self) -> str:
        print(self.name, self.email, self.password, self.is_login)
        return ''