# The Legend of Zelda: Oracle of Seasons Setup Guide

## Required Software

- [Oracle of Seasons .apworld](https://github.com/Dinopony/Archipelago/releases/latest)
- [Oracles Archipelago Patcher](https://github.com/Dinopony/oracles-archipelago-patcher/releases/latest)
- [Bizhawk 2.9.1 (x64)](https://tasvideos.org/BizHawk/ReleaseHistory)
- Your legally obtained Oracle of Seasons US ROM file

## Installation Instructions

1. Download the **Oracle of Seasons .apworld file** and put it inside the "lib/worlds/" subdirectory of your Archipelago install directory
2. Generate a seed using your .yaml settings file (see template below)
3. When generating, the server built for you a .patcherdata file that can be fed to the **Oracles Archipelago Patcher** software, download it
4. Download the **Oracles Archipelago Patcher** software and unzip it in its own directory
5. Put your **Oracle of Seasons US ROM** inside this folder (name doesn't matter as long as it has the .gbc file extension)
6. Get your own .patcherdata file that was generated by Archipelago Server while generating
7. Right-click the .patcherdata file, select "Open With..." and point to the **oracles-archipelago-patcher.exe** inside the same directory where you previously put the vanilla ROM
8. If everything went fine, the patched ROM should have appeared next to the .patcherdata file
9. Open the patched ROM inside Bizhawk
10. Inside Bizhawk, go into "Tools > Lua Console", then "Script > Open Script" and pick the "connector_bizhawk_generic.lua" file inside the "data/lua/" subfolder of your Archipelago install 
11. Launch Bizhawk Generic Client, it should automatically connect to the emulator
12. Connect the Client to the AP Server of your choice, and you can start playing!

## Create a Config (.yaml) File

Edit the following template for your settings:
```yaml
"The Legend of Zelda - Oracle of Seasons":
  progression_balancing: 50
  accessibility: items

  # Determine the amount of essences required to get the Maku Seed and be able to confront Onox
  # (number between 0 and 8)
  required_essences: 8

  # The world of Holodrum is split in regions, each one having its own default season being forced when entering it.
  # This options gives several ways of manipulating those default seasons.
  # - vanilla: default seasons for each region are the ones from the original game
  # - randomized: each region has its own random default season picked at generation time
  # - singularity: only one season is randomly picked and put in every region in the game
  default_seasons: randomized

  # Determines which animal companion you can summon using the Flute, as well as the layout of the Natzu region.
  # - ricky: the kangaroo with boxing skills
  # - dimitri: the swimming dinosaur who can eat anything
  # - moosh: the flying blue bear with a passion for Spring Bananas
  animal_companion: random

  # The difficulty of the logic used to generate the seed.
  # - casual: expects you to know what you would know when playing the game for the first time
  # - medium: expects you to know well the alternatives on how to do basic things, but won't expect any trick
  # - hard: expects you to have all knowledge and to be able to perform difficult tricks
  logic_difficulty: casual

  # - vanilla: each dungeon entrance leads to its intended dungeon
  # - shuffle: each dungeon entrance leads to a random dungeon picked at generation time
  shuffle_dungeons: shuffle

  # - vanilla: pairs of portals are the same as in the original game
  # - shuffle: each portal in Holodrum is connected to a random portal in Subrosia picked at generation time
  shuffle_portals: shuffle

  # This option defines how the "secret sequence" (both directions and seasons) leading to the Noble Sword pedestal
  # is handled by the randomizer.
  # - vanilla: the sequence is the same as in the original game
  # - randomized: the sequence is randomized, and you need to use the Phonograph on the Deku Scrub to learn the sequence
  lost_woods_item_sequence: randomized

  #  Determine how the Old Men that can be found under specific bushes are handled by the randomizer
  #  - vanilla: Each Old Man gives/takes the amount of rupees it usually does in the base game
  #  - shuffled_values: The rupee values given/taken are shuffled among Old Men
  shuffle_old_men: vanilla

  # Defines the quality of the rings that will be shuffled in your seed:
  #  - any: any ring can potentially be shuffled (including literally useless ones)
  #  - only_useful: only useful rings will be shuffled
  ring_quality: only_useful

  # In the vanilla game, the Fool's Ore is the item "given" by the strange brothers in "exchange" for your feather.
  # The way the vanilla game is done means you never get to use it, but it's by far the strongest weapon in the game
  # (dealing 4 times more damage than an L-2 sword!)
  #  - vanilla: Fool's Ore appears in the item pool with its stats unchanged
  #  - balanced: Fool's Ore appears in the item pool but its stats are lowered to become comparable to an L-2 sword
  #  - excluded: Fool's Ore doesn't appear in the item pool at all. Problem solved!
  fools_ore: balanced

  # When enabled, you can warp to start by holding Start while exiting map screen.
  # This makes backtracking a bit more bearable in seeds where Gale Seeds take time to obtain and prevent
  # most softlock situations from happening.
  # Enabling this is HIGHLY encouraged in most cases.
  warp_to_start: on

  # - default: play the beeping sound at the usual frequency when low on health
  # - half: play the beeping sound two times less when low on health
  # - quarter: play the beeping sound four times less when low on health
  # - disabled: never play the beeping sound when low on health
  heart_beep_interval: default

description: 'YAML Template for Oracle of Seasons'
game: "The Legend of Zelda - Oracle of Seasons"
name: Player
```