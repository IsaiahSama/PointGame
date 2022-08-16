import arcade
import utils
import gui


class MenuView(arcade.View):
    """Displays the menu of the game to the user."""

    def setup(self):
        """Sets up the data for the Menu"""
        self.game_state = utils.SaveStateManager.load_state()
        self.menu_gui = gui.MenuGUI()

    
    def on_show_view(self):
        """Called when this view is shown"""
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Draw the menu"""
        self.clear()
        self.menu_gui.manager.draw()