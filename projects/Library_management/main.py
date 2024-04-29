from Library import Library
from Person import Admin,User

def main():
    biddan = Library('biddan')
    neam = Admin('neam','neam@334','123')
    biddan.create_new_account(neam,'admin')
    print(neam)
    neam.add_book('manus', 3)
    neam.add_book('manus', 2)
    biddan.logout(neam)
    neam.add_book('arshinogor', 3)
    
    biddan.login(neam,'admin')
    neam.add_book('nirbashon', 3)
    
    rakibul = User('rakibul','rakibul@33',456)
    
    rakibul.borrow_books(['opekkha','manus'])
    biddan.login(rakibul,'user')
    biddan.create_new_account(rakibul,'user')
    rakibul.borrow_books(['opekkha','manus'])
    print(rakibul.pawna_books)
    rakibul.return_books(['manus'])
    print(rakibul.pawna_books)
    rakibul.show_books()
    biddan.logout(rakibul)
    rakibul.show_books()
    #print(biddan)

if __name__ == '__main__':
    main()