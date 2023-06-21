#combat.py

from combat_controller import CombatController
import random


class Combat:
    @staticmethod
    def validate_character(character):
        """
        Validate the character object
        """
        if character is None or not all(hasattr(character, attr) for attr in ['attack_bonus', 'damage_bonus', 'weapon', 'armor_class', 'health']):
            raise ValueError('Invalid character')

    @staticmethod
    def roll_die(sides):
        """
        Simulate a roll of a die with the specified number of sides.
        """
        return random.randint(1, sides)

    @staticmethod
    def attack(attacker, defender):
        """
        Simulate an attack from the attacker to the defender.
        """
        # Validate the characters
        Combat.validate_character(attacker)
        Combat.validate_character(defender)

        # Roll a d20 to determine if the attack hits
        roll = Combat.roll_die(20) + attacker.attack_bonus
        if roll >= defender.armor_class:
            # The attack hits
            # Roll a die to determine damage
            damage = Combat.roll_die(attacker.weapon.damage_die) + attacker.damage_bonus
            # Apply special ability damage if available
            if attacker.weapon.special_ability:
                special_damage = Combat.roll_die(attacker.weapon.special_ability['damage_die'])
                damage += special_damage
                print(f"{attacker.name} hits {defender.name} with special ability {attacker.weapon.special_ability['name']} for {special_damage} damage.")
            # Apply damage to the defender
            defender.health -= damage
            print(f"{attacker.name} hits {defender.name} for {damage} damage.")
        else:
            # The attack misses
            print(f"{attacker.name}'s attack misses.")

def engage_combat(self, enemy_name):
    enemy = self.player.current_location.get_creature(enemy_name)
    if enemy:
        print(f"A wild {enemy.name} appears!")
        while self.player.health > 0 and enemy.health > 0:
            # Player's turn
            CombatController.attack(self.player, enemy)
            if enemy.health <= 0:
                print(f"You have defeated {enemy.name}!")
                break
            # Enemy's turn
            CombatController.attack(enemy, self.player)
            if self.player.health <= 0:
                print("You have been defeated...")
                break
    else:
        print("There is no such creature here.")
