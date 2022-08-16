"""This file will contain the generic views for the game"""

import arcade
import gui
import utils

class NewGameView(arcade.View):
    """This class is responsible for the setup of a new game!"""

    def setup(self):
        """Sets up the class functionality"""
        self.error = ""
        self.game_state = utils.SaveStateManager.load_state()
        self.gui = gui.NewGameGUI()

        self.gui.add_user_button.on_click = self.add_player


    def on_show_view(self):
        return super().on_show_view()

    def on_draw(self):
        self.clear()
        self.gui.manager.draw()

        arcade.draw_text(self.error, start_x=arcade.get_window().width *0.5, start_y=arcade.get_window().height * 0.8, anchor_x="center")

    def start_game(self):
        """Used to start the game after the players have been added"""
        pass

    def add_player(self, event):
        player_name = self.gui.name_area.text
        player_nick = self.gui.nickname_area.text 

        if not (player_name.strip() and player_nick.strip()):
            self.error = "Can not leave fields empty."
            return

        if len(player_nick) > 6:
            self.error = "Nick should not be more than 6 characters"
            return

        self.game_state[player_name] = {"DISPLAY_NAME":player_nick, "SCORE":0}
        self.error = "Successfully added player"

        utils.SaveStateManager.save_state(self.game_state)
        
        
