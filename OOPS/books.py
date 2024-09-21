class Book:
    title:str

    author:str

    price:int

    language:str

    def __init__(self,title,author,price,language):
        
        self.title=title

        self.author=author

        self.price=price

        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price)

    def __str__(self):

        return self.title

#create object

book_instance1=Book("rainraising","nirupama",470,"hindi")

Book_instance2=Book("goatlife","benyamin",500,"malayalam")

#book_instance1.display_book()

print(book_instance1)   

#__str__() ===>> string represanation of object
