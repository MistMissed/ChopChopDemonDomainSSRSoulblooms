# based on demon domain rewards as of 2/23/2024
from area import Area
from demon import Demon

# assumed chests will not be opened
# chests therefore grant no soulblooms
silver_chest = Demon(0, [0])
gold_chest = Demon(0, [0])

# assumed 100% chance of beating bone altar enemies
dragon_bell = Demon(1, [0, 0, 0, 6, 2, 0, 0, 0, 0, 0, 0])
guard = Demon(1, [0, 10, 5, 3, 1, 0, 0, 0, 0])
falcon = Demon(1, [0, 2, 0, 0, 0])
bone_altar_cave = Demon(1, [0, 0, 10, 0, 0, 0, 0, 0])

bone_altar = Area(
    2, [dragon_bell, guard, falcon, silver_chest, gold_chest, bone_altar_cave]
)

# assumed 100% chance of beating dead zone enemies
priest = Demon(1, [0, 0, 8, 3, 0, 0, 0, 0, 0])
ghoul = Demon(1, [0, 10, 0, 0, 0])
dz_cave = Demon(1, [0])
chiyou = Demon(0.1, [0])  # assumed 10% chance of beating chiyou
fellow_cultivator = Demon(
    0.3, [0, 0, 0, 0, 4, 0, 0, 0]
)  # assumed 30% chance of beating fellow cultivator

dead_zone = Area(
    3, [chiyou, priest, ghoul, fellow_cultivator, silver_chest, gold_chest, dz_cave]
)

print("bone altar:")
print("  ssr soulblooms per:")
print("    explore:", round(bone_altar.average_soulbloom_per_explore, 2))
print("    stamina:", round(bone_altar.average_soulbloom_per_stamina, 2))

print("dead zone:")
print("  ssr soulblooms per:")
print("    explore:", round(dead_zone.average_soulbloom_per_explore, 2))
print("    stamina:", round(dead_zone.average_soulbloom_per_stamina, 2))
