'''
Create a class called "PetrolPump" that represents a petrol pump. The class should have the
following features:
● A constructor method that initializes the petrol pump with an initial quantity of petrol.
● A method called "fill_petrol" that takes the number of liters as a parameter and adds it to
the existing quantity of petrol.
● A method called "dispense_petrol" that takes the number of liters as a parameter and
dispenses that amount of petrol from the pump, if there is enough petrol available.
● A method called "get_petrol_quantity" that returns the current quantity of petrol in the
pump.
Write the PetrolPump class and demonstrate its usage by creating an instance of the class,
performing petrol filling and dispensing operations, and displaying the current quantity of petrol
in the pump.
'''

class PetrolPump:
    def __init__(self,initial_petrol_quqntity):
        self.petrol_quantity = initial_petrol_quqntity

    def fill_petrol(self,no_of_litres):
        self.petrol_quantity += no_of_litres

    def dispense_petrol(self,no_of_litres):
        if self.petrol_quantity >= no_of_litres:
            self.petrol_quantity -= no_of_litres
            print(f"Dispenced {no_of_litres} Litres of Petrol")
        else:
            print("Insufficient Petrol Available in Pump!")

    def get_petrol_quantity(self):
        return self.petrol_quantity


Indianoil = PetrolPump(100)
print("Initial petrol quantity:", Indianoil.get_petrol_quantity())

Indianoil.fill_petrol(25)
print("Updated petrol quantity:", Indianoil.get_petrol_quantity())

Indianoil.dispense_petrol(30)
print("Updated petrol quantity:", Indianoil.get_petrol_quantity())

Indianoil.dispense_petrol(100)  # More Than Available Capacity
print("Final petrol quantity:", Indianoil.get_petrol_quantity())

