import arcade


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title='Рисование фигур')
        self.background_color = (255, 255, 255)

    def on_draw(self):
        self.clear()


if __name__ == '__main__':
    game = Game()
    arcade.run()
