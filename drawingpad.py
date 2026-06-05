import tkinter as tk

class DrawingPad:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Pad")

        # Canvas widget
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.last_x, self.last_y = None, None

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
        self.last_x, self.last_y = x, y

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingPad(root)
    root.mainloop()
