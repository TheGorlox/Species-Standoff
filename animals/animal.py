
# initialize "Animal"() to init default values.
# initialize "Animal"(power, toughness) to init certain power/toughness
class Animal:
    def __init__(self, *args, **kwargs):
        self.power = args[0]
        self.toughness = args[1]


class Cow(Animal):
    def __init__(self, *args, **kwargs):
        self.type = "cow"
        self.desc = "a milk machine from Earth."
        self.power, self.toughness = 3,3
        if args:
            self.power, self.toughness = args[0], args[1]

class Chicken(Animal):
    def __init__(self, *args, **kwargs):
        type = "chicken"
        desc = "poops out smaller chickens."
        self.power, self.toughness = 2,1
        if args:
            self.power, self.toughness = args[0], args[1]

class Snake(Animal):
    def __init__(self, *args, **kwargs):
        type = "snake"
        desc = "a legless abomination from Earth. Shoots venom from its mouth bones."
        self.power, self.toughness = 3,1
        if args:
            self.power, self.toughness = args[0], args[1]

class Fish(Animal):
    def __init__(self, *args, **kwargs):
        type = "fish"
        desc = "soon to be sushi."
        self.power, self.toughness = 1,2
        if args:
            self.power, self.toughness = args[0], args[1]

class Eel(Animal):
    def __init__(self, *args, **kwargs):
        type = "eel"
        desc = "a shocking hybrid of the Earth fish and Earth snake."
        self.power, self.toughness = 3,2
        if args:
            self.power, self.toughness = args[0], args[1]

class Dog(Animal):
    def __init__(self, *args, **kwargs):
        type = "dog"
        desc = "the loyal companion of Earthlings."
        self.power, self.toughness = 2,2
        if args:
            self.power, self.toughness = args[0], args[1]

class Cat(Animal):
    def __init__(self, *args, **kwargs):
        type = "cat"
        desc = "cat"
        self.power, self.toughness = 2,2
        if args:
            self.power, self.toughness = args[0], args[1]

class Crow(Animal):
    def __init__(self, *args, **kwargs):
        type = "crow"
        desc = "a flying animal from Earth that collects shiny objects."
        self.power, self.toughness = 3,1
        if args:
            self.power, self.toughness = args[0], args[1]

class Penguin(Animal):
    def __init__(self, *args, **kwargs):
        type = "penguin"
        desc = "useless ice bird from Earth."
        self.power, self.toughness = 2,3
        if args:
            self.power, self.toughness = args[0], args[1]

class PolarBear(Animal):
    def __init__(self, *args, **kwargs):
        type = "polarbear"
        desc = "a mean and icy panda bear"
        self.power, self.toughness = 4,2
        if args:
            self.power, self.toughness = args[0], args[1]

class Panda(Animal):
    def __init__(self, *args, **kwargs):    
        type = "panda"
        desc = "a soft and harmless polar bear"
        self.power, self.toughness = 2,4
        if args:
            self.power, self.toughness = args[0], args[1]


