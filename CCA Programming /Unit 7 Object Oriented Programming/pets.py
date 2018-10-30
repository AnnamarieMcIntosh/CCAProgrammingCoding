class Pet:
    'Base class for all pets'

    __pet_count = 0  # class variable, keeps a count of all pets
    
    def __init__(self, name, species):
        self.name = name         # data attribute/instance variable
        self.species = species   # data attribute/isntance variable
        Pet.__pet_count += 1       # class variable
        
    # class methods
    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def make_noise(self):
        return None

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

    def pet_count():
        return Pet.__pet_count


class Dog(Pet):
    'Dog, a subclass of Pet'
    
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")      # class inheritance
        self.chases_cats = chases_cats       # specialization

    def chases_cats(self):
        return self.chases_cats
    
    def make_noise(self):                    # overload make_noise()
        print("woof woof woof!")


class Cat(Pet):
    'Cat, a subclass of Pet'
    
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hates_dogs(self):
        return self.hates_dogs
    
    def make_noise(self):
        for x in range(2):
            print("meow ", end="")
        print()
 

class Bird(Pet):
    'Bird, a subclass of Pet'
    
    def __init__(self, name, hates_cats):
        Pet.__init__(self, name, "Bird")
        self.hates_cats = hates_cats

    def hates_cats(self):
        return self.hates_cats
    
    def make_noise(self):
        print("tweet")
        print("tweet tweet")
        print("tweet tweet")

    

if __name__ == "__main__":
    fido = Pet("Fido", "Dog")            # instance of Pet class
    fifi = Dog("Fifi", True)             # instance of Dog subclass
    felix = Cat("Felix", True)           # instance of Cat sublcass
    tweety = Bird ("Tweety Bird", False) # instance of Bird subclass

    pets = [fido, fifi, felix, tweety]   
    for pet in pets:
        print(pet.get_name() + ":")
        pet.make_noise()                 # polymorphism
        print()

    print("We have a total of " + str(Pet.pet_count()) + " pets.")




