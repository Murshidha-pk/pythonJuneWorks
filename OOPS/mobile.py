class Mobile:

    name:str

    brand:str

    storage:int

    price:int

#instance variable   eg:(self.name...)
#initialise instance variable =>constructor
#constructor is unique name
#java=>class name()
#java script=>constructor()
#python=>__init__()

    def __init__(self,name,brand,storage,price):

        self.name=name

        self.brand=brand

        self.storage=storage

        self.price=price

    def display_details(self):

        print(self.name,self.price)

    def __str__(self):
        
        return self.name

#object creation
#reference_name=ClassName()

# mobile_instance=Mobile()

# mobile_instance2=Mobile()

# mobile_instance2.set_mobile("iphone 11","iphone","125GB",50000)

# mobile_instance2.display_details()

######## use====>>> __init__ (constructor)######
# call automatically

mobile_instance=Mobile("i phone ","iphone","125GB",50000)

print(mobile_instance)


