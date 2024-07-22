import arcade
import arcade.gui

class MyWindow(arcade.Window):
   def __init__(self):
       super().__init__(800, 600, "UIFlatButton Example", resizable=True)
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
       start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
       start_button.on_click = self.on_click_start
       self.v_box.add(start_button.with_space_around(bottom=20))

       settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
       self.v_box.add(settings_button.with_space_around(bottom=20))

       quit_button = QuitButton(text="Quit", width=200)
       self.v_box.add(quit_button)

       @settings_button.event("on_click")
       def on_click_settings(event):
           print("Settings:", event)


   def on_draw(self):
       self.clear()
       self.manager.draw()

   def on_click_start(self, event):
       print("Start:", event)




class QuitButton(arcade.gui.UIFlatButton):
   def on_click(self, event: arcade.gui.UIOnClickEvent):
       arcade.exit()



window = MyWindow()
arcade.run()

