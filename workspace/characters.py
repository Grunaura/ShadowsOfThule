class Character:
    def __init__(self, name, health, inventory, alignment, location, dialogue):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.alignment = alignment  # good, evil, neutral
        self.location = location
        self.dialogue = dialogue
        self.alive = True

    def greet(self):
        return f"Hello, I am {self.name}. I am on the {self.alignment} side."

    def is_alive(self):
        return self.alive

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            self.health = 0

    def speak(self):
        return self.dialogue


class Enemy(Character):
    def __init__(self, name, health, inventory, damage, location, dialogue, alignment="evil"):
        super().__init__(name, health, inventory, alignment, location, dialogue)
        self.damage = damage

    def attack(self, target):
        target.take_damage(self.damage)
        return f"{self.name} attacks {target.name} for {self.damage} damage!"


class Ally(Character):
    def __init__(self, name, health, inventory, help_text, location, dialogue, alignment="good"):
        super().__init__(name, health, inventory, alignment, location, dialogue)
        self.help_text = help_text

    def provide_help(self):
        return f"{self.name} says: {self.help_text}"


# Create characters with their respective locations and dialogues
caelum = Ally("Caelum", 100, [], "I possess extensive knowledge of the ancient civilization.", "Royal Library", "The secrets of the lost civilization shall be unraveled under my guidance!")
eris = Ally("Eris", 100, [], "My unparalleled combat skills and mastery of magic make me an unstoppable force.", "Warrior's Stronghold", "With sword and spell, justice shall prevail!")
vexis = Enemy("Lord Vexis", 120, [], 15, "Shadow Keep", "Your futile attempts to uncover the ancient secrets will only lead to your demise!")
informant1 = Enemy("Hepzibah", 80, [], 10, "Hidden Library", "My allegiance lies with Lord Vexis. Your every discovery shall be reported!", alignment="neutral")
informant2 = Enemy("Algernon", 80, [], 10, "Scholar's Retreat", "Rumors of your endeavors have reached my ears. Lord Vexis will be delighted!", alignment="neutral")
spy1 = Enemy("Phineas", 90, [], 12, "Underground Lair", "Your every move is being meticulously observed. Lord Vexis shall always have the advantage!", alignment="evil")
spy2 = Enemy("Lavinia", 90, [], 12, "Assassin's Hideout", "Lord Vexis demands your swift demise. Prepare to meet your untimely end!", alignment="evil")
hero1 = Ally("Gallant", 100, [], "I stand ready to assist you!", "Castle Stronghold", "Hail, noble adventurer! I am Gallant, ever loyal to our cause!")
villain1 = Enemy("Malachi", 100, [], 10, "Dark Citadel", "Tremble before the might of Malachi! True fear shall consume your heart!")
ally1 = Ally("Valeria", 80, [], "My expertise in combat is at your disposal.", "Frostholm Village", "Together, we shall triumph over any adversity!")
ally2 = Ally("Seraphine", 75, [], "My vast knowledge shall aid you in your quests.", "Academy of Wisdom", "Wisdom and courage shall guide our path to victory!")
villain2 = Enemy("Grimgor", 60, [], 8, "Shadow Caverns", "Behold the might of Grimgor, the harbinger of darkness!", alignment="evil")
ally3 = Ally("Braveheart", 80, [], "With unwavering loyalty, I shall fight alongside you.", "Warrior's Camp", "Fear not, for Braveheart shall stand as your shield!")
ally4 = Ally("Zephyrus", 70, [], "As master of the skies, I bring strategic advantage.", "Aerie Heights", "Take flight with me, and victory shall be ours to claim!")
ally5 = Ally("Ironclad", 80, [], "I shall shatter all obstacles with indomitable strength.", "Ironforge Fortress", "No barrier shall endure against the might of Ironclad!")
villain3 = Enemy("Vex'Nor", 70, [], 10, "Shadowed Ruins", "Tremble before the dark powers of Vex'Nor!", alignment="evil")
villain4 = Enemy("Lysandra", 60, [], 10, "Enchantress Tower", "The magic within me shall consume all of Elysium!", alignment="evil")
ally6 = Ally("Keeneye", 80, [], "My keen vision detects hidden dangers from afar.", "Woodland Outpost", "Ever watchful, I shall ensure our safety.")
ally7 = Ally("Bumblethorn", 75, [], "As a defender of the realm, I can aid with bee-related challenges.", "Beehive Grove", "In unity with the bees, we shall overcome all obstacles!")
ally8 = Ally("Morphius", 80, [], "I possess the power to shape-shift and deceive our foes.", "Shadowhaven Sanctum", "Through myriad forms, we shall emerge victorious!")
villain5 = Enemy("Dreadheart", 100, [], 12, "Twilight Keep", "I am the embodiment of your darkest nightmares! Dreadheart reigns supreme!", alignment="evil")
ally9 = Ally("Thornwhisper", 85, [], "I blend into nature's embrace, enabling stealth and subterfuge.", "Whispering Woods", "Nature's embrace conceals our every move.")
villain6 = Enemy("Arachnon", 70, [], 10, "Webbed Depths", "Escape from my intricate web? Impossible!", alignment="evil")
ally10 = Ally("Warden Reginald", 70, [], "As the noble ruler, I have knowledge and resources at our disposal.", "Royal Citadel", "With honor and wisdom, I lead our cause!")
ally11 = Ally("Lady Elara", 70, [], "As the wise councilor, my guidance shall illuminate our path.", "Chamber of Wisdom", "Never underestimate the power of compassion and wisdom.")
ally12 = Ally("Aurora", 90, [], "I am the mystical guardian, imbued with the essence of ancient magic.", "Sanctum of Mysteries", "Harness the magic within you, and all shall be possible!")
ally13 = Ally("Eldric", 100, [], "In the absence of the hero, I shall provide aid and guidance.", "Hall of Heroes", "By the ancient oaths, I answer your call!")
villain7 = Enemy("Slaughterbane", 75, [], 10, "Bloodthorn Arena", "No whip can match the fury of Slaughterbane!", alignment="evil")
villain8 = Enemy("Venomstrike", 70, [], 8, "Poisoned Marsh", "Feel the venom coursing through your veins! You are powerless against Venomstrike!", alignment="evil")
villain9 = Enemy("Nightshade", 80, [], 10, "Cursed Crypts", "Your darkest fears shall nourish Nightshade's power!", alignment="evil")
neutral1 = Character("Equinox", 90, [], "I maintain the delicate balance of the cosmos.", "Astral Sanctum", "I am Equinox, guardian of cosmic harmony.", alignment="neutral")
ally14 = Ally("Whirlwind", 80, [], "I summon the cyclone's might, tearing through our enemies.", "Tempest Spire", "The storm's wrath is at our command! Unleash the fury of the whirlwind!")

characters = [caelum, eris, vexis, informant1, informant2, spy1, spy2, hero1, villain1, ally1, ally2, villain2, ally3, ally4, ally5, villain3, villain4, ally6, ally7, ally8, villain5, ally9, villain6, ally10, ally11, ally12, ally13, villain7, villain8, villain9, neutral1, ally14]