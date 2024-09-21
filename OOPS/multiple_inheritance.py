class Grandparents:

    def m1(self):

        print("grand parent class m1 method")





class Parent():

    def m2(self):

        print("parent class m2 method")


class Child(Parent,Grandparents):

    def m2(self):

        print("parent class m2 method")


child_instance=Child()

child_instance.m3()
child_instance.m2()
child_instance.m1()
