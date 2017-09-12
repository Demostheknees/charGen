from random import choice


def roll(item):
    """Base Function"""
    result = choice(item)
    return result


def get(race):
    """generates a Background and Kit for a given Race."""
    result_background = roll(race.backgrounds)
    result_kit = roll(race.data[result_background]["Kits"])

    print("Race: " + race.name)
    print("Background: " + result_background)
    print("Kit: " + result_kit[0] + ", " + result_kit[1])


class Generator:

    def __init__(self, name):
        self.name = name
        self.races = []

    def generate(self):
        race = roll(self.races)
        get(race)



class Race:

    def __init__(self, name):
        """Stores a given set of backgrounds as a dict. contains data for referencing later."""
        self.name = name
        self.data = {}
        self.backgrounds = []

    def addto(self, generator, weight):
        for x in range(0,weight):
            generator.races.append(self)


class Background:

    def __init__(self, name):
        """Core data for a Background."""
        self.name = name
        self.weight = []
        self.data = {
            name: {
                "Kits": []
            }
        }

    def addkit(self, item1, item2):
        """Adds to the "Kits" key of a Background. Each Kit adds to the weight of a Background."""
        self.data[self.name]["Kits"].append([item1, item2])
        self.weight.append(self.name)

    def addto(self, race):
        """Adds a background to a Race. Current weight defines occurrences in Race.Backgrounds"""
        race.data.update(self.data)
        race.backgrounds.extend(self.weight)
