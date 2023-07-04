# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation (Car Class)

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
        
    def brake(self):
        self.__speed -= 5