class Dishes:

    name:str

    price:int

    quantity:str

    def __init__(self,name,price,quantity):

        self.name=name

        self.price=price

        self.quantity=str

    def __str__(self):

        return self.name

class Restuarant:

    name:str

    place:str

    dishes:list

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.dishes=[]


    def add_dishes(self,dishes):

        self.dishes.append(dishes)

    def list_dishes(self):

        for d in self.dishes:

            print(d)




biriyani_instance=Dishes("chicken biriyani",80,"full")
porotta_instance=Dishes("porotta",12,"large")
appam_instance=Dishes("appam",20,"full")
fried_rice_instance=Dishes("fried rice",120,"half")

restuarant_instance=Restuarant("caravans","kottakkal")

restuarant.instance.add_dishes()