import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALING = 1


class Game(arcade.Window):
   def __init__(self):
       super().__init__(
           width=SCREEN_WIDTH,
           height=SCREEN_HEIGHT,
           title="Работа со спрайтами",
       )
       self.player_sprite = None
       SPRITE_SCALING_COIN = 0.2
       self.coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)


   def setup(self):
       image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
       self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
       self.player_sprite.center_x = 64
       self.player_sprite.center_y = 128
       self.coin.center_x = 640
       self.coin.center_y = 120

   def on_draw(self):
       self.clear()
       self.player_sprite.draw()
       self.coin.draw()

   def update(self, delta_time: float):
       pass


if __name__ == "__main__":
   game = Game()
   game.setup()
   arcade.run()
