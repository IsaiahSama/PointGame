import arcade
import arcade.gui
import utils


class MenuGUI:
    """Class that loads the menu GUI"""
    
    def __init__(self) -> None:
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
        self.v_box.add(new_game_button.with_space_around(bottom=20))

        game_state = utils.SaveStateManager.load_state()
        if game_state != utils.default_save_state:
            load_game_button = arcade.gui.UIFlatButton(text="Load Game", width=200)
            self.v_box.add(load_game_button.with_space_around(bottom=20))

            load_game_button.on_click = self.load_game

        new_game_button.on_click = self.new_game
        

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                child=self.v_box
            )
        )

    def new_game(self, event):
        """Will start a new game"""
        pass
    
    def load_game(self, event):
        """Used to load the game"""
        pass