from faker import Faker
import random
import string

fake = Faker()

class NameGenerator:

    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = [ch for ch in string.ascii_lowercase if ch not in self.vowels]

        self.prefixes = {
        'continent': ['South', 'North', 'West', 'East', 'Western', 'Eastern'],
        'country': ['South', 'North', 'West', 'East', 'Western', 'Eastern'],
        'state': ['South', 'North', 'West', 'East', 'Western', 'Eastern'],
        'mountain': ['Mount', 'Mt.', 'Pico', 'Massif'],
        'lake': ['Lake', 'Lago', 'Mar'],
        'sea': ['Mar'],
        'castle': ['Castle', 'Chateau', 'Schloss', 'Burg', 'Fort'],
        'general': ['The', 'Grand', 'Old', 'New']
    }
        self.suffixes = {
        'continent': ['major', 'minor'],    
        'mountain': ['Peak', 'Ridge', 'Pass', 'Summit', 'Crest', 'Top', 'Point'],
        'river': ['River', 'Stream', 'Creek', 'Brook', 'Riviera', 'Fjord'],
        'forest': ['Woods', 'Forest', 'Groves', 'Thicket', 'Copse', 'Stand'],
        'swamp': ['Swamp', 'Marsh', 'Bog', 'Fen', 'Mire', 'Wetlands'],
        'desert': ['Desert', 'Wastes', 'Expanse', 'Sands', 'Dunes'],
        'island': ['Island', 'Isle', 'Isle of', 'Archipelago', 'Cay', 'Atoll'],
        'ocean': ['Ocean', 'Sea', 'Bay', 'Gulf', 'Harbor', 'Strait', 'Channel'],
        'building': ['Building', 'Tower', 'Hall', 'Palace', 'Manor', 'Mansion', 'Fortress'],
        'city': ['City', 'Metropolis', 'Capital', 'Haven', 'ville', 'burg'],
        'province': ['Province', 'County', 'Region', 'Territory', 'Shire'],
        'state': ['State', 'Commonwealth', 'Republic'],
        'village': ['Village', 'Hamlet', 'Settlement'],
        'town': ['Town', 'Borough', 'Township', 'ton'],
        'landmark': ['Monument', 'Memorial', 'Statue', 'Obelisk', 'Pillar', 'Column'],
        'dungeon': ['Dungeon', 'Crypt', 'Vault', 'Labyrinth', 'Catacombs', 'Cavern', 'Caverns', 'Den'],
        'castle': ['Castle', 'Fort', 'Keep', 'Tower', 'Palace', 'Spire', 'Stronghold', 'Citadel', 'Bastion', 'Burg', 'Chateau', 'Schloss'],
    }
        self.characteristics = {
        'general': ['Broad', 'Tall', 'Grand', 'Majestic', 'Mighty', 'Ancient', 'Brilliant', 'Colossal', 'Dazzling', 'Enormous', 'Gigantic', 'Golden', 'Haunting', 'Immense', 'Jagged', 'Lush', 'Mystical', 'Narrow', 'Ominous', 'Pristine', 'Quaint', 'Radiant', 'Secluded', 'Turquoise', 'Unspoiled', 'Vibrant', 'Winding', 'Xenophilic', 'Yielding', 'Zenithal']
    }

        self.first_names = [name for name in dir(Faker()) if "first_name" in name]
        
    def generate_syllable(self):
        syllable = random.choice(self.consonants) + random.choice(self.vowels)
        if random.choice([True, False]):  # With 50% chance add a trailing consonant
            syllable += random.choice(self.consonants)
        return syllable

    def generate_fantasy_name(self, syllable_count=2):
        name = ''.join(self.generate_syllable() for _ in range(syllable_count))
        return name.capitalize()

    def generate_single_word_name(self):
        return fake.word().capitalize()

    def generate_two_part_name(self):
        characteristic = random.choice(self.characteristics)
        name = fake.word().capitalize()
        return f"{characteristic} {name}"

    def generate_possessive_name(self):
        first_name_func = random.choice(self.first_names)
        first_name = getattr(fake, first_name_func)().capitalize()
        suffix = random.choice(self.suffixes)
        return f"{first_name}'s {suffix}"

    def generate_non_english_name(self):
        return fake.words(nb=1, ext_word_list=None, unique=False)[0].capitalize()

    def generate_prefixed_name(self):
        prefix = random.choice(self.prefixes)
        name = fake.word().capitalize()
        return f"{prefix} {name}"

def generate_continent_name(self):
    # select a random method for name generation
    generator = random.choice([self.generate_single_word_name,
                               self.generate_two_part_name,
                               self.generate_possessive_name,
                               self.generate_non_english_name,
                               self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['continent'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['continent'])
        name = f"{name} {suffix}"

    
def generate_mountain_name(self):
    # select a random method for name generation
    generator = random.choice([self.generate_single_word_name,
                               self.generate_two_part_name,
                               self.generate_possessive_name,
                               self.generate_non_english_name,
                               self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['mountain'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['mountain'])
        name = f"{name} {suffix}"

    return name

def generate_river_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['river'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['river'])
        name = f"{name} {suffix}"

    return name

def generate_state_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['state'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['state'])
        name = f"{name} {suffix}"

    return name

def generate_forest_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['forest'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['forest'])
        name = f"{name} {suffix}"

    return name

def generate_country_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['country'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['country'])
        name = f"{name} {suffix}"

    return name

def generate_swamp_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['swamp'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['swamp'])
        name = f"{name} {suffix}"

    return name

def generate_desert_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['desert'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['desert'])
        name = f"{name} {suffix}"

    return name

def generate_lake_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['lake'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['lake'])
        name = f"{name} {suffix}"

    return name

def generate_island_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['island'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['island'])
        name = f"{name} {suffix}"

    return name

def generate_ocean_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['ocean'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['ocean'])
        name = f"{name} {suffix}"

    return name


    
def generate_building_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['building'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['building'])
        name = f"{name} {suffix}"

    return name


    
def generate_city_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['city'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['city'])
        name = f"{name} {suffix}"

    return name

def generate_province_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['province'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['province'])
        name = f"{name} {suffix}"

    return name

def generate_landmark_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['landmark'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['landmark'])
        name = f"{name} {suffix}"

    return name

def generate_castle_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['castle'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['castle'])
        name = f"{name} {suffix}"

    return name


    
def generate_dungeon_name(self):
    generator = ([self.generate_single_word_name,
                   self.generate_two_part_name,
                   self.generate_possessive_name,
                   self.generate_non_english_name,
                   self.generate_prefixed_name])
    name = generator()

    # only 30% chance to add prefix or suffix, never both
    chance = random.randint(1, 100)
    if chance <= 20: # 20% chance to add a prefix
        prefix = random.choice(self.prefixes['dungeon'])
        name = f"{prefix} {name}"
    elif chance <= 45: # 45% chance to add a suffix
        suffix = random.choice(self.suffixes['dungeon'])
        name = f"{name} {suffix}"

    return name



name_generator = NameGenerator()
for i in range(10):
    print(name_generator.generate_mountain_name())


    def generate_river_name(self):
        return "The " + self.generate_fantasy_name() + " River"

    def generate_continent_name(self):
        return self.generate_fantasy_name()

    def generate_forest_name(self):
        return self.generate_fantasy_name() + " Woods"

    def generate_country_name(self):
        return self.generate_fantasy_name()

    def generate_Swamp_name(self):
        return self.generate_fantasy_name() + " Swamp"

    def generate_desert_name(self):
        return self.generate_fantasy_name() + " Desert"

    def generate_lake_name(self):
        return "Lake " + self.generate_fantasy_name()

    def generate_island_name(self):
        return self.generate_fantasy_name() + " Island"

    def generate_ocean_name(self):
        return "The " + self.generate_fantasy_name() + " Ocean"

    def generate_building_name(self):
        return self.generate_fantasy_name() + " Building"

    def generate_city_name(self):
        return self.generate_fantasy_name() + " City"

    def generate_province_name(self):
        return self.generate_fantasy_name() + " Province"

    def generate_landmark_name(self):
        return "The " + self.generate_fantasy_name() + " Monument"

    def generate_castle_name(self):
        return "Castle " + self.generate_fantasy_name()

    def generate_dungeon_name(self):
        return "The " + self.generate_fantasy_name() + " Dungeon"

    def generate_name(self, name_type):
        if name_type == "fantasy":
            return self.generate_fantasy_name()
        elif name_type == "continent":
            return self.generate_continent_name()
        elif name_type == "country":
            return self.generate_country_name()
        elif name_type == "swamp":
            return self.generate_swamp_name()
        elif name_type == "state":
            return self.generate_state_name()
        elif name_type == "mountain":
            return self.generate_mountain_name()
        elif name_type == "river":
            return self.generate_river_name()
        elif name_type == "forest":
            return self.generate_forest_name()
        elif name_type == "desert":
            return self.generate_desert_name()
        elif name_type == "lake":
            return self.generate_lake_name()
        elif name_type == "island":
            return self.generate_island_name()
        elif name_type == "ocean":
            return self.generate_ocean_name()
        elif name_type == "building":
            return self.generate_building_name()
        elif name_type == "city":
            return self.generate_city_name()
        elif name_type == "province":
            return self.generate_province_name()
        elif name_type == "landmark":
            return self.generate_landmark_name()
        elif name_type == "castle":
            return self.generate_castle_name()
        elif name_type == "dungeon":
            return self.generate_dungeon_name()
        else:
            return fake.first_name()

name_generator = NameGenerator()
print(name_generator.generate_name("continent"))  # Generates a continent name
print(name_generator.generate_name("country"))  # Generates a country name
print(name_generator.generate_name("swamp"))  # Generates a swamp name
print(name_generator.generate_name("state"))  # Generates a state name
print(name_generator.generate_name("mountain"))  # Generates a mountain name
print(name_generator.generate_name("river"))  # Generates a river name
print(name_generator.generate_name("forest"))  # Generates a forest name
print(name_generator.generate_name("desert"))  # Generates a desert name
print(name_generator.generate_name("lake"))  # Generates a lake name
print(name_generator.generate_name("island"))  # Generates an island name
print(name_generator.generate_name("ocean"))  # Generates an ocean name
print(name_generator.generate_name("building"))  # Generates a building name
print(name_generator.generate_name("city"))  # Generates a city name
print(name_generator.generate_name("province"))  # Generates a province name
print(name_generator.generate_name("landmark"))  # Generates a landmark name
print(name_generator.generate_name("castle"))  # Generates a castle name
print(name_generator.generate_name("dungeon"))  # Generates a dungeon name
print(name_generator.generate_name("fantasy"))  # Generates a fantasy name