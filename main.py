import random
import time


import arcade
from array import array
from dataclasses import dataclass
import arcade.gl

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "GPU Particle Explosion"

PARTICLE_COUNT = 300


@dataclass
class Burst:
    buffer: arcade.gl.Buffer
    vao: arcade.gl.Geometry
    start_time: float


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.burst_list = []

        self.program = self.ctx.load_program(
            vertex_shader="vertex_shader_v1.glsl",
            fragment_shader="fragment_shader.glsl",
        )

        self.ctx.enable_only()

    def on_draw(self):
        self.clear()
        self.ctx.point_size = 2 * self.get_pixel_ratio()

        for burst in self.burst_list:
            self.program['time'] = time.time() - burst.start_time
            burst.vao.render(self.program, mode=self.ctx.POINTS)

    def on_update(self, dt):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        def _gen_initial_data(initial_x, initial_y):
            for i in range(PARTICLE_COUNT):
                dx = random.uniform(-.2, .2)
                dy = random.uniform(-.2, .2)
                yield initial_x
                yield initial_y
                yield dx
                yield dy

        x2 = x / self.width * 2. - 1.
        y2 = y / self.height * 2. - 1.
        initial_data = _gen_initial_data(x2, y2)
        buffer = self.ctx.buffer(data=array('f', initial_data))
        buffer_description = arcade.gl.BufferDescription(buffer,
                                                         '2f 2f',
                                                         ['in_pos', 'in_vel'])
        vao = self.ctx.geometry([buffer_description])
        burst = Burst(buffer=buffer, vao=vao, start_time=time.time())
        self.burst_list.append(burst)


if __name__ == "__main__":
    window = MyWindow()
    window.center_window()
    arcade.run()
