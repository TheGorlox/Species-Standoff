import random
import math

# initialize "Animal"() to init default values.
# initialize "Animal"(power, toughness) to init certain power/toughness


class Animal:
    def __init__(self, *args, **kwargs):
        self.power = args[0]
        self.toughness = args[1]
        self.species = ""

        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }


# TIER1
class Cow(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "cow"
        self.desc = "a milk machine from Earth."
        self.power, self.toughness = 3, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/cow.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 2,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Chicken(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "chicken"
        self.desc = "poops out smaller chickens."
        self.power, self.toughness = 2, 1
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/chicken.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 1,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]
        if(self.on_death["egg"]) > 0:
            print("egg thrown")


class Snake(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "snake"
        self.desc = "a legless abomination. shoots venom from its mouth bones."
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/snake.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 1,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Fish(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "fish"
        self.desc = "soon to be sushi."
        self.power, self.toughness = 1, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/fish.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = .25
        self.crit_multiplier = 4

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Eel(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "eel"
        self.desc = "a shocking hybrid of the fish and the snake."
        self.power, self.toughness = 1, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/eel.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 1,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Dog(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "dog"
        self.desc = "the loyal companion of Earthlings."
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/dog.png"

        # special attributes
        self.dodge_chance = .2
        self.crit_chance = .2
        self.crit_multiplier = 2

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Cat(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "cat"
        self.desc = "cat :)"
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/cat.png"

        # special attributes
        self.dodge_chance = .2
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 1,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Crow(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "crow"
        self.desc = "a flying animal from Earth that collects shiny objects."
        self.power, self.toughness = 1, 1
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/crow.png"

        # special attributes
        self.dodge_chance = .33
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Penguin(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "penguin"
        self.desc = "useless ice bird from Earth."
        self.power, self.toughness = 2, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/penguin.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class PolarBear(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "polarbear"
        self.desc = "a mean and icy panda bear"
        self.power, self.toughness = 4, 3
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/polarbear.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Panda(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "panda"
        self.desc = "a soft and harmless polar bear"
        self.power, self.toughness = 2, 5
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/panda.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


# TIER2
class Glipglop(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "glip glop"
        self.desc = "always watching. always scared. marinating in poison."
        self.power, self.toughness = 2, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/glipglop.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = .5
        self.crit_multiplier = 2

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 1,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Sweebull(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "sweebull"
        self.desc = "covered in poison-filled sacks. bad oral hygiene."
        self.power, self.toughness = 0, 6
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/sweebull.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 1,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 1,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Gnekk(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "g'nekk"
        self.desc = "all neck. all beak. all terror."
        self.power, self.toughness = 3, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/gnekk.png"

        # special attributes
        self.dodge_chance = .1
        self.crit_chance = .33
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 1,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Loodle(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "loodle"
        self.desc = "remember the eel? this one is on fire."
        self.power, self.toughness = 1, 2
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/loodle.png"

        # special attributes
        self.dodge_chance = .25
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 2,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class Niugnep(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "niugnep"
        self.desc = "not so useless now. also burns."
        self.power, self.toughness = 2, 4
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/niugnep.png"

        # special attributes
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 1,
                        "poison": 0,
                        "shock": 0,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


class PolarityBear(Animal):
    def __init__(self, *args, **kwargs):
        self.species = "polarity bear"
        self.desc = "EXTRA mean panda bear."
        self.power, self.toughness = 4, 5
        if args:
            self.power, self.toughness = args[0], args[1]
        self.image = "./images/polaritybear.png"

        # special attributes
        self.dodge_chance = 0.1
        self.crit_chance = 0
        self.crit_multiplier = 1.5

        self.neg_effects = {"burned": 0,
                            "poisoned": 0,
                            }

        self.mutator = {"fire": 0,
                        "poison": 0,
                        "shock": 3,
                        "armor": 0,
                        }

        self.on_death = {"milk": 0,
                         "egg": 0,
                         }

    def die(self, friends, foes, index):
        if index == -1:
            return
        friends[index].toughness += self.on_death["milk"]
        if len(foes) == 0:
            return
        (random.choice(foes)).toughness -= self.on_death["egg"]


def fight(friends, foes):

    foes.reverse()
    if len(friends) != 0 and len(foes) != 0:

        # before attack - takes a list and returns it after all status damage is done (burn, poison etc)
        friends = pre_attack_damage(friends, foes)
        foes = pre_attack_damage(foes, friends)

        # attack - takes lists 1 and 2 and returns the lists after animals fight
        friends, foes = attack(friends, foes)

        # after attack - loops through dead animals and applies "on_death" attributes

        # end phase - loops through death queues and handles the results of who died this round

    # return the lists with possible victors, or empty lists for a tie
    return friends, foes


def pre_attack_damage(team, enemy):
    animal: Animal
    for animal in team:

        animal.toughness -= animal.neg_effects["burned"]
        if(animal.neg_effects["burned"] > 0):
            animal.neg_effects["burned"] -= 1   # weakens per turn

        animal.toughness -= animal.neg_effects["poisoned"]

        if animal.toughness <= 0:
            index = team.index(animal)
            if index == len(team)-1:
                index -= 1
            team.remove(animal)
            animal.die(team, enemy, index)

    return team


def attack(friends, foes):

    if len(friends) > 0:
        friend = friends[0]
    else:
        return friends, foes

    if len(foes) > 0:
        foe = foes[0]
    else:
        return friends, foes

    print(f"{friend.species} - {friend.power}/{friend.toughness} vs {foe.species} - {foe.power}/{foe.toughness}")

    # combat
    combat(friend, foe, friends)
    combat(foe, friend, foes)

    # on die
    if friend.toughness <= 0:
        index = friends.index(friend)
        if index == len(friends)-1:
            index -= 1
        friends.remove(friend)
        friend.die(friends, foes, index)

    if foe.toughness <= 0:
        index = foes.index(foe)
        # if dead animal is last in the list
        if index == len(foes)-1:
            index -= 1
        foes.remove(foe)
        foe.die(foes, friends, index)

    return friends, foes


def combat(team, enemy, teammates):
    if random.random() > team.dodge_chance:
        # if teammate doesnt dodge
        if random.random() <= enemy.crit_chance:
            # if enemy crits
            print(enemy.species, " crit!")
            team.toughness = team.toughness - \
                math.ceil(enemy.power * enemy.crit_multiplier)

        # else normal combat
        else:
            team.toughness = team.toughness - enemy.power
    else:
        print(team.species, " dodged!")

    # add special negative effects after combat and dodge
    team.neg_effects["burned"] = enemy.mutator["fire"]
    team.neg_effects["poisoned"] = enemy.mutator["poison"]

    if teammates.index(team) != len(teammates)-1:
        teammates[teammates.index(team)+1].toughness -= enemy.mutator["shock"]


def load_animal(animal: str):
    animal_dict = {
        "cow": Cow(), "chicken": Chicken(), "snake": Snake(), "fish": Fish(),
        "eel": Eel(), "dog": Dog(), "cat": Cat(), "crow": Crow(), "penguin": Penguin(),
        "polarbear": PolarBear(), "panda": Panda(), "glipglop": Glipglop(),
        "sweebull": Sweebull(), "gnekk": Gnekk(), "loodle": Loodle(), "niugnep": Niugnep(),
        "polaritybear": PolarityBear(),
    }

    return animal_dict[animal]


### TESTING TESTING ONE TWO THREE TESTING TESTING ###
friends = [Eel(), Cow(), PolarBear(), Panda(), Dog(), Chicken()]
foes = [Gnekk(), Loodle(), Loodle(), Niugnep(), PolarityBear(), Sweebull()]


res1, res2 = fight(friends, foes)

if len(res1) == 0 and len(res2) == 0:
    print("tie!")
else:
    item: Animal
    for item in res1:
        print(item.species, " won! (FRIEND)")
    for item in res2:
        print(item.species, "won! (ENEMY)")
