import arcade


def create_cloud(x, y):
   arcade.draw_circle_filled(
       center_x=x,
       center_y=y,
       color=(0, 0, 255),
       radius=60
   )


class Game(arcade.Window):
   def __init__(self):
       super().__init__(width=800, height=600, title='Рисование фигур')
       self.background_color = (255, 255, 255)

   def on_draw(self):
       self.clear()
       for i in range(1, 4):
           create_cloud(100 * i, 400)
       for j in range(1, 3):
           create_cloud(100 * j + 50, 470)
       arcade.draw_line_strip(
           point_list=[(100, 200), (150, 250), (200, 200)],
           color=(0, 0, 0),
           line_width=2
       )
       arcade.draw_lrtb_rectangle_filled(
           left=300,
           right=500,
           top=300,
           bottom=100,
           color=(0, 0, 0)
       )
       arcade.draw_lrtb_rectangle_outline(
           left=550,
           right=750,
           top=300,
           bottom=100,
           color=(0, 0, 0),
           border_width=2
       )
       arcade.draw_point(
           x=100,
           y=250,
           color=(0, 0, 0),
           size=10
       )
       arcade.draw_rectangle_filled(
           center_x=100,
           center_y=100,
           width=200,
           height=100,
           color=(0, 0, 0),
           tilt_angle=45
       )
       arcade.draw_rectangle_outline(
           center_x=500,
           center_y=500,
           width=200,
           height=100,
           color=(0, 0, 0),
           tilt_angle=45,
           border_width=2
       )
       arcade.draw_triangle_filled(
           x1=100,
           y1=100,
           x2=200,
           y2=200,
           x3=300,
           y3=100,
           color=(0, 0, 0)
       )
       arcade.draw_triangle_outline(
           x1=500,
           y1=500,
           x2=600,
           y2=600,
           x3=400,
           y3=200,
           color=(0, 0, 0),
           border_width=2
       )


if __name__ == '__main__':
   game = Game()
   arcade.run()
