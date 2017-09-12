from base.core import Background


# Creating Halfling Backgrounds

criminal = Background("Criminal")
outcast = Background("Outcast")
entertainer = Background("Entertainer")
artisan = Background("Artisan")
soldier = Background("Soldier")


# Creating Kits for each Background

criminal.addkit("Dagger", "Thieves' Tools")

outcast.addkit("Short Sword", "Lantern")

entertainer.addkit("Dagger", "Gambling Set")
entertainer.addkit("Dagger", "Musical Instrument")

artisan.addkit("Hammer", "Smith's Tools")

soldier.addkit("Sling", "Leather Armor")



