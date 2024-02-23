from dataclasses import dataclass


@dataclass
class Demon:
    """
    class for representing enemies encountered by exploring in demon domain
    """

    player_victory_chance: float
    ssr_soulbloom_rewards: list[int]  # list of ssr soulblooms possibly rewarded

    @property
    def average_soulbloom_per_victory(self):
        """calculate average ssr soulblooms per defeating this enemy"""
        return sum(self.ssr_soulbloom_rewards) / len(self.ssr_soulbloom_rewards)

    @property
    def average_soulbloom_per_challenge(self):
        """calculate average ssr soulblooms per challenging this enemy"""
        return self.average_soulbloom_per_victory * self.player_victory_chance
