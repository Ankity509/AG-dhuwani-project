from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Background color set karne ke liye (Optional)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class AGDhuwaniApp(App):
    def build(self):
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Header
        header = Label(
            text='AG DHUWANI', 
            font_size='32sp', 
            bold=True, 
            color=(1, 0.8, 0, 1), # Yellow/Gold color
            size_hint_y=None, 
            height=100
        )
        layout.add_widget(header)

        # Tagline
        tagline = Label(
            text='Medicine Cold Chain Transport', 
            font_size='14sp', 
            size_hint_y=None, 
            height=30
        )
        layout.add_widget(tagline)

        # Input Fields (Mockup)
        layout.add_widget(Label(text='Enter Pickup Location:', halign='left', size_hint_y=None, height=30))
        self.pickup = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.pickup)

        layout.add_widget(Label(text='Enter Destination:', size_hint_y=None, height=30))
        self.drop = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.drop)

        # Booking Button
        btn = Button(
            text='Book Now', 
            background_color=(0, 0.6, 0.3, 1), 
            bold=True,
            size_hint_y=None, 
            height=60
        )
        btn.bind(on_press=self.on_booking)
        layout.add_widget(btn)

        return layout

    def on_booking(self, instance):
        print(f"Booking Request: From {self.pickup.text} to {self.drop.text}")
        instance.text = "Request Sent!"

if __name__ == '__main__':
    AGDhuwaniApp().run()
