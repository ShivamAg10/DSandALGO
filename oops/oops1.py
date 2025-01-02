class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("electric", "SUV")
print(car1.name)
print(car1.type)