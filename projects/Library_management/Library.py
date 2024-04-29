
class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.book_quantity = {}
        self.users = []
        self.admins = []

    
    def create_new_account(self, person, cna_type):
            person.library = self
            person.is_login = 'True'
            if cna_type == 'user':
                self.users.append(person)
            else:
                self.admins.append(person)
    
    def login(self, person , login_type):
        ok=False
        if login_type == 'admin':
            for admin in self.admins:
                if admin.email==person.email and admin.password== person.password:
                    person.is_login = 'True'
                    print('Welcome Admin!')
                    ok = True
            if not ok:
                print('Sorry! login Failed')
        elif login_type == 'user':
            for user in self.users:
                if user.email==person.email and user.password== person.password:
                    person.is_login = 'True'
                    print('Welcome Sir!')
                    ok =True
            if not ok:
                print('Sorry! login Failed')
                
    def logout(self, person):
        person.is_login = 'False'
                
    def add_book(self, book_name, quantity):
        print(f'{book_name} added successfully')
        if book_name in self.book_quantity:
            self.book_quantity[book_name] += quantity
        else:
            self.book_quantity[book_name] = quantity
            
    
    def show_books(self):
        print(f'--------Our Available Books-------') 
        print(f'-Book Name-- --Quantity--')
        print(self.book_quantity)
            
    
    
    def __repr__(self) -> str:
        print(f'########Welcome to our {self.name} Library########')
        self.show_books()
        print(f'--Our Valuable Admins--')
        for admin in self.admins:
            print(admin.name, admin.email)
        print(f'--Our Valuable Customers--')
        for customer in self.users:
            print(customer.name, customer.email)
        return ' '
        