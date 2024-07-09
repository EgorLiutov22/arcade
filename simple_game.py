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
       self.columns_list = arcade.SpriteList()


   def setup(self):
       for i in range(5):
           column_top = ColumnTop("resources/column_top.png", 1)
           column_top.center_x = 130 * i + SCREEN_WIDTH
           column_top.center_y = 400
           column_top.change_x = 4
           self.columns_list.append(column_top)



   def on_draw(self):
       self.clear()
       arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
       self.player.draw()
       self.columns_list.draw()
       self.columns_list.update()

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
       self.cur_texture = 0

   def update(self):
       self.center_y += self.change_y
       self.angle += self.change_angle
       self.change_y -= 0.4
       if self.center_y < 0:
           self.center_y = 0
       if self.center_y > SCREEN_HEIGHT:
           self.center_y = SCREEN_HEIGHT
       self.change_angle -= 0.4
       if self.angle >= 40:
           self.angle = 40
       if self.angle <= -30:
           self.angle = -30

   def update_animation(self, delta_time: float = 1 / 60):
       self.cur_texture += 1
       if self.cur_texture >= len(self.textures) * 5:
           self.cur_texture = 0
       frame = self.cur_texture // 5
       self.texture = self.textures[frame]

class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x



game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()



