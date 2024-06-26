import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Rectangle:
    def __init__(self, x, y, w, h, color, tlit=0, filled=False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.tlit = tlit
        self.filled = filled
        self.change_x = 3
        self.change_y = 3

    def draw(self):
        if not self.filled:
            arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, self.color)
        else:
            arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color)

    def update(self):
        self.y += self.change_y
        self.x += self.change_x
        if self.x + self.w / 2 > SCREEN_WIDTH or self.x - self.w / 2 < 0:
            self.change_x = -self.change_x
        if self.y + self.h / 2 > SCREEN_HEIGHT or self.y - self.h / 2 < 0:
            self.change_y = -self.change_y

    def change_size(self):
        if (
                self.x + self.w / 2 >= SCREEN_WIDTH
                or self.x - self.w / 2 <= 0
                or self.y + self.h / 2 >= SCREEN_HEIGHT
                or self.y - self.h / 2 <= 0
        ):
            self.w += 2
            self.h += 2


class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Геометрические фигуры и их анимация"
        )

        self.background_color = (155, 255, 255)
        # self.batch = arcade.ShapeElementList()
        self.rectangle1 = Rectangle(20, 100, 40, 50, arcade.color.BLUE)
        self.rectangle2 = Rectangle(SCREEN_WIDTH - 40, 200, 40, 50, arcade.color.YELLOW, filled=True)



    def on_draw(self):
        self.clear()
        self.rectangle1.draw()
        self.rectangle2.draw()

    def update(self, delta_time: float):
        self.rectangle1.update()
        self.rectangle2.update()
        self.rectangle2.change_size()

    # def on_draw(self):
    #     self.clear()
        # self.batch.draw()

    # def setup(self):
    #     ellipse1 = arcade.create_ellipse(
    #         center_x=300, center_y=300, width=50, height=60, color=arcade.color.BLUE, filled=False
    #     )
    #     ellipse2 = arcade.create_ellipse_filled_with_colors(
    #         center_x=300,
    #         center_y=300,
    #         width=200,
    #         height=250,
    #         outside_color=arcade.color.RED,
    #         inside_color=arcade.color.GREEN,
    #         tilt_angle=45,
    #     )
    #
    #     self.batch.append(ellipse1)
    #     self.batch.append(ellipse2)


if __name__ == "__main__":
    game = Game()
    arcade.run()
