class smartphone:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"{self.make},{self.year},{self.model}")

smartphone1=smartphone("iphone","2025","iphone17")
smartphone2=smartphone("samsung","2025","galaxy")
print (smartphone1.make)
smartphone2.display_info()

#the following exaple is a show of  polymorphism
class book:
    def sub_genre(self):
        pass
    def book_info(self):
        print(f"{self.sub_genre()}")
class science(book):
    def sub_genre(self):
        return "technical"
class social(book):
    def sub_genre(self):
        return "art"
    
science=science()
social=social()

science.book_info()
social.book_info()

print(science.sub_genre())
print(social.sub_genre())


#polymorphism challenge
class Animal:
    def make_sound(self):
        pass
    
    def move(self):
        return "moves"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "runs"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
    def move(self):
        return "sneaks"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"
    
    def move(self):
        return "flies"

def animal_actions(animals):
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.make_sound()} and {animal.move()}")

animals = [Dog(), Cat(), Bird()]
animal_actions(animals)