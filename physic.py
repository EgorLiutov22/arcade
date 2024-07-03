import arcade

SCREEN_TITLE = "Использование PyMunk"

SPRITE_IMAGE_SIZE = 128

SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_TILES = 0.3

SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT


GRAVITY = 1500

DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.4

PLAYER_FRICTION = 1.0
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6

PLAYER_MASS = 2.0

PLAYER_MAX_HORIZONTAL_SPEED = 200
PLAYER_MAX_VERTICAL_SPEED = 1600



class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player_sprite = None

        self.player_list = None
        self.wall_list = None
        self.bullet_list = None
        self.item_list = None

        self.left_pressed = False
        self.right_pressed = False

        self.physics_engine = None

        arcade.set_background_color(arcade.color.AMAZON)

        damping = DEFAULT_DAMPING
        gravity = (0, -GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        map_name = ":resources:/tiled_maps/pymunk_test_map.json"
        tile_map = arcade.load_tilemap(map_name, SPRITE_SCALING_TILES)
        print(tile_map.sprite_lists)
        self.wall_list = tile_map.sprite_lists["Platforms"]
        self.item_list = tile_map.sprite_lists["Dynamic Items"]
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = SPRITE_SIZE + SPRITE_SIZE / 2
        self.player_sprite.center_y = SPRITE_SIZE + SPRITE_SIZE / 2
        self.player_list.append(self.player_sprite)

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def on_update(self, delta_time):
        self.physics_engine.step()

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.item_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
