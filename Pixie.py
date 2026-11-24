from Percy import Percy
from TensorPercy import TensorPercy
from PIL import Image
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split

ASSETS =  Path(__file__).resolve().parent / "assets"

class Pixie:
    def __init__(self):
        self.percy = Percy(3)  
        self.tensor_percy = TensorPercy(3)
        self.tensor_precy_tanh = TensorPercy(3, activation="tanh")

        self.models = [self.percy, self.tensor_percy, self.tensor_precy_tanh]

        self.classifiers = {
            0: "Land",
            1: "Sea"
        }

        self.assets = self._prepare_assets()

        self.inputs, self.labels = self._parse_images()

        self.inputs = self._normalize_inputs()

        self.train_inputs, self.test_inputs, self.train_labels, self.test_labels = self._train_test_split()
        
    def _prepare_assets(self) -> list:
        assets = []
        dirs = (ASSETS / "land", ASSETS / "sea")
        classifier = 0

        for dir in dirs:
            for item in dir.iterdir():
                if item.is_file():
                    assets.append((item, classifier))

            classifier += 1

        return assets

    def _parse_images(self) -> tuple:
        inputs = []
        labels = []

        # iterate over all of the images, and build the inputs, labels lists
        for tuple in self.assets:
            # open the current image
            file = tuple[0]
            classifier = tuple[1]
            with Image.open(file) as img:
                # convert to a numpy array
                arr = np.array(img, dtype=np.uint8)

            # update inputs and labels accordignly
            inputs.append(self._get_color_averages(arr))
            labels.append(classifier)

        return (inputs, labels) 

    def _get_color_averages(self, arr) -> tuple:
        return (
            arr[:,:,0].mean(),
            arr[:,:,1].mean(),
            arr[:,:,2].mean()
        )

    
    def _train_test_split(self) -> tuple:
        return train_test_split(
            self.inputs,
            self.labels,
            test_size=0.2,
            stratify=self.labels,
            random_state=42
        )  

    def _normalize_inputs(self):
        return np.asarray(self.inputs, dtype=float) / 255.0 

    def run(self, alan):
        self.train(alan.update_terminal)
        self.test(alan.display_results)

    def train(self, on_epohc_end=None):
        for model in self.models:
            model.train(self.train_inputs, self.train_labels, on_epoch_end=on_epohc_end)

    def test(self, on_test_end=None):
        for model in self.models:
            model.test(self.train_inputs, self.train_labels, on_test_end=on_test_end)