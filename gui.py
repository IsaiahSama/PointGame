import arcade
import arcade.gui
import utils
import views

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
        view = views.NewGameView()
        view.setup()
        arcade.get_window().show_view(view)

    def load_game(self, event):
        """Used to load the game"""
        pass

class NewGameGUI:
    """The gui displayed when starting a new game"""
    def __init__(self) -> None:
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.header_box = arcade.gui.UIBoxLayout()

        text_label = arcade.gui.UITextArea(text="Add your Players!", font_size=24)
        self.header_box.add(text_label)

        self.form_box = arcade.gui.UIBoxLayout()

        name_label = arcade.gui.UILabel(text="Enter Player name", font_size=12, align="center")
        self.form_box.add(name_label.with_space_around(bottom=10))

        name_area = arcade.gui.UIInputText(height=20, width=200)
        self.form_box.add(name_area.with_border(2, arcade.color.BLACK).with_space_around(bottom=20))

        nickname_label = arcade.gui.UILabel(text="Enter Player's Display Name", font_size=12, align="center")
        self.form_box.add(nickname_label.with_space_around(bottom=10))

        nickname_area = arcade.gui.UIInputText(height=20, width=200)
        self.form_box.add(nickname_area.with_border(2, arcade.color.BLACK).with_space_around(bottom=20))

        self.button_box = arcade.gui.UIBoxLayout(vertical=False)

        add_user_button = arcade.gui.UIFlatButton(text="Add User")
        self.button_box.add(add_user_button.with_space_around(right=20))

        play_game_button = arcade.gui.UIFlatButton(text="Play Game")
        self.button_box.add(play_game_button.with_space_around(right=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.header_box,
                anchor_x='center',
                anchor_y='top',
                align_x=20
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.form_box,
                anchor_x='center',
                anchor_y='center'
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.button_box,
                anchor_x='center',
                anchor_y='bottom'
            )
        )
