from base.core import Background


# Creating Dwarf Backgrounds

criminal = Background("Criminal")
peasant = Background("Peasant")
outcast = Background("Outcast")
artisan = Background("Artisan")
soldier = Background("Soldier")


# Creating Kits for each Dwarf Background

criminal.addkit("Club", "Thieves' Tools")

peasant.addkit("Club", "Lantern")

outcast.addkit("Dagger", "Rope")

artisan.addkit("Hammer", "Smith's Tools")

soldier.addkit("Axe", "Shield")
soldier.addkit("Axe", "Axe")
