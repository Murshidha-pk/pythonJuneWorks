class Person:

    name:str

    age:int

    gender:str

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):
         
        print(self.name,self.age,self.gender)

class Employee(Person):
        
        eid:int

        dept:str

        salary:int
        
        def __init__(self,name,age,gender,eid,dept,salary):
             
             super().__init__(name,age,gender)        #refer parent class

             self.eid=eid

             self.dept=dept

             self.salary=salary

        def display(self):                            #self===disply current instance
             
             super().display()                        #refer from parent

             print(self.eid,self.dept,self.salary)

emp_instance=Employee("vipin",34,"male","e01","hr",12000)

emp_instance.display()




#constructor  ===initialise instance variables

#__init__ ()=======python===automatically invok ==object call

#__str__() ======string representation for object craeation

# inheritance

   #single   
   # multiple
   # multilevel      

# polymorphism
   #many forms

   # 1.method overloading(same method name,diff no of arguments)
   # 2.method overriding