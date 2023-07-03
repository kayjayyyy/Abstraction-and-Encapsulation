# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation

class Fan:
    # Three constants: SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    # Constructor that creates a fan with the specified speed, raidus, color, and on properties
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        # Private int data field named speed
        self.__speed = int(speed)
        # Private float data field named radius
        self.__radius = float(radius)
        # Private string data field named color
        self.__color = str(color)
        # Private bool data field named on
        self.__on = bool(on)
    
    # The accessor (getters) methodl; speed, radius, color and on properties
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on
    
    # The mutator (setters) methods; speed, radius, color and on properties
    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def set_on(self, on):
        self.__on = bool(on)