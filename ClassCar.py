# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation (Car Class)

# Private constructor with year model, make, and speed
class Car:
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
    # Accelerate method should add 5 to the speed data attribute each time it is called
    def accelerate(self):
        self.__speed += 5
    
    # Brake method should subtract 5 from the speed data attribute each time it is called 
    def brake(self):
        self.__speed -= 5
    
    # The get_speed method should return the current speed
    def get_speed(self):
        return self.__speed