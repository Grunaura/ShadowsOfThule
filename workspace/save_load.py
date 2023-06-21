import os
import json
from .game import Player, Item

class SaveLoad:
    @staticmethod
    def save_game(player, save_file='save.json'):
        """
        Save the game state to a file.
        """
        try:
            save_dir = os.path.dirname(save_file)
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir)
            with open(save_file, 'w') as f:
                game_state = {
                    'player': {
                        'name': player.name,
                        'health': player.health,
                        'inventory': [item.__dict__ for item in player.inventory],
                    },
                    # Add other game state data as needed
                }
                json.dump(game_state, f)
        except Exception as e:
            print(f"Error while saving the game: {e}")

    @staticmethod
    def load_game(save_file='save.json'):
        """
        Load the game state from a file.
        """
        if not os.path.exists(save_file):
            print(f"No save file found at {save_file}")
            return None
        try:
            with open(save_file, 'r') as f:
                saved_data = json.load(f)
                player_data = saved_data.get('player')
                if player_data:
                    player = Player(
                        name=player_data.get('name'),
                        health=player_data.get('health'),
                        inventory=[Item(**item_data) for item_data in player_data.get('inventory')],
                    )
                    # Add other game state loading as needed
                    return player
                else:
                    print("Invalid save file format: Missing player data")
                    return None
        except Exception as e:
            print(f"Error while loading the game: {e}")
            return None
