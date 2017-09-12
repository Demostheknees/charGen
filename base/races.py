from base.race_data import data_human
from base.race_data import data_elf
from base.race_data import data_dwarf
from base.race_data import data_halfling

from base.core import Race


# Creating the Race: Human

human = Race("Human")

# Adding The Backgrounds to the Race: Human

data_human.criminal.addto(human)
data_human.peasant.addto(human)
data_human.outlander.addto(human)
data_human.entertainer.addto(human)
data_human.artisan.addto(human)
data_human.sailor.addto(human)
data_human.soldier.addto(human)
data_human.sage.addto(human)
data_human.acolyte.addto(human)
data_human.noble.addto(human)


# Creating the Race: Elf

elf = Race("Elf")

# Adding The Backgrounds to the Race: Elf

data_elf.criminal.addto(elf)
data_elf.outcast.addto(elf)
data_elf.entertainer.addto(elf)
data_elf.artisan.addto(elf)
data_elf.soldier.addto(elf)
data_elf.sage.addto(elf)


# Creating the Race: Dwarf

dwarf = Race("Dwarf")

# Adding The Backgrounds to the Race: Dwarf

data_dwarf.criminal.addto(dwarf)
data_dwarf.peasant.addto(dwarf)
data_dwarf.outcast.addto(dwarf)
data_dwarf.artisan.addto(dwarf)
data_dwarf.soldier.addto(dwarf)


# Creating the Race: Halfling

halfling = Race("Halfling")

# Adding The Backgrounds to the Race: Halfling

data_halfling.criminal.addto(halfling)
data_halfling.outcast.addto(halfling)
data_halfling.entertainer.addto(halfling)
data_halfling.artisan.addto(halfling)
data_halfling.soldier.addto(halfling)