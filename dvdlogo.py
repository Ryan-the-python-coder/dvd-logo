import tkinter as tk
from PIL import Image, ImageTk

class DVDLogoBouncer:
    def __init__(self, root, img_path):
        self.root = root
        self.root.title("DVD Logo Bouncer")
        self.root.resizable(True, True)
        self.root.configure(bg='black')

        self.fullscreen = False
        self.previous_geometry = None  # To save window size/position before fullscreen

        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.exit_fullscreen)

        self.img = Image.open(img_path)
        self.photo = ImageTk.PhotoImage(self.img)

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image_obj = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)

        self.x = 0
        self.y = 0
        self.dx = 3
        self.dy = 3

        self.img_width = self.img.width
        self.img_height = self.img.height

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        self.canvas.bind("<Configure>", self.on_resize)

        self.animate()

    def toggle_fullscreen(self, event=None):
        if not self.fullscreen:
            # Save geometry before fullscreen
            self.previous_geometry = self.root.geometry()
            self.fullscreen = True
            self.root.attributes("-fullscreen", True)
            self.root.overrideredirect(True)
        else:
            self.exit_fullscreen()

    def exit_fullscreen(self, event=None):
        if self.fullscreen:
            self.fullscreen = False
            self.root.attributes("-fullscreen", False)
            self.root.overrideredirect(False)
            # Restore previous size/position if saved
            if self.previous_geometry:
                self.root.geometry(self.previous_geometry)
                self.previous_geometry = None

    def on_resize(self, event):
        self.canvas_width = event.width
        self.canvas_height = event.height

        # Clamp position inside canvas when resized
        if self.x + self.img_width > self.canvas_width:
            self.x = max(self.canvas_width - self.img_width, 0)
            self.dx = -abs(self.dx)  # Bounce back to left

        if self.y + self.img_height > self.canvas_height:
            self.y = max(self.canvas_height - self.img_height, 0)
            self.dy = -abs(self.dy)  # Bounce back up

    def animate(self):
        self.x += self.dx
        self.y += self.dy

        max_x = max(self.canvas_width - self.img_width, 0)
        max_y = max(self.canvas_height - self.img_height, 0)

        # Bounce horizontally
        if self.x >= max_x:
            self.x = max_x
            self.dx = -abs(self.dx)
        elif self.x <= 0:
            self.x = 0
            self.dx = abs(self.dx)

        # Bounce vertically
        if self.y >= max_y:
            self.y = max_y
            self.dy = -abs(self.dy)
        elif self.y <= 0:
            self.y = 0
            self.dy = abs(self.dy)

        self.canvas.coords(self.image_obj, self.x, self.y)

        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = DVDLogoBouncer(root, "dvd_logo.png")
    root.mainloop()
