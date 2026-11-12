from Percy import Percy
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

    def run(self):
        self.train()
        self.test()

    def _normalize_inputs(self):
        return np.asarray(self.inputs, dtype=float) / 255.0

    def train(self):
        self.brain.train(self.train_inputs, self.train_labels)

    def test(self):
        total = len(self.test_labels)
        correct = 0
        wrong = 0
        for i in range(total):
            if self.check_prediction(self.test_inputs[i], self.test_labels[i]): correct += 1
            else: wrong += 1

        # output results
        print(f"Percy classified correctly: {correct}")
        print(f"Percy classified incorrectly: {wrong}")
        print(f"Accuracy: {(correct / total) * 100}%")

    def check_prediction(self, input, label):
        return self.brain.predict(input) == label
        
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