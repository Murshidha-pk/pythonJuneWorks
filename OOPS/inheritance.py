


class Vehicle:

    name:str

    brand:str

    def __init__(self,name,brand):

        self.name=name

        self.brand=brand

    def start(self):

        print(f"{self.name} vehicle start method")

    def accelerate(self):

        print(f"{self.name} vehicle accelerate method")

class Swift(Vehicle):

    def __init__(self, name, brand):
        super().__init__(name, brand)         #refer parent classs(super)

    
#object

Swift_instance=Swift("swift","maruthi")

Swift_instance.accelerate()

Swift_instance.start()