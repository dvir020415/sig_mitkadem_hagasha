class Animal:
    # Default zoo name
    zoo_name = "Hayaton"

    def __init__(self, name_, hunger_=0):
        # Initialize animal with name and hunger level
        self.name_ = name_
        self.hunger_ = hunger_

    def get_name(self):
        # Get the name of the animal
        return self.name_

    def is_hungry(self):
        # Check if the animal is hungry
        return self.hunger_ > 0

    def feed(self):
        # Feed the animal and decrease its hunger level
        if self.hunger_ > 0:
            self.hunger_ -= 1

    def talk(self):
        # Abstract method for animal sound
        pass

class Dog(Animal):
    def talk(self):
        # Dog sound
        print("woof woof")

    def fetch_stick(self):
        # Special action for dogs
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        # Cat sound
        print("meow")

    def chase_laser(self):
        # Special action for cats
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name_, hunger_=0, stink_count=6):
        # Initialize Skunk with stink count
        super().__init__(name_, hunger_)
        self.stink_count = stink_count

    def talk(self):
        # Skunk sound
        print("tsssss")

    def stink(self):
        # Special action for skunks
        print("Dear lord!")

class Unicorn(Animal):
    def talk(self):
        # Unicorn sound
        print("Good day, darling")

    def sing(self):
        # Special action for unicorns
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self, name_, hunger_=0, color="Green"):
        # Initialize Dragon with color
        super().__init__(name_, hunger_)
        self.color = color

    def talk(self):
        # Dragon sound
        print("Raaaawr")

    def breath_fire(self):
        # Special action for dragons
        print("$@#$#@$")

def main():
    # Creating animals from the first table
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)

    # Creating animals from the second table
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)

    # List of animals
    zoo_lst = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky_jr, clair, mcfly]

    # Iterate over animals
    for animal in zoo_lst:
        # Print type and name of hungry animals
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
        # Feed the animals until they are not hungry
        while animal.is_hungry():
            animal.feed()
        # Perform animal sound
        animal.talk()
        # Perform special action for each animal type
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # Print the zoo name
    print("Zoo name is", Animal.zoo_name)

if __name__ == "__main__":
    main()
