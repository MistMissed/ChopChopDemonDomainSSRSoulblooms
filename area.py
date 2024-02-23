from dataclasses import dataclass

from demon import Demon


@dataclass
class Area:
    """
    class for representing explorable areas in demon domain
    eg. Dark Forest, Bone Altar, Dead Zone
    """

    stamina_per_explore: int
    demons: list[Demon]  # list of possibly encountered enemies

    @property
    def average_soulbloom_per_explore(self):
        """calculate average soulblooms per explore of area"""
        demons_soulbloom_per_challenge = list(
            map(lambda x: x.average_soulbloom_per_challenge, self.demons)
        )
        return sum(demons_soulbloom_per_challenge) / len(demons_soulbloom_per_challenge)

    @property
    def average_soulbloom_per_stamina(self):
        """calculate average soulblooms per stamina used in area"""
        return self.average_soulbloom_per_explore / self.stamina_per_explore
