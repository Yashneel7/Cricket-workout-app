# 🏏 Cricket Workout App

A cross-platform mobile workout application designed specifically for cricket players.  
Built with **Python + Kivy**, packaged for Android using **Buildozer**, and featuring a custom native **Android WebView** video player for smooth streaming of training videos.

> Perfect for college students, interns, and junior developers looking to showcase real mobile development skills with Python.

---

## ✨ Features

- **Day-wise Workout Plans** – Structured training routines for Monday, Tuesday, and Thursday
- **Native Video Playback** – Custom Android WebView integration for reliable video streaming (solves common Kivy video limitations on Android)
- **Simple & Clean UI** – Dark theme with intuitive navigation (Previous / Next / Back)
- **Cross-platform Ready** – Runs on desktop during development, packages cleanly to Android APK
- **Internet Streaming** – Videos hosted externally (no large APK size)

---

## 🛠️ Tech Stack

| Layer              | Technology                          |
|--------------------|-------------------------------------|
| UI Framework       | Kivy                                |
| Language           | Python 3                            |
| Android Bridge     | Pyjnius + android.runnable          |
| Video Player       | Custom Android WebView              |
| Packaging          | Buildozer + python-for-android      |
| Target Platforms   | Android (primary), Desktop (dev)    |

---

## 📱 Screenshots

*(Add screenshots here after building the APK)*

| Day Selection | Video Player |
|---------------|--------------|
| ![Day Select](screenshots/day_select.png) | ![Video](screenshots/video_player.png) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Kivy
- Buildozer (for Android builds)
- Android SDK / NDK (managed by Buildozer)

### Run on Desktop (Development)

```bash
pip install kivy
python main.py
```

### Build Android APK

```bash
# Install Buildozer
pip install buildozer

# Build debug APK
buildozer android debug

# The APK will be generated in the `bin/` folder
```

---

## 📂 Project Structure

```
Cricket-workout-app/
├── main.py                     # App entry point + screens
├── android_webview_video.py    # Custom native WebView video player
├── buildozer.spec              # Android packaging configuration
├── icon.jpg                    # App icon
├── logo.png                    # Splash / presplash image
└── README.md
```

---

## 🔧 Key Technical Highlights

- **Custom Android WebView Widget**  
  Solved the common problem of unreliable video playback in pure Kivy by embedding a native Android `WebView` and controlling it via Pyjnius.

- **Proper Media Lifecycle Management**  
  Implemented `onPause()`, `pauseTimers()`, and blank page loading so audio/video correctly stops when navigating away from the player.

- **Clean Screen Management**  
  Used Kivy’s `ScreenManager` for smooth transitions between day selection and video playback screens.

- **Buildozer Configuration**  
  Fully configured `buildozer.spec` with correct permissions (`INTERNET`), architecture targets (`arm64-v8a`, `armeabi-v7a`), and API levels.

---

## 🎯 Learning Outcomes & Skills Demonstrated

- Mobile app development with Python
- Native Android integration using Pyjnius
- Handling media playback edge cases on Android
- Cross-platform UI development with Kivy
- Android packaging & deployment pipeline (Buildozer)
- Clean architecture and separation of concerns

---

## 📈 Future Improvements

- [ ] Add more training days and categories (Bowling, Batting, Fielding, Strength)
- [ ] Offline video download support
- [ ] Progress tracking & workout history
- [ ] User authentication
- [ ] Dark / Light theme toggle
- [ ] iOS support via Kivy / Briefcase

---

## 👨‍💻 Author

**Yashneel**  
GitHub: [Yashneel7](https://github.com/Yashneel7)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
