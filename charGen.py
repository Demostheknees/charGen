from base.core import Generator

from base.races import human, elf, dwarf, halfling


def charGen():
    result = Generator("Character Generation")

    human.addto(result, 7)
    elf.addto(result, 1)
    dwarf.addto(result, 1)
    halfling.addto(result, 1)

    print(result.name)
    print(" ")

    result.generate()


charGen()















