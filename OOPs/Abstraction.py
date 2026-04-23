class car:
    def __init__(self):
        self.brake = False
        self.clutch = False
        self.acc = False
    def start(self):
        self.brake = True
        self.clutch = True
        print("car started")

car1 = car()
car1.start()

#Abstraction
#the car class demonstrates the concept of abstraction by hiding the internal details of how a car operates
#it shows only essential functionalities, such as the ability to start the car.