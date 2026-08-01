"""
Android-native WebView video player for Kivy
"""

from kivy.utils import platform
from kivy.uix.widget import Widget
from kivy.uix.video import Video
from kivy.clock import Clock

if platform == "android":
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
else:
    def run_on_ui_thread(func):
        return func


class AndroidVideoWebView(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._webview = None
        self._current_url = None
        self._webview_ready = False

        if platform == "android":
          
            self.bind(pos=self._on_pos_size, size=self._on_pos_size)
        else:
            self._desktop_video = Video(state="pause")
            self.add_widget(self._desktop_video)
            self.bind(pos=self._sync_desktop_video, size=self._sync_desktop_video)

    def _sync_desktop_video(self, *args):
        self._desktop_video.pos = self.pos
        self._desktop_video.size = self.size

    def _on_pos_size(self, *args):
        if self._webview_ready:
            self._update_webview_bounds()

    # ------------------------------------------------------------------
    # ANDROID
    # ------------------------------------------------------------------
    @run_on_ui_thread
    def _setup_android_webview(self):
        if self._webview is not None:
            return  # already exists
        try:
            WebView = autoclass("android.webkit.WebView")
            WebViewClient = autoclass("android.webkit.WebViewClient")
            WebChromeClient = autoclass("android.webkit.WebChromeClient")
            LayoutParams = autoclass("android.view.ViewGroup$LayoutParams")
            View = autoclass("android.view.View")
            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            
            activity = PythonActivity.mActivity
            self._webview = WebView(activity)
            self._webview.getSettings().setJavaScriptEnabled(True)
            self._webview.getSettings().setMediaPlaybackRequiresUserGesture(False)
            self._webview.setWebViewClient(WebViewClient())
            self._webview.setWebChromeClient(WebChromeClient())

           
            self._webview.setVisibility(View.GONE)

            activity.addContentView(
                self._webview,
                LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT),
            )

            self._webview_ready = True
            self._update_webview_bounds()
        except Exception as e:
            print("WebView setup failed:", e)

    @run_on_ui_thread
    def _update_webview_bounds(self, *args):
        if not self._webview or not self._webview_ready:
            return
        try:
            LayoutParams = autoclass("android.view.ViewGroup$LayoutParams")
            View = autoclass("android.view.View")

            window = self.get_root_window()
            window_height = window.height if window else self.top

            android_x = int(self.x)
            android_y = int(window_height - self.top)

            params = self._webview.getLayoutParams()
            if params is None:
                params = LayoutParams(int(self.width), int(self.height))
            else:
                params.width = int(self.width)
                params.height = int(self.height)

            self._webview.setLayoutParams(params)
            self._webview.setX(android_x)
            self._webview.setY(android_y)

           
            if self.width > 1 and self.height > 1:
                self._webview.setVisibility(View.VISIBLE)
        except Exception as e:
            print("WebView bounds update failed:", e)

    @run_on_ui_thread
    def load_url(self, url):
        self._current_url = url
        html = f"""
        <html><body style="margin:0;background:#000;">
        <iframe src="{url}" width="100%" height="100%" frameborder="0"
                allow="autoplay; fullscreen" allowfullscreen>
        </iframe>
        </body></html>
        """
        if platform == "android":
            if self._webview is None:
                self._setup_android_webview()
            if self._webview and self._webview_ready:
                View = autoclass("android.view.View")
                self._webview.setVisibility(View.VISIBLE)
                self._webview.loadDataWithBaseURL(None, html, "text/html", "UTF-8", None)
                self._update_webview_bounds()
        else:
            self._desktop_video.source = url
            self._desktop_video.state = "play"

    @run_on_ui_thread
    def play(self):
        if platform == "android" and self._webview and self._webview_ready:
            self._webview.evaluateJavascript(
                "document.getElementById('player') && document.getElementById('player').play();",
                None,
            )
        elif platform != "android":
            self._desktop_video.state = "play"

    @run_on_ui_thread
    def pause(self):
        if platform == "android" and self._webview and self._webview_ready:
            self._webview.evaluateJavascript(
                "document.getElementById('player') && document.getElementById('player').pause();",
                None,
            )
        elif platform != "android":
            self._desktop_video.state = "pause"

    @run_on_ui_thread
    def close(self):
        
        if not self._webview:
            return
        try:
            self._webview_ready = False
            

            
            self._webview.setVisibility(self.View.GONE)

           
            self._webview.stopLoading()
            self._webview.loadUrl("about:blank")
            self._webview.clearHistory()
            self._webview.clearCache(True)
            try:
                self._webview.onPause()
                self._webview.pauseTimers()
            except Exception:
                pass

            
            parent = self._webview.getParent()
            if parent is not None:
                parent.removeView(self._webview)

            
            self._webview.destroy()
        except Exception as e:
            print("WebView close failed:", e)
        finally:
            self._webview = None
            self._webview_ready = False
    @run_on_ui_thread
    def hide(self):
        if not self._webview:
            return
        try:
            
            self._webview.setVisibility(8)                             # if you have a pause helper
            
            params = self._webview.getLayoutParams()
            if params:
                params.width = 0
                params.height = 0
                self._webview.setLayoutParams(params)
        except Exception as e:
            print("hide failed:", e)

    @run_on_ui_thread
    def show(self):
        if not self._webview:
            return
        try:
            self._webview.setVisibility(0)          
            self._update_webview_bounds()           
        except Exception as e:
            print("show failed:", e)