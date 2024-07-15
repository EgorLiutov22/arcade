import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Космический шутер'

SPRITE_SCALING_PLAYER = 0.5

SPRITE_SCALING_LASER = 0.3


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_texture = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.player_sprite = None
        self.laser_sprite = None
        self.laser_sprite_list = None

    def setup(self):
        self.player_sprite = Player()
        self.set_mouse_visible(False)
        self.laser_sprite_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background_texture)
        self.player_sprite.draw()
        self.laser_sprite_list.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        if self.player_sprite.center_y >= SCREEN_HEIGHT / 2:
            self.player_sprite.center_y = SCREEN_HEIGHT / 2

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.laser_sprite = Laser()
            self.laser_sprite.bottom = self.player_sprite.top
            self.laser_sprite.center_x = self.player_sprite.center_x
            self.laser_sprite_list.append(self.laser_sprite)


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png', SPRITE_SCALING_PLAYER)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 30


class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/laserBlue01.png', SPRITE_SCALING_LASER)


def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
