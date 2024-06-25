import arcade

class Game(arcade.Window):
   def __init__(self, width=400, height=300, title='Моя игра'):
       super().__init__(width=width, height=height, title=title, resizable=True)
       self.background_color = (0, 0, 150)
       self.set_min_size(400, 300)
       self.set_max_size(900, 700)
       self.center_window()
       print(self.get_location())
       print(self.get_size())
       self.center_window()
       self.set_mouse_visible(False)
   def on_draw(self):
       self.clear()

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       self.set_location(500, 500)


if __name__ == '__main__':
   game = Game(400, 300, 'Моя игра')
   arcade.run()

