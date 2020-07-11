#animal example inheritance

# class Animal :
#     cool = True
    
#     def makeSound(self, sound):
#         print(f"This animal make sound {sound}")

# class cat(Animal):
#     pass

# blue = cat()
# blue.makeSound("Meow")

# class Human :
#     def __init__(self,first,last,age):
#         self.first = first,
#         self.last = last,
#         if age>=0:
#             self._age = age
#         else:
#             self._age = 0

#     # def get_age(self):
#     #     return self._age
    
#     # def set_age(self,new_age):
#     #     if new_age >=0:
#     #         self._age = new_age
#     #     else:
#     #         self._age = 0

#     @property
#     def age(self) :
#         return self._age b vg

#     @age.setter #we can set age without using it as a function or parenthesis
#     def age(self,value):
#         if value>=0:
#             self._age = value
#         else:
#             raise ValueError("age can't be negative")


# tarun = Human("Tarun", "Kantiwal", -21)
# print(tarun.get_age())
# tarun.set_age(10)
# print(tarun.get_age())


#introduction of Super()

class Animal :
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def makeSound(self, sound):
        print(f"This animal make sound {sound}")
    
    def __repr__ (self):
        return (f"{self.name} is a  {self.species}")

class cat(Animal):
    def __init__ (self, name, breed, toy):
        super().__init__(name, species="Cat") #use of super instead of Anima__init__()
        # Animal.__init__(self,name, species)
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = cat("Blue","Scottish Fold", "String")
blue.play()

