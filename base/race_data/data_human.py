from base.core import Background, Race


# Creating Human Backgrounds

criminal = Background("Criminal")
peasant = Background("Peasant")
outlander = Background("Outlander")
entertainer = Background("Entertainer")
artisan = Background("Artisan")
sailor = Background("Sailor")
soldier = Background("Soldier")
sage = Background("Sage")
acolyte = Background("Acolyte")
noble = Background("Noble")

# Creating Kits for each Background

criminal.addkit("Dagger", "Cloak")
criminal.addkit("Dagger", "Thieves' Tools")
criminal.addkit("Short Sword", "Leather Armor")

peasant.addkit("Pitchfork", "5 Rations of Vegetables")
peasant.addkit("Staff", "Rope")
peasant.addkit("Dagger", "Chicken")

outlander.addkit("Staff", "Torch")
outlander.addkit("Short Bow", "Deer Pelt")
outlander.addkit("Axe", "Herbs")

entertainer.addkit("Dagger", "Musical Instrument")
entertainer.addkit("Club", "Gambling Set")

artisan.addkit("Hammer", "Smith's Tools")
artisan.addkit("Dagger", "Nice Rug (Worth 20GP)")

sailor.addkit("Short Sword", "Rope")
sailor.addkit("Trident", "Net")

soldier.addkit("Spear", "Shield")
soldier.addkit("Longsword", "Hide Armor")

sage.addkit("Dart", "10 sheets of parchment")

acolyte.addkit("Dagger", "Holy Water")

noble.addkit("Longsword", "Signet Ring (Worth 10GP)")



