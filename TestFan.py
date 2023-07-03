# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation

import pyfiglet

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(90))
print("")
print(pyfiglet.figlet_format("FAN", font="isometric2", justify="center"))

from ClassFan import Fan

fanOne = Fan()
fanOne.set_speed(Fan.FAST)
fanOne.set_radius(10)
fanOne.set_color("Yellow")
fanOne.set_on(True)

print("~" * 80)
print(pyfiglet.figlet_format("FIRST FAN", font="bubble", justify="center"))
print("Speed:", fanOne.get_speed())
print("Radius:", fanOne.get_radius())
print("Color:", fanOne.get_color())
print("On:", fanOne.get_on())

fanTwo = Fan()
fanTwo.set_speed(Fan.MEDIUM)
fanTwo.set_radius(5)
fanTwo.set_color("blue")
fanTwo.set_on(False)

print("~" * 80)
print(pyfiglet.figlet_format("SECOND FAN", font="bubble", justify="center"))
print("Speed:", fanTwo.get_speed())
print("Radius:", fanTwo.get_radius())
print("Color:", fanTwo.get_color())
print("On:", fanTwo.get_on())