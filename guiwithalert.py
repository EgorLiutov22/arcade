import arcade
import arcade.gui


class MyWindow(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "OKMessageBox Example", resizable=True)
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        open_message_box_button = arcade.gui.UIFlatButton(text="Open", width=200)
        open_message_box_button.on_click = self.on_click_open
        self.v_box.add(open_message_box_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_open(self, event):
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text=(
                "Это сообщение "
                "Нажмите Ок или Cancel"
            ),
            callback=self.on_message_box_close,
            buttons=["Ok", "Cancel"]
        )

        self.manager.add(message_box)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")


window = MyWindow()
arcade.run()
