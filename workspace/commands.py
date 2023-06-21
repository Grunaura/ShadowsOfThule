#commands.py
from . import save_load
from . import controller
from . import combat
from .characters import characters

class Commands:

    def __init__(self, game_state):
        self.game_state = game_state
        self.combat = combat.Combat()
        
    def look(self):
        location = self.game_state.get_player_location()
        return location.get_description()

    def use_item(self, item_name):
        player = self.game_state.get_player()
        item = player.get_item(item_name)
        if item:
            return item.use()
        else:
            return "You don't have that item."

    def move(self, direction):
        if direction in ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest', 'up', 'down']:
            new_location = self.game_state.move_player(direction)
            return new_location.get_description()
        else:
            return "Invalid direction."

    def save(self):
        # Call the save function from save_load module
        save_load.save_game(self.game_state.player)
        return "Game saved."

    def restore(self):
        # Call the load function from save_load module
        self.game_state.player = save_load.load_game()
        return "Game restored."

    def restart(self):
        # Reset the game state in game_state
        self.game_state.reset_state()
        return "Game restarted."

    def verbose(self):
        # Enable verbose mode in game_state
        self.game_state.verbose = True
        return "Verbose mode on."

    def score(self):
        # Fetch score from player object
        return f"Your score is {self.game_state.player.score}."

    def diagnostic(self):
        # Let's assume game_state has a diagnostic method which runs some checks
        result = self.game_state.diagnostic()
        return "Everything seems to be working fine." if result else "Something seems off."

    def brief(self):
        # Enable brief mode in game_state
        self.game_state.brief = True
        return "Brief mode on."

    def superbrief(self):
        # Enable superbrief mode in game_state
        self.game_state.superbrief = True
        return "Superbrief mode on."

    def quit(self):
        # Call game_state's quit method
        self.game_state.quit()
        return "Quitting game."

    def climb(self):
        # Climb command implementation would depend on the game world.
        # If climbing is context-dependent, you'll need to check the player's location, possible actions, etc.
        # For now, let's say that climbing just changes the player's altitude
        self.game_state.player.altitude += 1
        return "You start to climb."

def redo_last_command(self):
    # Redo last command implementation
    if self.game_state.last_command is not None:
        # Recall the last command and parameters used and perform the action
        return getattr(self, self.game_state.last_command[0])(*self.game_state.last_command[1:])
    else:
        return "No previous command to redo."

def go(self, direction):
    # Go command implementation
    return self.move(direction)

def enter(self, place):
    # Enter command implementation
    if self.game_state.get_player_location().name == place:
        return "You're already here."
    else:
        possible_directions = self.game_state.get_player_location().get_exits()
        for direction in possible_directions:
            if possible_directions[direction].name == place:
                return self.move(direction)
        return f"There's no {place} nearby to enter."

def go_in(self, place):
    # Go in command implementation
    return self.enter(place)

def go_out(self):
    # Go out command implementation
    return self.move("out")

def say_hello(self):
    # Say hello command implementation
    return "You say hello. It echoes in the quiet."

def get_item(self, item_name):
    # Get/take/grab command implementation
    item = self.game_state.get_player_location().get_item(item_name)
    if item:
        self.game_state.get_player().add_item(item)
        return f"You have taken the {item_name}."
    else:
        return f"There's no {item_name} here to take."

def get_all_items(self):
    # Get/take/grab all command implementation
    items = self.game_state.get_player_location().get_items()
    for item in items:
        self.game_state.get_player().add_item(item)
    return "You've taken all the items."

def throw_item_at(self, item_name, target):
    # Throw item at command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        self.game_state.get_player().remove_item(item_name)
        return f"You've thrown the {item_name} at the {target}."
    else:
        return f"You don't have a {item_name} to throw."

def open_container(self, container_name):
    # Open container command implementation
    container = self.game_state.get_player_location().get_container(container_name)
    if container:
        return container.open()
    else:
        return f"There's no {container_name} here to open."

def open_exit(self, exit_name):
    # Open exit command implementation
    exit = self.game_state.get_player_location().get_exit(exit_name)
    if exit:
        if exit.is_locked():
            return f"The {exit_name} is locked."
        else:
            return exit.open()
    else:
        return f"There's no {exit_name} here to open."

def read_item(self, item_name):
    # Read command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        if item.is_readable():
            return item.read()
        else:
            return f"You can't read the {item_name}."
    else:
        return f"You don't have a {item_name} to read."

def drop_item(self, item_name):
    # Drop command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        self.game_state.get_player().remove_item(item_name)
        self.game_state.get_player_location().add_item(item)
        return f"You have dropped the {item_name}."
    else:
        return f"You don't have a {item_name} to drop."

def put_item_in_container(self, item_name, container_name):
    # Put command implementation
    item = self.game_state.get_player().get_item(item_name)
    container = self.game_state.get_player_location().get_container(container_name)
    if item and container:
        self.game_state.get_player().remove_item(item_name)
        container.add_item(item)
        return f"You have put the {item_name} in the {container_name}."
    else:
        return f"You don't have a {item_name} to put in the {container_name}."

def turn_control_with_item(self, control_name, item_name):
    # Turn control with item command implementation
    control = self.game_state.get_player_location().get_control(control_name)
    item = self.game_state.get_player().get_item(item_name)
    if control and item:
        return control.turn_with(item)
    else:
        return f"You can't turn the {control_name} with the {item_name}."

def turn_on_item(self, item_name):
    # Turn on item command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        return item.turn_on()
    else:
        return f"You don't have a {item_name} to turn on."

def turn_off_item(self, item_name):
    # Turn off item command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        return item.turn_off()
    else:
        return f"You don't have a {item_name} to turn off."

def move_object(self, object_name):
    # Move object command implementation
    object = self.game_state.get_player_location().get_object(object_name)
    if object:
        return object.move()
    else:
        return f"There's no {object_name} here to move."

def attack_creature_with_item(self, creature_name, item_name):
    # Attack creature with item command implementation
    creature = self.game_state.get_player_location().get_creature(creature_name)
    item = self.game_state.get_player().get_item(item_name)
    if creature and item:
        return self.combat.attack(creature, item)
    else:
        return f"You can't attack the {creature_name} with the {item_name}."

def examine_object(self, object_name):
    # Examine command implementation
    object = self.game_state.get_player_location().get_object(object_name)
    if object:
        return object.examine()
    else:
        return f"There's no {object_name} here to examine."

def show_inventory(self):
    # Inventory command implementation
    return self.game_state.get_player().show_inventory()

def eat_item(self, item_name):
    # Eat command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        if item.is_edible():
            self.game_state.get_player().remove_item(item_name)
            return item.eat()
        else:
            return f"You can't eat the {item_name}."
    else:
        return f"You don't have a {item_name} to eat."

def shout(self):
    # Shout command implementation
    return "You shout loudly. The echo lingers in the air."

def close_door(self, door_name):
    # Close door command implementation
    door = self.game_state.get_player_location().get_door(door_name)
    if door:
        return door.close()
    else:
        return f"There's no {door_name} here to close."

def tie_item_to_object(self, item_name, object_name):
    # Tie item to object command implementation
    item = self.game_state.get_player().get_item(item_name)
    object = self.game_state.get_player_location().get_object(object_name)
    if item and object:
        return object.tie_item(item)
    else:
        return f"You can't tie the {item_name} to the {object_name}."

def pick_item(self, item_name):
    # Pick command implementation
    return self.get_item(item_name)

def kill_self_with_weapon(self, weapon_name):
    # Kill self with weapon command implementation
    weapon = self.game_state.get_player().get_item(weapon_name)
    if weapon:
        return self.combat.self_harm(weapon)
    else:
        return "You don't have the weapon to do this."

def break_item_with_item(self, item_to_break_name, breaking_item_name):
    # Break item with item command implementation
    item_to_break = self.game_state.get_player().get_item(item_to_break_name)
    breaking_item = self.game_state.get_player().get_item(breaking_item_name)
    if item_to_break and breaking_item:
        return item_to_break.break_with(breaking_item)
    else:
        return "You don't have the necessary items to do this."

def attack_creature_with_item(self, creature_name, item_name):
    # Attack creature with item command implementation
    creature = self.game_state.get_player_location().get_creature(creature_name)
    item = self.game_state.get_player().get_item(item_name)
    if creature and item:
        return self.combat.attack(creature, item)
    else:
        return "You can't attack the creature with this item."

def pray(self):
    # Pray command implementation
    return "You start to pray."

def drink_item(self, item_name):
    # Drink command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        if item.is_drinkable():
            self.game_state.get_player().remove_item(item_name)
            return item.drink()
        else:
            return "You can't drink this item."
    else:
        return "You don't have the item to drink."

def smell_item(self, item_name):
    # Smell command implementation
    item = self.game_state.get_player().get_item(item_name)
    if item:
        return item.smell()
    else:
        return "You don't have the item to smell."

def cut_object_with_weapon(self, object_name, weapon_name):
    # Cut object with weapon command implementation
    object = self.game_state.get_player_location().get_object(object_name)
    weapon = self.game_state.get_player().get_item(weapon_name)
    if object and weapon:
        return object.cut_with(weapon)
    else:
        return "You can't cut the object with this weapon."

def wand_commands(self):
    # Wand commands implementation
    return "The wand glows faintly."

def fall(self):
    # Wand fall command implementation
    return "You command the wand to fall. It thuds against the ground."

def fantasize(self):
    # Wand fantasize command implementation
    return "You command the wand to fantasize. It does nothing."

def fear(self):
    # Wand fear command implementation
    return "You command the wand to fear. It trembles slightly."

def feeble(self):
    # Wand feeble command implementation
    return "You command the wand to become feeble. It dims slightly."

def fence(self):
    # Wand fence command implementation
    return "You command the wand to fence. It does nothing."

def ferment(self):
    # Wand ferment command implementation
    return "You command the wand to ferment. It does nothing."

def fierce(self):
    # Wand fierce command implementation
    return "You command the wand to become fierce. It sparks briefly."

def filch(self):
    # Wand filch command implementation
    return "You command the wand to filch. It does nothing."

def fireproof(self):
    # Wand fireproof command implementation
    return "You command the wand to become fireproof. It glows red briefly."

def float(self):
    # Wand float command implementation
    return "You command the wand to float. It rises a few inches off the ground."

def fluoresce(self):
    # Wand fluoresce command implementation
    return "You command the wand to fluoresce. It emits a soft, radiant light."

def free(self):
    # Wand free command implementation
    return "You command the wand to free. It briefly feels lighter in your hand."

def freeze(self):
    # Wand freeze command implementation
    return "You command the wand to freeze. It chills momentarily."

def frobizz(self):
    # Wand frobizz command implementation
    return "You command the wand to frobizz. It vibrates momentarily."

def frobnoid(self):
    # Wand frobnoid command implementation
    return "You command the wand to frobnoid. It wobbles briefly."

def frobozzle(self):
    # Wand frobozzle command implementation
    return "You command the wand to frobozzle. It remains stubbornly normal."

def fry(self):
    # Wand fry command implementation
    return "You command the wand to fry. It warms up slightly."

def fudge(self):
    # Wand fudge command implementation
    return "You command the wand to fudge. It gets slightly sticky."

def fumble(self):
    # Wand fumble command implementation
    return "You command the wand to fumble. It nearly slips from your grip."

def engage_combat(self, enemy):
    # Engage combat command implementation
    enemy = self.game_state.get_player_location().get_creature(enemy)
    if enemy:
        self.combat.initiate_combat(self.game_state.get_player(), enemy)
        return "You engage in combat!"
    else:
        return "There is no such creature here."

    # Add more commands as needed
