class parent:
    def show(self):
        print("this is a parent class")
class child(parent):
    def display(self):
        print("this is a child class")

c = child()
c.display()
c.show()


#Inheritance : Inheritance is where child class inherit the property of parents class

#in above example child class can inherit the property of parent class so using child class we can call the function of parent class
