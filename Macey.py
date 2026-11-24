import random

class Macey:
    def __init__(self, goey, pixie, alan):
        self.goey = goey
        self.pixie = pixie
        self.alan = alan

    def run(self):
        self.pixie.run(self.alan)

        self.goey.set_refresh_callback(self.refresh)

        self.refresh()
        self.goey.run()

    def refresh(self):
        pick1, pick2 = self.pick_images()
        predictions = {}

        images = (
            self.pixie.assets[pick1], 
            self.pixie.assets[pick2]
            )
        
        labels = (
            self.pixie.classifiers[self.pixie.labels[pick1]], 
            self.pixie.classifiers[self.pixie.labels[pick2]]
            )
        
        input1, input2 = (
            self.pixie.inputs[pick1], 
            self.pixie.inputs[pick2]
            )

        for model in self.pixie.models:
            prediction1 = self.pixie.classifiers[model.predict_one(input1)]
            prediction2 = self.pixie.classifiers[model.predict_one(input2)]
        
            predictions[model.name] = (prediction1, prediction2)

        self.goey.update_widgets(images, predictions, labels)

    def pick_images(self):
        return (random.randrange(len(self.pixie.assets)), random.randrange(len(self.pixie.assets)))