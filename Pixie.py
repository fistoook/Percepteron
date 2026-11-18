from Percy import Percy
from TensorPercy import TensorPercy
from PIL import Image
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split

ASSETS =  Path(__file__).resolve().parent / "assets"

class Pixie:
    '''
        Meet Pixie. A drug addict in recovery.
        instead of meph, Prixie setteled on pixels.
        He reads images, turn them into juicy numpy pixel arrays, and feeds them
        to his cousion Percy, teaching him to classify them. 
    '''
    def __init__(self):
        self.brain = Percy(3)  
        self.tensor_brain = TensorPercy(3)

        self.classifiers = {
            "land": 0,
            "sea": 1
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

    def _normalize_inputs(self):
        return np.asarray(self.inputs, dtype=float) / 255.0 

    def run(self, terminal_interface):
        self.train(terminal_interface.update_terminal)
        self.test()

    def train(self, on_epohc_end=None):
        self.brain.train(self.train_inputs, self.train_labels, on_epoch_end=on_epohc_end)
        self.tensor_brain.train(self.train_inputs, self.train_labels, on_epoch_end=on_epohc_end)

    def test(self):
        total = len(self.test_labels)
        percy_correct = 0
        percy_wrong = 0
        tensor_correct = 0
        tensor_wrong = 0

        for i in range(total):
            percy_prediction, tensor_prediction = self.check_prediction(self.test_inputs[i], self.test_labels[i])
            tensor_classification = (tensor_prediction >= 0.5).astype(int)

            if percy_prediction: percy_correct += 1
            else: percy_wrong += 1

            if tensor_classification: tensor_correct += 1
            else: tensor_wrong += 1

        # output results
        print(f"Percy classified correctly: {percy_correct}")
        print(f"Percy classified incorrectly: {percy_wrong}")
        print(f"Accuracy: {(percy_correct / total) * 100}%\n")
        print(f"Tensor classified correctly: {tensor_correct}")
        print(f"Tensor classified incorrectly: {tensor_wrong}")
        print(f"Accuracy: {(percy_correct / total) * 100}%")

    def check_prediction(self, input, label) -> tuple:
        return self.brain.predict(input) == label, self.tensor_brain.predict(np.array([input]))
        
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

    def _random_land(self):
        pass

    def _random_sea(self):
        pass