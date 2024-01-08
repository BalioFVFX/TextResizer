# FontResizer

### What is this about?
This is a little utility script that allows me to automatically adjust the font size of apps that I frequently use.
### Why don't you use the scaling that macOS provides?
Some monitors (including mine) do not support HiDPI resolutions.
### Can I use it too?
Yes, but at your own risk. I have created this script for my specific use case and it's intended to work for my setup. You will most likely have to edit the code. Also, keep in mind that the script overwrites some of the existing configs of the apps.

To use simply invoke `main.py`:

```bash
python3 main.py spotify:0 firefox:1.3 android_studio:14 intellij_idea:14 brave:1.2239010857415449
```

Note: Make sure to close the apps before running the script!

Additionally, you could use the `Laptop` and `Monitor` files included in this project. You just have to edit the `python3 ABSOULUTE_PATH_TO_FontAdjuster/main.py` to match the `main.py` file location.

### How does it work?
Firstly, this script supports a limited set of apps:
- Android Studio
- IntelliJ IDEA
- Firefox
- Brave
- Spotify

The script searches for the default installation paths for those apps.
Every app has its unique way of storing the last used font size. For example, Firefox has the `content-prefs.sqlite` file that contains a table named `prefs`. The script simply overwrites existing "per page" zoom levels and sets a default one for every website regardless of whether it has been visited before.
