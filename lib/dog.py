#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
print(fido.name)   # Fido
print(fido.breed)  # Mutt
fido.bark()        # Woof!
fido.sit()         # The dog is sitting.
fido.get_adopted("Sophie")
print(fido.owner)  # Sophie

snoopy = Dog("Snoopy", "Beagle")
print(snoopy.name)  # Snoopy
print(snoopy.breed) # Beagle
