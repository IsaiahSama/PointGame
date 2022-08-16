import arcade


class MenuView(arcade.View):
    
    def on_show_view(self):
        """Called when this view is shown"""
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Draw the menu"""
        self.clear()