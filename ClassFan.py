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