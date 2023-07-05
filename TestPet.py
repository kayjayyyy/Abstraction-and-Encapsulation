# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation (Pet Class)

import pyfiglet

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(90))
print("")

from ClassPet import Pet

your_pet = Pet

print(pyfiglet.figlet_format("Pet's Info", font="bulbhead", justify="center"))

pet_name = input("\033[36;3mEnter the name of your pet: \033[0m")
pet_type = input("\033[36;3mEnter the type of your pet: \033[0m")
pet_age = input("\033[36;3mEnter the age of your pet: \033[0m")

print("")
print("-" * 80)
print("\033[1;3;32mProcessing..........\033[0m".center(90))
print("-" * 80)