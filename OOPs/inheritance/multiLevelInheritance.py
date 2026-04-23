class grandParent:
    def grandParentMethod(self):
        print("this is grandfather class")

class parent(grandParent):
    def parentMethod(self):
        print("this is parent class")

class child(parent):
    def childMethod(self):
        print("this is child class")

c = child()
c.childMethod()
c.parentMethod()
c.grandParentMethod()


#multilevelInheritance: so in multilevel inheritance there is a chain see in example where main class is grandfather and parent inherit the
#property of grandfather and like this child inherit the property of parent s so now child have access of all the class like grandfather, pat