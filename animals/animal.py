import random
import math
# initialize "Animal"() to init default values.
# initialize "Animal"(power, toughness) to init certain power/toughness
class Animal:
    def __init__(self, *args, **kwargs):
        self.power = args[0]
        self.toughness = args[1]
        self.species = ""
    
    dodge_chance = 0
    crit_chance = 0

    neg_effects = { "burn":0,
                    "poison":0,
                    }
    
    mutator = { "fire":0,
                "poison":0,
                "shock":0,
                "armor":0,
                }


    death_q = []

    # def die(self):


class Cow(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "cow"
        self.desc = "a milk machine from Earth."
        self.power, self.toughness = 3, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/cow.png"

        #special attributes



class Chicken(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "chicken"
        self.desc = "poops out smaller chickens."
        self.power, self.toughness = 2, 1
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/chicken.png"

        #special attributes



class Snake(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "snake"
        self.desc = "a legless abomination from Earth. Shoots venom from its mouth bones."
        self.power, self.toughness = 3, 1
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/snake.png"

        #special attributes



class Fish(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "fish"
        self.desc = "soon to be sushi."
        self.power, self.toughness = 1, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/fish.png"

        #special attributes
        self.crit_chance = .2



class Eel(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "eel"
        self.desc = "a shocking hybrid of the Earth fish and Earth snake."
        self.power, self.toughness = 3, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/eel.png"

        #special attributes
        self.mutator["shock"] = 1



class Dog(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "dog"
        self.desc = "the loyal companion of Earthlings."
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/dog.png"

        #special attributes



class Cat(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "cat"
        self.desc = "cat"
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/cat.png"

        #special attributes



class Crow(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "crow"
        self.desc = "a flying animal from Earth that collects shiny objects."
        self.power, self.toughness = 1, 1
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/crow.png"

        #special attributes
        self.dodge_chance = .2


class Penguin(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "penguin"
        self.desc = "useless ice bird from Earth."
        self.power, self.toughness = 2, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/penguin.png"

        #special attributes



class PolarBear(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "polarbear"
        self.desc = "a mean and icy panda bear"
        self.power, self.toughness = 4, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/polarbear.png"

        #special attributes



class Panda(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "panda"
        self.desc = "a soft and harmless polar bear"
        self.power, self.toughness = 2, 4
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/panda.png"

        #special attributes



def fight(list1, list2):
    list2.reverse()
    while len(list1) != 0 and len(list2) != 0:

        #before attack - takes a list and returns it after all status damage is done (burn, poison etc)
        list1 = pre_attack_damage(list1)
        list2 = pre_attack_damage(list2)

        #attack - takes lists 1 and 2 and returns the lists after animals fight
        list1, list2 = attack(list1, list2)

        #after attack - loops through death queue and handles the results of who died this round
        animal: Animal
        for animal in Animal.death_q:
            print(animal.species, " died!")
        Animal.death_q.clear()
    
    # return the lists with possible victors, or empty lists for a tie
    return list1, list2

def pre_attack_damage(lis):
    animal: Animal
    for animal in lis:
        animal.toughness -= animal.neg_effects["burn"]
        animal.toughness -= animal.neg_effects["poison"]
        if animal.toughness <= 0:
            Animal.death_q.append(lis.pop(animal))
    return lis

def attack(list1, list2):

    animal1 = list1[0]
    animal2 = list2[0]

    print(f"{animal1.species} - P{animal1.power}/T{animal1.toughness} vs {animal2.species} - P{animal2.power}/T{animal2.toughness}")
        
    # animal 1 combat
    if random.random() > animal1.dodge_chance:
        # if animal 1 doesnt dodge
        if random.random() <= animal2.crit_chance:
            # if animal 2 crits
            print(animal2.species, " crit!")
            animal1.toughness = animal1.toughness - math.floor(animal2.power * 1.5)

        # else normal combat
        else: animal1.toughness = animal1.toughness - animal2.power
    else:
        print(animal1.species, " dodged!")

    # animal 2 combat
    if random.random() > animal2.dodge_chance:
        # if animal 2 doesnt dodge
        if random.random() <= animal1.crit_chance:
            # if animal 2 crits
            print(animal1.species, " crit!")
            animal2.toughness = animal2.toughness - math.floor(animal1.power * 1.5)
        
        # else normal combat
        else: animal2.toughness = animal2.toughness - animal1.power
    else:
        print(animal2.species," dodged!")
    
    # on die
    if animal1.toughness <= 0 and animal2.toughness <= 0:
        Animal.death_q.append(list1.pop(0))
        Animal.death_q.append(list2.pop(0))
    if animal1.toughness <= 0:
        Animal.death_q.append(list1.pop(0))
    if animal2.toughness <= 0:
        Animal.death_q.append(list2.pop(0))

    return list1, list2

### TESTING TESTING ONE TWO THREE TESTING TESTING ###
list1 = [Cow(), Chicken(), Panda(), Crow(), Dog()]
list2 = [Penguin(), Fish(), Eel(), Crow(), PolarBear()]

res1, res2 = fight(list1, list2)

if len(res1) == 0 and len(res2) == 0:
    print("tie!")
else:
    item:Animal
    for item in res1:
        print(item.species, " won! (FRIEND)")
    for item in res2:
        print(item.species, "won! (ENEMY)")