# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = int(speed)
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)
        
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on
    
    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_radius(self, radius):
        self.__raduis = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def set_on(self, on):
        self.__color = bool(on)