# combat_controller.py
import random

class CombatController:
    @staticmethod
    def validate_character(character):
        # Validation code here
        if character is None or not all(hasattr(character, attr) for attr in ['attack_bonus', 'damage_bonus', 'weapon', 'armor_class', 'health']):
            raise ValueError('Invalid character')

    @staticmethod
    def roll_die(sides):
        # Roll die code here
        return random.randint(1, sides)

    @staticmethod
    def attack(attacker, defender):
        # Attack simulation code here
        roll = CombatController.roll_die(20) + attacker.attack_bonus
        if roll >= defender.armor_class:
            damage = CombatController.roll_die(attacker.weapon.damage_die) + attacker.damage_bonus
            defender.health -= damage
            print(f"{attacker.name} hits {defender.name} for {damage} damage.")
        else:
            print(f"{attacker.name}'s attack misses.")

    @staticmethod
    def engage_combat(player, enemy):
        # Combat engagement code here
        print(f"A wild {enemy.name} appears!")
        while player.health > 0 and enemy.health > 0:
            CombatController.attack(player, enemy)
            if enemy.health <= 0:
                print(f"You have defeated {enemy.name}!")
                break
            CombatController.attack(enemy, player)
            if player.health <= 0:
                print("You have been defeated...")
                break
