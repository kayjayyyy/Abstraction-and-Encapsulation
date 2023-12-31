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

# First Fan properties: maximum speed, radius 10, color yellow, and turn it on
fanOne = Fan()
fanOne.set_speed(Fan.FAST)
fanOne.set_radius(10)
fanOne.set_color("\033[33;1;3mYellow\033[0m")
fanOne.set_on(True)

# First Fan print output
print("~" * 80)
print("\n")
print(pyfiglet.figlet_format("FIRST FAN", font="bubble", justify="center"))
print("\033[32;1;3mSpeed:\033[0m", fanOne.get_speed())
print("\033[32;1;3mRadius:\033[0m", fanOne.get_radius())
print("\033[32;1;3mColor:\033[0m", fanOne.get_color())
print("\033[32;1;3mOn:\033[0m", fanOne.get_on())

# Second Fan properties: medium speed, radius 5, color blue, and turn it off
fanTwo = Fan()
fanTwo.set_speed(Fan.MEDIUM)
fanTwo.set_radius(5)
fanTwo.set_color("\033[34;1;3mBlue\033[0m")
fanTwo.set_on(False)

# Second Fan print output
print("\n")
print("~" * 80)
print("\n")
print(pyfiglet.figlet_format("SECOND FAN", font="bubble", justify="center"))
print("\033[32;1;3mSpeed:\033[0m", fanTwo.get_speed())
print("\033[32;1;3mRadius:\033[0m", fanTwo.get_radius())
print("\033[32;1;3mColor:\033[0m", fanTwo.get_color())
print("\033[32;1;3mOn:\033[0m", fanTwo.get_on())

# Outro and border line
print("\n")
print("\033[3mThank you! Have a great day!".center(80))
print("")
print("\033[35m※ \033[0m" * 40)
print("")