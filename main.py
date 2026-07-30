
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from android_webview_video import AndroidVideoWebView

BG_MAIN = (0x0d / 255, 0x0c / 255, 0x0d / 255, 1)
BG_SIDEBAR = (0x28 / 255, 0x24 / 255, 0x24 / 255, 1)
BTN_TEAL = (22 / 255, 147 / 255, 168 / 255, 1)
TEXT_WHITE = (1, 1, 1, 1)


def styled_button(text):
    return Button(
        text=text,
        background_normal="",
        background_color=BTN_TEAL,
        color=TEXT_WHITE,
        size_hint=(None,None),
        size=(dp(200),dp(80))
    )



class DaySelectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(15))

      
        app = App.get_running_app()
        for day in app.days_dictionary:
            anchor=AnchorLayout()
            btn=styled_button(day.capitalize())
            btn.bind(on_release=lambda instance, d=day: self.go_to_day(d))
            anchor.add_widget(btn)
            layout.add_widget(anchor)
        self.add_widget(layout)

    def go_to_day(self, day):
      
        app=App.get_running_app()
        app.selected_day=day
        self.manager.current="video_screen"



class VideoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.video_num = 0
        self.current_video = None

        root = BoxLayout(orientation="vertical")

        self.video = AndroidVideoWebView()
        controls = BoxLayout(size_hint=(1, 0.15))

        back_btn = styled_button("< Back to Days")
        prev_btn = styled_button("< Previous")
        
        next_btn = styled_button("Next >")
        back_btn.size_hint=(1,1)
        prev_btn.size_hint=(1,1)
        
        next_btn.size_hint=(1,1)
        back_btn.bind(on_release=self.go_back)
        prev_btn.bind(on_release=self.previous_video)
        next_btn.bind(on_release=self.next_video)
        
     
        controls.add_widget(back_btn)
        controls.add_widget(prev_btn)
        
        controls.add_widget(next_btn)

        root.add_widget(self.video)
        root.add_widget(controls)
        self.add_widget(root)

    def on_enter(self):
        
        app=App.get_running_app()
        day=app.selected_day
        self.current_video=app.days_dictionary[day]
        self.video_num=0
        self.video.load_url(self.current_video[self.video_num])

    def go_back(self, instance):
        self.video.pause()
        self.video.close()
        self._is_playing = False    
        self.manager.current = "day_select"
        Clock.schedule_once(
            lambda dt: setattr(self.manager, "current", "day_select"), 0.15
        )
    def next_video(self, instance):
        
        self.video_num+=1
        app=App.get_running_app()

        if self.video_num==len(app.days_dictionary[app.selected_day]):
            self.video_num=0
        self.current_video=app.days_dictionary[app.selected_day]
        self.video.load_url(self.current_video[self.video_num])

    def previous_video(self, instance):
      
        self.video_num-=1
        app=App.get_running_app()
        if self.video_num==-1:
            self.video_num=len(app.days_dictionary[app.selected_day])-1
        self.current_video=app.days_dictionary[app.selected_day]
        self.video.load_url(self.current_video[self.video_num])
        

    

# ------------------------------------------------------i------
# APP
# ------------------------------------------------------------
class WorkoutApp(App):
    def build(self):
        Window.clearcolor = BG_MAIN

      
        self.days_dictionary = {
    "monday": [
        "https://video-host-v7l6.onrender.com/assets/monday/monday1.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday2.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday3.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday4.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday5.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday6.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday7.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday8.mp4",
        "https://video-host-v7l6.onrender.com/assets/monday/monday9.mp4",
    ],

    "tuesday": [
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday1.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday2.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday3.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday4.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday5.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday6.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday7.mp4",
        "https://video-host-v7l6.onrender.com/assets/tuesday/Tuesday8.mp4",
    ],

    "thursday": [
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday1.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday2.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday3.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday4.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday5.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday6.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday7.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday8.mp4",
        "https://video-host-v7l6.onrender.com/assets/thursday/Thursday9.mp4",
    ],
}

        
        self.selected_day = None

        sm = ScreenManager()
        sm.add_widget(DaySelectScreen(name="day_select"))
        sm.add_widget(VideoScreen(name="video_screen"))
        return sm


if __name__ == "__main__":
    WorkoutApp().run()