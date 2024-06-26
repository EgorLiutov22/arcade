import arcade


class Game(arcade.Window):
   def __init__(self):
       super().__init__(width=800, height=600, title='Рисование фигур')
       self.background_color = (255, 255, 255)

   def on_draw(self):
       self.clear()
       arcade.draw_arc_filled(
           center_x=400,
           center_y=300,
           width=155,
           height=155,
           color=(0, 0, 0, 125),
           start_angle=0,
           end_angle=180,
           tilt_angle=15,
           num_segments=15
       )
       arcade.draw_arc_outline(
           center_x=200,
           center_y=150,
           width=155,
           height=155,
           color=(0, 0, 0, 125),
           start_angle=0,
           end_angle=90,
           tilt_angle=15,
           num_segments=15,
           border_width=2
       )
       arcade.draw_circle_filled(
           center_x=600,
           center_y=400,
           radius=100,
           color=(0, 0, 0),
           tilt_angle=0,
           num_segments=-1
       )
       arcade.draw_circle_outline(
           center_x=200,
           center_y=400,
           radius=100,
           color=(0, 0, 0),
           tilt_angle=0,
           num_segments=-1,
           border_width=2
       )
       arcade.draw_ellipse_filled(
           center_x=100,
           center_y=500,
           color=(0, 0, 0),
           tilt_angle=0,
           num_segments=-1,
           width=100,
           height=150
       )
       arcade.draw_ellipse_outline(
           center_x=100,
           center_y=100,
           color=(0, 0, 0),
           tilt_angle=0,
           num_segments=-1,
           width=100,
           height=150, border_width=2
       )
       arcade.draw_line(
           start_x=300,
           start_y=250,
           end_x=500,
           end_y=250,
           color=(0, 0, 0),
           line_width=2
       )


if __name__ == '__main__':
   game = Game()
   arcade.run()
