# Demon Domain SSR Soulbloom Guide
**Last Updated**: February 2, 2024
## Introduction
Demon domain is one of the best ways to gain SSR Soulblooms in the game. This project seeks to answer the question: "What area is best to explore for getting the most SSR soulblooms?"

## Methodology
### Demons
Each enemy is represented in code using a class 'Demon', which contains: 
- a probability of a player defeating it (float)
- possibly rewarded ssr soulblooms (list)

If an enemy has:
- 3 rewards which drop 0 ssr soulblooms
- a reward which drops 5 ssr soulblooms

Its rewards may be represented as: 
> [0, 0, 0, 5]

Probability of defeating an enemy will be represented as a float. (eg. 10% -> 0.1, 100% -> 1.0)

From this information, the average ssr soulblooms rewarded per challenge and per victory of each enemy can be calculated.

### Areas
Dark Forest area is ignored due to not rewarding any ssr soulblooms.

Each area is represented in code using a class 'Area', which contains:
- stamina consumed per exploration (int)
- all possible enemies which can be encountered (list[Demon])

Stamina consumed per exploration:
- Bone Altar: 2
- Dead Zone: 3

Possibly encountered enemies will be stored as discussed above in the 'Demons' section.

Enemies in Bone Altar:
- Fury Dragon Bell
- Fury Guard
- ...
- Gold Demonic Chest
- Hidden Cave

From this information, the average ssr soulblooms rewarded per exploration and per stamina consumed can be calculated.

## Assumptions Made
This section holds assumptions made either about the player or the game:
- Enemies are assumed to have an equal **probability of dropping** any of their rewards
- Enemies (unless otherwise specified) are assumed to have a **100% chance of being defeated** by the player
- **Chests** are assumed to go unopened
- **Chiyou** is assumed to have a 10% chance of being defeated by the player
- **Fellow cultivators** are assumed to have a 30% chance of being defeated by the player
- Players do not receive **assistance** from teammates

## Results
### Bone Altar
Each exploration yields an average of 0.748 ssr soulblooms.

Each stamina consumed yields an average of 0.374 ssr soulblooms.
### Dead Zone
Each exploration yields an average of 0.482 ssr soulblooms.

Each stamina consumed yields an average of 0.161 ssr soulblooms.

## Conclusions
The optimal area for farming SSR soulblooms may change in the future, but as of February 2, 2024:

For most people, **exploring Bone Altar will yield over twice as many SSR soulblooms overall.**

To maximize the amount of SSR soulblooms collected in demon domain, a player must get out of Dark Forest as quickly as possible, then explore Bone Altar as much as possible.

**My Discord:** mistyyyyy
