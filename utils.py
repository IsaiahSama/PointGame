"""This file contains all of the utilities that I will be using throughout the game"""

import arcade
import yaml
import os

"""Format for save state:
PLAYER_NAME:
    DISPLAY_NAME: str
    SCORE: int
"""

default_save_state = {}

save_file_name = ""
class SaveStateManager:
    """Class which contains static methods used to manage the save state of the game"""

    @staticmethod
    def save_state(state:dict=default_save_state):
        """Method used to save the current state of the game
        
        Args:
            state (dict): The dictionary to store"""

        with open(save_file_name, "w") as fp:
            yaml.safe_dump(state, fp, indent=4)
        print("Saved!")

    @staticmethod
    def load_state():
        """Method used to load the current state of the game.
        
        Returns:
            dict - The state of the game"""
        
        if not os.path.exists(save_file_name):
            SaveStateManager.save_state()

        with open(save_file_name) as fp:
            try:
                data = yaml.safe_load(fp)
            except Exception as err:
                print(err)
                data = default_save_state
        return data
        