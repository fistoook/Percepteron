import tkinter as tk
from PIL import ImageTk, Image, ImageOps

class Goey(tk.Tk):
    def __init__(self):
        super().__init__()
        self.look_nice()
        self.init_widgets()

    def run():
        tk.mainloop()

    def look_nice(self):
        dimensions = (int(self.winfo_screenwidth() * 0.5), int(self.winfo_screenheight() * 0.5))
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")
        self.title("Pixie")
        self.config(background="tomato")

    def init_widgets(self):
        # main frame holding everything besides the button
        self.image_frame = tk.Frame(self)

        self.image1 = tk.Label(self.image_frame)
        self.image2 = tk.Label(self.image_frame)

        self.label1 = tk.Label(self.image_frame)
        self.label2 = tk.Label(self.image_frame)

        self.button = tk.Button(self, text="Switch")

        self.grid_them()

    def grid_them(self):
        self.image_frame.grid()
        self.image1.grid(row=0, column=0)
        self.image2.grid(row=0, column=1)
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=1, column=1)   
        self.button.grid(row=2) 

    def update_widgets(self, images, predictions, labels):
        self.photo1 = self._load_photo(images[0][0])
        self.photo2 = self._load_photo(images[1][0])

        self.image1.configure(image=self.photo1)
        self.image2.configure(image=self.photo2)

        prediction1 = "Land" if predictions[0] == 0 else "Sea"
        prediction2 = "Land" if predictions[1] == 0 else "Sea"

        self.label1.configure(text=f"Predcited: {prediction1}")
        self.label2.configure(text=f"Predicted: {prediction2}")

    
    def _load_photo(self, path):
        with Image.open(path) as img:
            resized = ImageOps.pad(
                img.convert("RGB"),
                (320, 240),
                color="black"
            )
        return ImageTk.PhotoImage(resized)
