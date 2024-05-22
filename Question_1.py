#Task 1
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.status = True

    def change_title(self, new_title):
        self.title = new_title
        
    def change_author(self, new_author):
        self.author = new_author
    
    def change_price(self, new_price):
        self.price = new_price

    def change_status(self):
        self.status = False if True else self.status == True

    def display_book(self):
        if self.status:
            self.status = 'Yes'
        else:
            self.status = 'No'
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}\nIn Stock: {self.status}")



book1 = Book('Red Rising', 'Pierce Brown', 25.99)

book1.display_book()
    #Output: 
    #Title: Red Rising
    #Author: Pierce Brown
    #Price: 25.99
    #In Stock: Yes

book1.change_title('Fellowship of the Ring')
book1.change_author('JRR Tolkien')
book1.change_price(30.99)
book1.change_status()

book1.display_book()
    #Output:
    # Title: Fellowship of the Ring
    # Author: JRR Tolkien
    # Price: 30.99
    # In Stock: No