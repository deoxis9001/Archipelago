# Guide d'installation de The Legend of Zelda : Oracle of Seasons

## Logiciel requis

- [Oracle of Seasons .apworld](https://github.com/Dinopony/Archipelago/releases/latest)
- [Oracles Archipelago Patcher](https://github.com/Dinopony/oracles-archipelago-patcher/releases/latest)
- Bizhawk 2.9.1 (x64)](https://tasvideos.org/BizHawk/ReleaseHistory)
- Votre ROM Oracle of Seasons US obtenu légalement

## Instructions d'installation

1. Téléchargez le fichier **Oracle of Seasons .apworld** et placez-le dans le sous-répertoire "lib/worlds/" de votre répertoire d'installation d'Archipelago.
2. Générez en utilisant votre fichier de configuration .yaml (voir le modèle ci-dessous).
3. Lors de la génération, le serveur a généré pour vous un fichier .patcherdata qui pourra être transmis au logiciel **Oracles Archipelago Patcher**, téléchargez-le.
4. Téléchargez le logiciel **Oracles Archipelago Patcher** et décompressez-le dans son propre répertoire.
5. Placez votre **Rom de Oracles of Seasons US** dans ce dossier (le nom n'a pas d'importance tant qu'il a l'extension .gbc).
6. Récupérez votre propre fichier .patcherdata qui a été généré par Archipelago lors de la génération du fichier .patcherdata.
7. Faites un clic droit sur le fichier .patcherdata, sélectionnez "Open With..." et pointez sur **oracles-archipelago-patcher.exe** dans le même répertoire que celui où vous avez placé la ROM vanille.
8. Si tout s'est bien passé, la ROM patchée devrait apparaître à côté du fichier .patcherdata.
9. Ouvrez la ROM patchée dans Bizhawk
10. Dans Bizhawk, allez dans "Tools > Lua Console", puis "Script > Open Script" et choisissez le fichier "connector_bizhawk_generic.lua" dans le sous-dossier "data/lua/" de votre installation Archipelago. 
11. Lancez Bizhawk Generic Client, il devrait se connecter automatiquement à l'émulateur.
12. Connectez le client au serveur AP de votre choix, et vous pouvez commencer à jouer !

## Créer un fichier de configuration (.yaml)

Modifiez le modèle suivant en fonction de vos paramètres :
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
