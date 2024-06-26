import arcade


class Game(arcade.Window):
   def __init__(self):
       super().__init__(width=800, height=600, title='Рисование фигур')
       self.background_color = (255, 255, 255)
       self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_jump.png')

   def on_draw(self):
       self.clear()
       w, h = self.texture.image.size
       arcade.draw_texture_rectangle(
           center_x=100,
           center_y=200,
           width=w,
           height=h,
           texture=self.texture
       )


if __name__ == '__main__':
   game = Game()
   arcade.run()
