#inheritance  (child inheritance from parent)
#polymorphism (more than one form)
   
     #method overloading(*args==tuple),(**kwargs ====dictionary)

     #method overriding (same method signature from parent) 

#Abstraction
from abc import ABC,abstractmethod

class car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Swift(car):

    def start(self):
        print("swift start method")

    def accelarate(self):
        print("swift accelarate method")

    def stop(self):
        print("swift stop method")

car_instance=Swift()

car_instance.start()