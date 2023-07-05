# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment no. 9 - Abstraction and Encapsulation (Pet Class)

# Private constructor for pet class with following attributes: name, animal type, and age
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    # The accessor (getters) methods: name, animal type, and age
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    # The mutator (setters) methods: name, animal type, and age
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age