from dataclasses import dataclass


@dataclass
class Demon:
    chance_of_beating: int
    rewards: list[int]

    @property
    def avg_sb(self):
        return sum(self.rewards) / len(self.rewards)

@dataclass
class Area:
    stamina_cost: int
    demons: list[Demon]

    @property
    def avg_sb_per_stamina(self):
        return sum(list(map(lambda x: x.avg_sb, self.demons))) / self.stamina_cost


silver_chest = Demon(1, [0])
gold_chest = Demon(1, [0])

dragon_bell = Demon(1, [0, 0, 0, 6, 2, 0, 0, 0, 0, 0, 0])
guard = Demon(1, [0, 10, 5, 3, 1, 0, 0, 0, 0])
falcon = Demon(1, [0, 2, 0, 0, 0])
ba_cave = Demon(1, [0, 0, 10, 0, 0, 0, 0, 0])

bone_alter = Area(2, [dragon_bell, guard, falcon, silver_chest, gold_chest, ba_cave])

chiyou = Demon(0.1, [0])
priest = Demon(1, [0, 0, 8, 3, 0, 0, 0, 0, 0])
ghoul = Demon(1, [0, 10, 0, 0, 0])
fellow_cultivator = Demon(0.3, [0, 0, 0, 0, 4, 0, 0, 0])
dz_cave = Demon(1, [0])

dead_zone = Area(3, [chiyou, priest, ghoul, fellow_cultivator, silver_chest, gold_chest, dz_cave])

print(round(bone_alter.avg_sb_per_stamina, 2))
print(round(dead_zone.avg_sb_per_stamina, 2))

