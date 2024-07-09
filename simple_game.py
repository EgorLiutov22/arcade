import arcade


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Работа со звуками"


class OurGame(arcade.Window):
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

   def setup(self):
       pass

   def on_draw(self):
       self.clear()

   def update(self, delta_time):
       pass

   def on_key_press(self, key, modifiers):
       pass

   def on_key_release(self, key, modifiers):
       pass


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
