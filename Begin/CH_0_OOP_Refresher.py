# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car:

  # Constructor (Initialization) - __init__ method
  def __init__(self, make, model):
    self.make = make
    self.model = model



  # Encapsulation: Attributes (make and model) are encapsulated within the class.


  # Method - start_engine
  def start_engine(self):
    print(f"The {self.make} {self.model} vehicle is running!")

# Encapsulation: Accessing attributes through self.


# Creating instances (objects) of the Car class
car1 = Car("Porsche",'911 gt3')
car2 = Car("Land Rover",'Defender')

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.

# Creating the first car (object)

# Creating the second car (object)


# Accessing object attributes
car1.start_engine()
car2.start_engine()

# Encapsulation: Accessing object attributes (make and model) using dot notation.


# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).


# Method Call - start_engine
