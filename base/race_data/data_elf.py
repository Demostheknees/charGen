from base.core import Background, Race


# Creating Elf Backgrounds

criminal = Background("Criminal")
outcast = Background("Outcast")
entertainer = Background("Entertainer")
artisan = Background("Artisan")
soldier = Background("Soldier")
sage = Background("Sage")

# Creating Kits for each Background

criminal.addkit("Short Sword", "Thieves' Tools")

outcast.addkit("Staff", "Herbs")

entertainer.addkit("Dagger", "Musical Instrument")

artisan.addkit("Dagger", "Jewel (Worth 20Gp")

soldier.addkit("Longbow", "Leather Armor")

sage.addkit("Dagger", "Parchment, Quill, and Ink")

