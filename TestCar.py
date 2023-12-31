# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation (Car Class)

import pyfiglet
from ClassCar import Car

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(90))
print("")
print(pyfiglet.figlet_format("CAR INFO'S", font="bulbhead", justify="center"))

# Ask for users name
name = input("\n\033[033mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

print("\033[36m Let's get started! \033[0m".center(90, "~"))

# Assign year model and make
new_car = Car (1956, "Corvette")

# Display cars brand/name
print("")
print(pyfiglet.figlet_format("CORVETTE", font="speed", justify="center"))
key = input("\033[35mPress ENTER to start...\033[0m".center(90))

# Accelerate banner
print("")
print(pyfiglet.figlet_format("ACCELERATE", font="bubble", justify="center"))
print("\n")

# Get the current speed when the cars accelerate
for i in range(1, 6):
    new_car.accelerate()
    print("\033[34mCurrent Speed: \033[0m", new_car.get_speed())

# Brake banner
print("")
print("~" * 81)
print(pyfiglet.figlet_format("BRAKE", font="bubble", justify="center"))
print("\n")

# Get the current speed when the car brakes
for i in range(1, 6):
    new_car.brake()
    print("\033[34mCurrent Speed: \033[0m", new_car.get_speed())
    
# Outro and border line
print("\n")
print("\033[3mThank you! Have a great day!".center(80))
print("")
print("\033[35m※ \033[0m" * 40)
print("")