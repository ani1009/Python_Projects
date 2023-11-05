'''
Create a class called "Car" that represents a car in an automotive system. The class should
have the following features:
● A constructor method that takes the car's make, model, and year as parameters and
initializes them.
● A method called "start_engine" that starts the car's engine and prints a message
indicating that the engine has started.
● A method called "accelerate" that takes a speed as a parameter and simulates the car
accelerating to that speed.
● A method called "display_car_info" that prints the car's make, model, and year.
Write the Car class and demonstrate its usage by creating an instance of the class, starting the
engine, accelerating the car, and displaying the car's information.
'''

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        self.engine_started = True
        print("The Engine Has Started!")

    def accelerate(self,speed):
        if self.engine_started:
            print(f"The Car is Accelerating to {speed} KM/H")
        else:
            print("Please Start the Engine First!")

    def display_car_info(self):
        print(f"Car Information: {self.make} {self.model} {self.year}")

my_car = Car("Toyota", "Etios Liva",2017)
my_car.display_car_info()

my_car.start_engine()

my_car.accelerate(60)
