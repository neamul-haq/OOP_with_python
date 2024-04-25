class Eshop:
    def __init__(self, name) -> None:
        self.name = name
        self.customers = []
        self.sellers =  []
        self.product_price = {}
        self.product_quantity = {}
        print('##########WELCOME TO OUR SHOP#########')
        self.home_page()
        
    
    def home_page(self):
        print('##WELCOME TO HOME PAGE')
        print('Press 1 TO Signup')
        print('OR')
        print('Press 2 TO Login')
        print('OR')
        print('Press 3 TO Exit')
        self.show_sellers()
        self.show_customers()
        press = int(input())
        if press == 1:
            self.signup()
        elif press == 2:
            self.login()
        else:
            print('Thanks for Coming')
            
    def signup(self):
        print('##Welcome TO Signup form##')
        print('**press 1 to signup as Seller**')
        print('**press 2 to signup as Custome**')
        signup_press = int(input())
        if signup_press == 1:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            seller = Person(email,password)
            self.sellers.append(seller)
            print('-- Welcome Mr. Seller --')
            print('**press 1 to Add product**')
            print('**press 2 to Exit**')
            seller_press = int(input())
            if seller_press == 1:
                self.add_product()
            else:
                self.home_page()
            
        else:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            customer = Person(email,password)
            self.customers.append(customer)
            print('-- Welcome Mr. Customer --')
            print('** Press 1 to show products')
            print('** Press 2 to buy products')
            print('** Press 3 to home page')
            customer_press = int(input())
            if customer_press == 1:
                self.show_products()
            elif customer_press == 3:
                self.home_page()
            else:
                self.buy_products()
            
    def login(self):
        print('##Welcome TO Login form##')
        print('**press 1 to Login as Seller**')
        print('**press 2 to Login as Customer**')
        login_press = int(input())
        if login_press == 1:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            seller = Person(email,password)
            for seller in self.sellers:
                if seller.email == email and seller.password == password:
                    print('-- Welcome Mr. Seller --')
                    print('**press 1 to Add product**')
                    print('**press 2 to Exit**')
                    seller_press = int(input())
                    if seller_press == 1:
                        self.add_product()
                    else:
                        self.home_page()
            else:
                print('Sorry,You are not registered! Please Signup')
                self.home_page()
                
        else:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            customer = Person(email,password)
            for customer in self.customers:
                if customer.email == email and customer.password == password:
                    print('-- Welcome Mr. Customer --')
                    print('** Press 1 to show products')
                    print('** Press 2 to buy products')
                    print('** Press 3 to home page')
                    customer_press = int(input())
                    if customer_press == 1:
                        self.show_products()
                    elif customer_press == 3:
                        self.home_page()
                    else:
                        self.buy_products()
            else:
                print('Sorry,You are not registered! Please Signup')
                self.home_page()
            
    def add_product(self):
        product_name = input('Enter product name: ')
        product_price = int(input('Enter product price: '))
        product_quantity = int(input('Enter product quantity: '))
        self.product = Product(product_name, product_price, product_quantity)
        self.product_price[product_name] = product_price
        self.product_quantity[product_name] = product_quantity
        print('**press 1 to Add More**')
        print('**press 2 to Exit**')
        prod_press = int(input())
        if prod_press == 1:
            self.add_product()
        else:
            self.home_page()
            
    def show_products(self):
        print('---------Our Products------')
        print(' --- Name --- Price --- Quantity ')
        for key in self.product_price:
            print(f' --- {key} --- {self.product_price[key]} --- {self.product_quantity[key]}')
            
        print('press 1 To buy')
        print('press 2 To Exit')
        press = int(input())
        if press == 1:
            self.buy_products()
        else:
            self.home_page()
            
    def buy_products(self):
        cart = []
        while(True):
            product = input('Enter product name: ')
            cart.append(product)
            print('press 1 to add more products')
            print('OR')
            print('press 2 to end')
            press = int(input())
            if press == 2:
                break
        bill = 0
        for item in cart:
            if self.product_quantity.get(item,0)==0:
                print(f'Sorry! {item} is not available')
            else:
                bill = bill + self.product_price[item]
                self.product_quantity[item] -= 1
                if self.product_quantity[item] == 0:
                    self.product_price.pop(item)
                    self.product_quantity.pop(item)
        print(f'Your Total Bill is {bill} ! Thanks For shopping!')
        self.home_page()
        
    def show_sellers(self):
        for seller in self.sellers:
            print(f'seller name: {seller.email}  pass: {seller.password}')
        
    def show_customers(self):
        for cus in self.customers:
            print(f'customer name: {cus.email} pass: {cus.password}')
            
            
        
        
class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
        
class Person:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password