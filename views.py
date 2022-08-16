"""This file will contain the generic views for the game"""

import arcade
import gui

class NewGameView(arcade.View):
    """This class is responsible for the setup of a new game!"""

    def setup(self):
        self.gui = gui.NewGameGUI()

    def on_show_view(self):
        return super().on_show_view()

    def on_draw(self):
        self.clear()
        self.gui.manager.draw()