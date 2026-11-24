import tkinter as tk
from PIL import ImageTk, Image, ImageOps

class Goey(tk.Tk):
    '''
        Goey is a (goey) tkinter user interface made for 
        playing around with the Percepteron model, Percy.
        It is used by Macey, The MCV, and it is cool.
    '''
    def __init__(self):
        super().__init__()
        self._init_screen()
        self._init_widgets()
        self._structure_widgets()

        self.prediction_frames_dict = {}

    def run(self):
        tk.mainloop()

    def _init_screen(self):
        dimensions = (int(self.winfo_screenwidth() * 0.8), int(self.winfo_screenheight() * 0.8))
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")
        self.title("Land & Sea Classifier")
        self.config(background="tomato")

    def _init_widgets(self):
        self.main_frame = tk.Frame(self)

        self.title_label = tk.Label(self.main_frame, text="Land & Sea Classifier")

        self.button = tk.Button(self.main_frame, text="Refresh")

        self.image_frame = tk.Frame(self.main_frame)

        self.image1 = tk.Label(self.image_frame)
        self.image2 = tk.Label(self.image_frame)

        self.classification_frame = tk.Frame(self.main_frame)

        self.classification_label1 = tk.Label(self.classification_frame)
        self.classification_label2 = tk.Label(self.classification_frame)

        self.predictions_frame = tk.Frame(self.main_frame)



    def _structure_widgets(self):
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label.pack(pady=(0, 15))

        self.image_frame.pack(fill="x", pady=10)

        self.image_frame.columnconfigure(0, weight=1)
        self.image_frame.columnconfigure(1, weight=1)

        self.image1.grid(row=0, column=0, padx=10)
        self.image2.grid(row=0, column=1, padx=10)

        self.classification_label1.grid(row=0, column=0)
        self.classification_label2.grid(row=0, column=1)

        self.classification_frame.columnconfigure(0, weight=1)
        self.classification_frame.columnconfigure(1, weight=1)

        self.classification_frame.pack(fill="x")
        self.predictions_frame.pack(fill="x", pady=10)

        self.button.pack(pady=10)

    def update_widgets(self, images, predictions, classifications):
        self.photo1 = self._load_photo(images[0][0])
        self.photo2 = self._load_photo(images[1][0])

        self.image1.configure(image=self.photo1)
        self.image2.configure(image=self.photo2)

        self.classification_label1.configure(text=classifications[0])
        self.classification_label2.configure(text=classifications[1])

        for widget in self.predictions_frame.winfo_children():
            widget.destroy()

        for model_name, (prediction1, prediction2) in predictions.items():
            prediction_frame = tk.Frame(self.predictions_frame)

            self.prediction_frames_dict[model_name] = prediction_frame

            for widget in prediction_frame.winfo_children():
                widget.destroy()

            name_label = tk.Label(prediction_frame, text=model_name)

            prediction1_label = tk.Label(prediction_frame, text=prediction1)
            prediction2_label = tk.Label(prediction_frame, text=prediction2)

            prediction_frame.pack(fill="x", pady=5)

            prediction_frame.columnconfigure(0, weight=1)
            prediction_frame.columnconfigure(1, weight=1)

            name_label.grid(row=0, column=0, columnspan=2)
            prediction1_label.grid(row=1, column=0)
            prediction2_label.grid(row=1, column=1)

            

    def _load_photo(self, path):
        with Image.open(path) as img:
            resized = ImageOps.pad(
                img.convert("RGB"),
                (320, 240),
                color="black"
            )
        return ImageTk.PhotoImage(resized)

    def set_refresh_callback(self, callback=None):
        self.button.configure(command=callback)