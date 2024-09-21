class Student:                                            #class

    name:str

    age:int

    eid:int

    gender:str

    mark:int

    department:str

    def __init__(self,name,age,id,gender,mark,dept):      #initialise    ,atributes(self.name,...)

        self.name=name

        self.age=age

        self.id=id

        self.gender=gender

        self.mark=mark

        self.department=dept

    def display_student(self):                                 #for display

        print(self.name,self.age)

    def __str__(self):

        return self.name  

#create object (create out of class)
student_instance=Student("murshi",21,101,"female",50,"address line 1")

print(student_instance)

