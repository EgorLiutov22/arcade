import arcade


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Работа со звуками"


class OurGame(arcade.Window):
   def __init__(self, width, height, title):
       super().__init__(width, height, title)
       self.background = arcade.load_texture("resources/space.png")
       self.player = Penguin()
       self.player.center_x = 100
       self.player.center_y = 180
       self.player.change_y = 0
       self.player.change_angle = 0

   def setup(self):
       pass

   def on_draw(self):
       self.clear()
       arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
       self.player.draw()

   def on_update(self, delta_time):
       self.player.update()

   def on_key_press(self, key, modifiers):
       if key == arcade.key.SPACE:
           self.player.change_y = 5
           self.player.change_angle = 5

   def on_key_release(self, key, modifiers):
       pass

class Penguin(arcade.AnimatedTimeBasedSprite):
   def __init__(self):
       super().__init__(filename='resources/penguin1.png', scale=1)
       self.textures.append(arcade.load_texture("resources/penguin1.png"))
       self.textures.append(arcade.load_texture("resources/penguin2.png"))
       self.textures.append(arcade.load_texture("resources/penguin3.png"))

   def update(self):
       self.center_y += self.change_y
       self.angle += self.change_angle



game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()



