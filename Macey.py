from pathlib import Path
import random

class Macey:
    '''
        Macey has a big heart. she is the MCV.
        She acts as the man in the middle - in the good sense- 
        between the Goey GUI and the Pixie image classification model.
    '''
    def __init__(self, goey, model, terminal_interface):
        self.goey = goey
        self.model = model
        self.terminal_interface = terminal_interface

    def run(self):
        self.model.run(self.terminal_interface)

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