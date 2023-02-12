class Grandparent:
    def about(self):
        print("I am Grandparent")
    def about_myself(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def about_myself(self):
        print("i am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()

