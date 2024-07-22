import arcade
import arcade.gui


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Пример", resizable=True)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        start_button = arcade.gui.UIFlatButton(text="Старт", width=200)
        start_button.on_click = self.on_click_start
        self.v_box.add(start_button.with_space_around(bottom=20))

        quit_button = QuitButton(text="Выход", width=200)
        self.v_box.add(quit_button)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_start(self, event):
        print("Нажата кнопка Старт", event)


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("Нажата кнопка Выход", event)
        arcade.exit()


window = MyWindow()
arcade.run()
