'''
Create a class called "Circle" that represents a circle object. The class should have the following
features:
● A constructor method that takes the radius as a parameter and initializes it.
● A method called "get_area" that calculates and returns the area of the circle.
● A method called "get_circumference" that calculates and returns the circumference of
the circle.
Write the Circle class and demonstrate its usage by creating an instance of the class, setting a
radius, and printing the area and circumference of the circle.
'''

class circle:
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * self.radius ** 2
    def get_circumference(self):
        return 2 * 3.14 * self.radius

radius = 4
cal_circle = circle(radius)
print(f"Radius: {radius}")

area = cal_circle.get_area()
print(f"Area: {3.14 * radius ** 2}")

circumference = cal_circle.get_circumference()
print(f"Circumference: {2 * 3.14 * radius}")





