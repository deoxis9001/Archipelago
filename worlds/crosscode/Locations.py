from typing import NamedTuple
from BaseClasses import Location

class CrossCodeLocation(Location):
    game: str = "CrossCode"

    def __init__(self, player: int, name = "", code = None, parent = None):
        super(CrossCodeLocation, self).__init__(player, name, code, parent)
        self.event = code is None

class LocationData(NamedTuple):
    name: str
    clearance: str
    region: str

locations_data = [
	LocationData(name='Vermillion Wasteland - Spiral Cliff - Bronze Chest', clearance='Bronze', region='22'),
	LocationData(name='Vermillion Wasteland - Spiral Cliff - Chest', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - Storage Basement - Chest', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - Crimson Lake - Chest 1', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - Crimson Lake - Chest 2', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - East Town - Silver Chest', clearance='Silver', region='22'),
	LocationData(name='Vermillion Wasteland - East Town - Chest 1', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - East Town - Chest 2', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - West Town - Bronze Chest 1', clearance='Bronze', region='22'),
	LocationData(name='Vermillion Wasteland - West Town - Chest', clearance='Default', region='22'),
	LocationData(name='Vermillion Wasteland - West Town - Bronze Chest 2', clearance='Bronze', region='22'),
	LocationData(name="Autumn's Rise - Drippy Den - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Normal Clearing - Chest 1", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Normal Clearing - Chest 2", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Entrance - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Old Observatory - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Quiet Passage 1 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Quiet Passage 2 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Hedgehag's Den - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 1 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 2 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 3 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Off Road 1 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Off Road 2 - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 6 - Chest 1", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 6 - Chest 2", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 6 - Chest 3", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 7 - Chest 1", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 7 - Chest 2", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Ending Pathway - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Obelisk Lake - Bronze Chest", clearance='Bronze', region='3'),
	LocationData(name="Autumn's Rise - Obelisk Lake - Chest", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 4 - Chest 1", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 4 - Chest 2", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 4 - Chest 3", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 5 - Chest 1", clearance='Default', region='3'),
	LocationData(name="Autumn's Rise - Pathway 5 - Chest 2", clearance='Default', region='3'),
	LocationData(name="Autumn's Fall - Ruby Tunnel - Gold Chest", clearance='Gold', region='31'),
	LocationData(name="Autumn's Fall - Lake Cave 1 - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Lake Cave 2 - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Lake Cave 3 - Silver Chest", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Lake Cave 4 - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Southern Exit - Chest 1", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Southern Exit - Chest 2", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Southern Exit - Chest 3", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Ruined Path - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Ruined Path - Gold Chest", clearance='Gold', region='20'),
	LocationData(name="Autumn's Fall - Eastern Exit - Silver Chest", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Eastern Exit - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Ancient Center - Silver Chest 1", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Ancient Center - Silver Chest 2", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Northern Exit - Chest", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Northern Exit - Bronze Chest", clearance='Bronze', region='20'),
	LocationData(name="Autumn's Fall - Pillar Isle - Chest 1", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Pillar Isle - Chest 2", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Pillar Isle - Chest 3", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Village Remains - Silver Chest", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Village Remains - Gold Chest", clearance='Gold', region='20'),
	LocationData(name="Autumn's Fall - Village Remains - Bronze Chest", clearance='Bronze', region='20'),
	LocationData(name="Autumn's Fall - Secluded Path - Gold Chest", clearance='Gold', region='20'),
	LocationData(name="Autumn's Fall - Secluded Path - Chest 1", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Secluded Path - Chest 2", clearance='Default', region='20'),
	LocationData(name="Autumn's Fall - Villa of Terror - Silver Chest", clearance='Silver', region='20'),
	LocationData(name="Autumn's Fall - Villa of Terror - Bronze Chest", clearance='Bronze', region='20'),
	LocationData(name="Autumn's Fall - Para Island 1 - Chest", clearance='Default', region='21'),
	LocationData(name='Bergen Village - Bergen South - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Bergen South - Bronze Chest 1', clearance='Bronze', region='3'),
	LocationData(name='Bergen Village - Bergen South - Bronze Chest 2', clearance='Bronze', region='3'),
	LocationData(name='Bergen Village - Bergen South - Gold Chest', clearance='Gold', region='3'),
	LocationData(name='Bergen Village - Bergen North - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Bergen North - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Bergen North - Silver Chest', clearance='Silver', region='3'),
	LocationData(name='Bergen Village - Bergen North - Chest 3', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Diving Railway - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Seeker Hub Cellar - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Village - Seeker Hub Cellar - Bronze Chest', clearance='Bronze', region='3'),
	LocationData(name='Bergen Village - Storage Room - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Abandoned Cave  - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Frozen Cave - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Abandoned Ground - Silver Chest', clearance='Silver', region='3'),
	LocationData(name="Bergen Trail - Pengpeng's Den - Chest", clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Entrance - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Entrance - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 1 - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 1 - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 1 - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 2 - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 2 - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 2 - Chest 3', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 3 - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Off Road 3 - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Old Plateau - Gold Chest', clearance='Gold', region='3'),
	LocationData(name='Bergen Trail - Rising Path 2 - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 3 - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 3 - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Spike Heights - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Spike Heights - Bronze Chest', clearance='Bronze', region='3'),
	LocationData(name='Bergen Trail - Icy Cauldron - Silver Chest', clearance='Silver', region='3'),
	LocationData(name='Bergen Trail - Bergen Waterfalls - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 4 - Chest 1', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 4 - Chest 2', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Lofty Heights - Bronze Chest', clearance='Bronze', region='3'),
	LocationData(name='Bergen Trail - Windy Climb - Chest', clearance='Default', region='3'),
	LocationData(name='Bergen Trail - Rising Path 5 - Chest', clearance='Default', region='3'),
	LocationData(name='Temple Mine - Elevator - Chest', clearance='Default', region='5'),
	LocationData(name='Temple Mine - Crossing Funnel - Chest', clearance='Default', region='5'),
	LocationData(name='Temple Mine - Old Shaft 1 - Chest', clearance='Default', region='5'),
	LocationData(name='Temple Mine - Old Shaft 2 - Chest', clearance='Default', region='5'),
	LocationData(name='Temple Mine - Testing Chamber - Chest', clearance='Default', region='5'),
	LocationData(name='Temple Mine - Old Chamber - Chest', clearance='Default', region='6'),
	LocationData(name='Temple Mine - Storage Room 1 - Bronze Chest', clearance='Bronze', region='7'),
	LocationData(name='Temple Mine - Frozen Chamber 1 - Chest', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Frozen Chamber 2 - Bronze Chest 1', clearance='Bronze', region='9'),
	LocationData(name='Temple Mine - Frozen Chamber 2 - Bronze Chest 2', clearance='Bronze', region='9'),
	LocationData(name='Temple Mine - Frozen Shaft 1 - Chest', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Frozen Shaft 2 - Chest', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Frozen Shaft 3 - Chest', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Frozen Shaft 3 - Bronze Chest', clearance='Bronze', region='7'),
	LocationData(name='Temple Mine - Overrun Chamber - Chest 1', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Overrun Chamber - Chest 2', clearance='Default', region='7'),
	LocationData(name='Temple Mine - Elevator - Chest', clearance='Default', region='9'),
	LocationData(name='Temple Mine - Infested Chamber - Chest', clearance='Default', region='10'),
	LocationData(name='Temple Mine - Forgotten Shaft 1 - Chest', clearance='Default', region='9'),
	LocationData(name='Temple Mine - Forgotten Shaft 2 - Bronze Chest', clearance='Bronze', region='9'),
	LocationData(name='Temple Mine - Forgotten Shaft 3 - Chest', clearance='Default', region='9'),
	LocationData(name='Temple Mine - Forgotten Shaft 4 - Chest', clearance='Default', region='9'),
	LocationData(name='Temple Mine - Forgotten Shaft 5 - Chest', clearance='Default', region='9'),
	LocationData(name='Temple Mine - Elevator - Bronze Chest', clearance='Bronze', region='4'),
	LocationData(name='Temple Mine - Temple Chamber 2 - Chest', clearance='Default', region='4'),
	LocationData(name='Sapphire Ridge - The Barracks - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - The Bellow - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Sapphire Tunnel - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Eroded Passage - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Eroded Passage - Chest', clearance='Default', region='31'),
	LocationData(name='Sapphire Ridge - Spider Chasm - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - Spider Chasm - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Narrow Passage - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Narrow Passage - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - Wheel Passage - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Wheel Passage - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - Cave Inn 1F - Chest', clearance='Default', region='31'),
	LocationData(name='Sapphire Ridge - Cave Inn Storage - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Western Exit - Chest', clearance='Default', region='31'),
	LocationData(name='Sapphire Ridge - Western Exit - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - North West Path - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - North West Path - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - River Road - Bronze Chest 1', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - River Road - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - River Road - Bronze Chest 2', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - The Cave Inn - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - The Cave Inn - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Tranquil Bamboo - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - Tranquil Bamboo - Chest', clearance='Default', region='31'),
	LocationData(name='Sapphire Ridge - Bamboo Thicket - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Bamboo Thicket - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - North East Path - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - North East Path - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Flower Lake - Gold Chest 1', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Flower Lake - Gold Chest 2', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Carved Pathway - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Carved Pathway - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Carved Pathway - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Sapphire Ridge - High Ground - Gold Chest', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - High Ground - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Old Dojo - Silver Chest', clearance='Silver', region='31'),
	LocationData(name='Sapphire Ridge - Old Dojo - Gold Chest 1', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Old Dojo - Gold Chest 2', clearance='Gold', region='31'),
	LocationData(name='Sapphire Ridge - Dream Pond - Gold Chest', clearance='Gold', region='33'),
	LocationData(name='Sapphire Ridge - Ascension Temple - Gold Chest', clearance='Gold', region='33'),
	LocationData(name='Sapphire Ridge - Ascension Temple - Silver Chest 1', clearance='Silver', region='33'),
	LocationData(name='Sapphire Ridge - Ascension Temple - Silver Chest 2', clearance='Silver', region='33'),
	LocationData(name='Sapphire Ridge - Baton Pond - Bronze Chest', clearance='Bronze', region='31'),
	LocationData(name='Maroon Valley - Mystery Cave - Gold Chest', clearance='Gold', region='11'),
	LocationData(name='Maroon Valley - Mystery Cave - Silver Chest', clearance='Silver', region='11'),
	LocationData(name='Maroon Valley - Maroon Cave 1 - Chest', clearance='Default', region='12'),
	LocationData(name='Maroon Valley - River Cliff - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - River Cliff - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Endless Pit - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Endless Pit - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Endless Pit - Chest 3', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Vivid Path - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Vivid Path - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Maroon Oasis - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Maroon Oasis - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Bright Path - Bronze Chest', clearance='Bronze', region='11'),
	LocationData(name='Maroon Valley - Rising Railway - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - East Entrance - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Dusty Path - Bronze Chest', clearance='Bronze', region='11'),
	LocationData(name='Maroon Valley - Dusty Path - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Crossroad - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Crossroad - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Long Piece - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Barren Arcs - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Barren Arcs - Bronze Chest', clearance='Bronze', region='11'),
	LocationData(name='Maroon Valley - Barren Land - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Overpass - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Overpass - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Paw Cliffs - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Paw Cliffs - Silver Chest', clearance='Silver', region='11'),
	LocationData(name='Maroon Valley - Torn Road - Chest 1', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Torn Road - Chest 2', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - West Entrance - Chest', clearance='Default', region='11'),
	LocationData(name='Maroon Valley - Fractured Path - Silver Chest', clearance='Silver', region='11'),
	LocationData(name='Maroon Valley - Fractured Path - Chest', clearance='Default', region='11'),
	LocationData(name="Faj'ro Temple - Right Chamber 1 - Chest", clearance='Default', region='15'),
	LocationData(name="Faj'ro Temple - Bottom Chamber - Chest", clearance='Default', region='17'),
	LocationData(name="Faj'ro Temple - Large Fire Chamber - Bronze Chest", clearance='Bronze', region='17.5'),
	LocationData(name="Faj'ro Temple - Large Fire Chamber - Silver Chest", clearance='Silver', region='17.5'),
	LocationData(name="Faj'ro Temple - Test of Wisdom - Chest", clearance='Default', region='17.5'),
	LocationData(name="Faj'ro Temple - West Pathway - Chest", clearance='Default', region='17'),
	LocationData(name="Faj'ro Temple - Test of Surprise - Chest", clearance='Default', region='17'),
	LocationData(name="Faj'ro Temple - West Chamber 1 - Chest", clearance='Default', region='17.5'),
	LocationData(name="Faj'ro Temple - East Chamber 1 - Chest", clearance='Default', region='17.5'),
	LocationData(name="Faj'ro Temple - East Pathway - Silver Chest", clearance='Silver', region='17'),
	LocationData(name="Faj'ro Temple - Test of Memory - Chest", clearance='Default', region='17.5'),
	LocationData(name="Faj'ro Temple - Chamber of Prosperity - Chest", clearance='Default', region='18'),
	LocationData(name="Faj'ro Temple - Left Chamber 1 - Chest", clearance='Default', region='13'),
	LocationData(name="Faj'ro Temple - Fire and Sand 2 - Chest", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Balance Room 2 - Chest 1", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Balance Room 2 - Chest 2", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Right Chamber 1 - Chest", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Right Chamber 2 - Chest", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Test of Memory 1 - Chest", clearance='Default', region='14'),
	LocationData(name="Faj'ro Temple - Test of Memory 2 - Chest", clearance='Default', region='14'),
	LocationData(name="Ba'kii Kum - Solar Farm - Chest 1", clearance='Default', region='11'),
	LocationData(name="Ba'kii Kum - Solar Farm - Chest 2", clearance='Default', region='11'),
	LocationData(name="Ba'kii Kum - Market - Chest", clearance='Default', region='11'),
	LocationData(name="Ba'kii Kum - Market - Bronze Chest", clearance='Bronze', region='11'),
	LocationData(name="Ba'kii Kum - Bazaar House - Silver Chest", clearance='Silver', region='11'),
	LocationData(name="Gaia's Garden - Dripping Cave - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Tranquility Pond - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil West - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil West - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil West - Bronze Chest", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil East - Bronze Chest", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil East - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil North - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - V'rda Vil North - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Chief's Den - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Chief's Den - Bronze Chest", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - Chief's Den - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - Grand Krys'kajo Entrance - Bronze Chest", clearance='Bronze', region='28'),
	LocationData(name="Gaia's Garden - So'najiz Temple Entrance - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Covert Path - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Covert Path - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Royal Grove - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Royal Grove - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Royal Grove - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Royal Grove - Chest 3", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Calm Backyard - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Calm Backyard - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Lost Lookout - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Lost Lookout - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Lost Lookout - Chest 3", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Seared Lake - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Seared Lake - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes South - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes South - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes South - Chest 3", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes South - Chest 4", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes North - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes North - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes North - Silver Chest 1", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Infested Marshes North - Silver Chest 2", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Overgrown Path - Bronze Chest 1", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - Overgrown Path - Bronze Chest 2", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - Drizzle Bosk - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - Drizzle Bosk - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Drizzle Bosk - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Wet Passage - Bronze Chest", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - Wet Passage - Chest", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - River's Bed - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - River's Bed - Chest", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Jungle Entrance - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Jungle Entrance - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Crossroad - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - Crossroad - Chest", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Tying Greens - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Tying Greens - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Peridot Approach - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Peridot Approach - Chest", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Splitting Stumps - Chest 1", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Splitting Stumps - Chest 2", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Clinging River - Silver Chest", clearance='Silver', region='23'),
	LocationData(name="Gaia's Garden - Clinging River - Gold Chest", clearance='Gold', region='23'),
	LocationData(name="Gaia's Garden - Ringing River - Bronze Chest", clearance='Bronze', region='23'),
	LocationData(name="Gaia's Garden - Ringing River - Chest", clearance='Default', region='23'),
	LocationData(name="Gaia's Garden - Old Timber - Chest", clearance='Default', region='23'),
	LocationData(name='Basin Keep - Centrum - Gold Chest', clearance='Gold', region='24'),
	LocationData(name='Basin Keep - Pond Slums - Silver Chest 1', clearance='Silver', region='24'),
	LocationData(name='Basin Keep - Pond Slums - Silver Chest 2', clearance='Silver', region='24'),
	LocationData(name='Basin Keep - Pond Slums - Gold Chest', clearance='Gold', region='24'),
	LocationData(name="Gaia's Garden - Basin Keep Entrance - Chest", clearance='Default', region='23'),
	LocationData(name='Basin Keep - Basin Police Force HQ - Gold Chest', clearance='Gold', region='23'),
	LocationData(name='Basin Keep - Seeker Hub 1st Floor - Silver Chest', clearance='Silver', region='23'),
	LocationData(name='Rhombus Dungeon - Ability Room 1 - Chest 1', clearance='Default', region='1'),
	LocationData(name='Rhombus Dungeon - Ability Room 1 - Chest 2', clearance='Default', region='1'),
	LocationData(name='Rhombus Square - Arena Plaza - Bronze Chest', clearance='Bronze', region='33'),
	LocationData(name='Rhombus Square - Arena Plaza - Silver Chest', clearance='Silver', region='33'),
	LocationData(name='Rhombus Square - Garden Boulevard - Bronze Chest', clearance='Bronze', region='33'),
	LocationData(name='Rhombus Square - Garden Boulevard - Silver Chest', clearance='Silver', region='33'),
	LocationData(name='Rhombus Square - South Arch - Gold Chest', clearance='Gold', region='33'),
	LocationData(name='Rhombus Square - Lloyd Passage - Silver Chest', clearance='Silver', region='33'),
	LocationData(name='Rookie Harbor - Marketplace - Chest', clearance='Default', region='2'),
	LocationData(name='Rookie Harbor - Falling Exit - Chest', clearance='Default', region='2'),
	LocationData(name='Rookie Harbor - Weapon & Backer Shop - Silver Chest', clearance='Silver', region='19'),
	LocationData(name='Rookie Harbor - Dusty Storage - Silver Chest', clearance='Silver', region='19'),
	LocationData(name='Rookie Harbor - South Harbor - Gold Chest', clearance='Gold', region='2'),
	LocationData(name='Rookie Harbor - Beginners Arc - Chest 1', clearance='Default', region='2'),
	LocationData(name='Rookie Harbor - Beginners Arc - Chest 2', clearance='Default', region='2'),
	LocationData(name="Zir'vitar Temple - Moving Transmit - Chest 1", clearance='Default', region='23'),
	LocationData(name="Zir'vitar Temple - Moving Transmit - Chest 2", clearance='Default', region='25'),
	LocationData(name="Zir'vitar Temple - Haunted Waves - Bronze Chest", clearance='Bronze', region='25'),
	LocationData(name="Zir'vitar Temple - Hoodwink - Chest", clearance='Default', region='23'),
	LocationData(name="Zir'vitar Temple - Spinning Transmit - Bronze Chest", clearance='Bronze', region='25'),
	LocationData(name="Grand Krys'kajo - East Branch - Gold Chest", clearance='Gold', region='28'),
	LocationData(name="Grand Krys'kajo - East Branch - Chest 1", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - East Branch - Chest 2", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - West Branch - Chest 1", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - West Branch - Chest 2", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - Falling Leaves - MasterKey Chest", clearance='MasterKey', region='29'),
	LocationData(name="Grand Krys'kajo - Branch Conveyance - Chest", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - Branch Transmit - Chest 1", clearance='Default', region='28'),
	LocationData(name="Grand Krys'kajo - Branch Transmit - Chest 2", clearance='Default', region='28'),
	LocationData(name="So'najiz Temple - Principle of Conveyance - Chest", clearance='Default', region='23'),
	LocationData(name="So'najiz Temple - Trial of Persistence - Chest 1", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Trial of Persistence - Chest 2", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Trial of Persistence - Chest 3", clearance='Default', region='23'),
	LocationData(name="So'najiz Temple - Trial of Persistence - Silver Chest", clearance='Silver', region='26'),
	LocationData(name="So'najiz Temple - Trial of Persistence - Gold Chest", clearance='Gold', region='26'),
	LocationData(name="So'najiz Temple - Moving Attraction - Chest", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Slowing Attraction - Chest", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Standing Attraction - Chest", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Attracting Conveyance - Chest", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Fast Conveyance - Chest", clearance='Default', region='26'),
	LocationData(name="So'najiz Temple - Flaming Conveyance - Chest", clearance='Default', region='26')
]