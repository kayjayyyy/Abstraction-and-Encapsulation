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

fanOne = Fan
fanTwo = Fan

fanOne = Fan()
fanOne.set_speed(Fan.FAST)
fanOne.set_radius(10)
fanOne.set_color("Yellow")
fanOne.set_on(True)
