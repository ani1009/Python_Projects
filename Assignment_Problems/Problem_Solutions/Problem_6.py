'''
Create a class called "Product" that represents a retail product. The class should have the
following features:
● A constructor method that takes the product name, price, and quantity in stock as
parameters and initializes them.
● A method called "calculate_total_cost" that calculates and returns the total cost of a
specified quantity of the product, taking into account any discounts or promotions.
● A method called "display_product_details" that prints the product name, price, and
quantity in stock.
Write the Product class and demonstrate its usage by creating an instance of the class,
calculating the total cost for a specific quantity, and displaying the product details.
'''

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self,quantity):
        total_cost = self.price * quantity
        return total_cost

    def display_product_details(self):
        print("Product Name:",self.name)
        print("Product Price:",self.price)
        print("Product Quantity:",self.quantity)

product = Product("Wifi Modem", 700, 50)

quantity_needed = 10
total_cost = product.calculate_total_cost(quantity_needed)

product.display_product_details()
print(f"Total Cost for {quantity_needed} units: {total_cost}")



