# DVD Logo Bouncer

A fun Python Tkinter app that displays the classic DVD logo bouncing around your screen!  
Supports window resizing, multi-monitor setups, and fullscreen toggle with smooth animation.

---

## Features

- Classic DVD logo bouncing inside a resizable window  
- Fullscreen toggle with **F11** key (borderless, black background)  
- Exit fullscreen with **Esc** key  
- Proper handling of window maximize/restore behavior  
- Works on multi-monitor setups (window can span screens)  

---

## Requirements

- Python 3.x  
- [Pillow](https://python-pillow.org/) (`pip install pillow`)  

---

## Usage

1. Clone or download this repo  
2. Add a `dvd_logo.png` image file in the project folder (or use your own DVD logo image)  
3. Run the app:

```bash
python dvd_bouncer.py
```
4. Use **F11** to toggle fullscreen, **Esc** to exit fullscreen
5. Resize and move the window as you like

## Customize

- Replace `dvd_logo.png` with any image you want
- Adjust animation speed or bounce behavior inside dvd_bouncer.py

## License
This program uses an **MIT License**.

See LICENSE for more details.
