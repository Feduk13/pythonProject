class Grandparent:
    def about(self):
        print("I am Grandparent")
    def about_myself(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def about_myself(self):
        print("we Parent")
class Child(Parent):
    def about_myself(self):
        print("i am Child")

class Friend(Child):
    def about_myself(self):
        print("i am a friend Child")
class girlfriend(Child):
    def about_myself(self):
        print("i am a girlfriend Child")

class Baby(Parent):
    def about_myself(self):
        print("Gu gu ga ga")

def __init__(self):
    super().about()
    super().about_myself()
nick = Child()

