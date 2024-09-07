class student:                                            #class

    name:str

    age:int

    eid:int

    gender:str

    mark:int

    department:str

    def set_student(self,name,age,id,gender,mark,dept):      #initialise    ,atributes(self.name,...)

        self.name=name

        self.age=age

        self.id=id

        self.gender=gender

        self.mark=mark

        self.department=dept

    def display_student(self):                                 #for display

        print(self.id,self.name)

#create object (create out of class)
student_instance=student()

student_instance.set_student("murshi",21,101,"female",50,"address line 1")

student_instance.display_student()