import arcade
import menu

WIDTH, HEIGHT = 800, 600
TITLE = "POINT GAME!"

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    menu_view = menu.MenuView()
    menu_view.setup()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()