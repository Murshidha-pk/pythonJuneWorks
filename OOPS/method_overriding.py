
class parent:

    def bike(self):

        print("bullet")

    def mobile(self):

        print("samsung")

class child(parent):

    def bike(self):

        print("hunter")

    def mobile(self):

        print("i phone")

child_instance=child()

child_instance.bike()

child_instance.mobile()