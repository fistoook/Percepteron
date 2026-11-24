import random

class Macey:
    def __init__(self, goey, pixie, alan):
        self.goey = goey
        self.pixie = pixie
        self.alan = alan

    def run(self):
        self.pixie.run(self.alan)

        self.goey.button.configure(command=self.refresh)

        self.refresh()
        self.goey.mainloop()

    def refresh(self):
        pick1, pick2 = self.pick_images()

        images = (self.pixie.assets[pick1], self.pixie.assets[pick2])
        labels = (self.pixie.labels[pick1], self.pixie.labels[pick2])
        inputs = (self.pixie.inputs[pick1], self.pixie.inputs[pick2])
        predictions = (self.pixie.percy.predict_one(inputs[0]),
                       self.pixie.percy.predict_one(inputs[1]))

        self.goey.update_widgets(images, predictions, labels)

    def pick_images(self):
        return (random.randrange(len(self.pixie.assets)), random.randrange(len(self.pixie.assets)))