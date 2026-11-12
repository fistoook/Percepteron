from pathlib import Path
import random

class Macey:
    def __init__(self, goey, model):
        self.goey = goey
        self.model = model

    def run(self):
        self.model.run()

        self.goey.button.configure(command=self.refresh)

        self.refresh()
        self.goey.mainloop()

    def refresh(self):
        pick1, pick2 = self.pick_images()

        images = (self.model.assets[pick1], self.model.assets[pick2])
        labels = (self.model.labels[pick1], self.model.labels[pick2])
        inputs = (self.model.inputs[pick1], self.model.inputs[pick2])
        predictions = (self.model.brain.predict(inputs[0]),
                       self.model.brain.predict(inputs[1]))

        self.goey.update_widgets(images, predictions, labels)

    def pick_images(self):
        return (random.randrange(len(self.model.assets)), random.randrange(len(self.model.assets)))