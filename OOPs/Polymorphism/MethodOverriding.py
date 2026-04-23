class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        #super().fly()
        print("Penguin cannot fly")


input1 = Penguin()
input1.fly()


# Same method name, different implementation
#
# Happens in parent and child class
# Child class redefines the parent method
# Considered runtime polymorphism


#in above example we have diffrent class but have same name function so if i call the fly method inside penguin class this fly will overright the fly method
# in bird class so it print only penguin output when i use use super it will work