from Percy import Percy
from PIL import Image
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split

class Pixie:
    '''
        Meet Pixie. A drug addict in recovery.
        instead of meph, Prixie setteled on pixels.
        He reads images, turn them into juicy numpy pixel arrays, and feeds them
        to this cousion Percy, teaching him to classify them. 
    '''
    def __init__(self):
        self.brain = Percy(3)
        self.classifiers = {
            "land": 0,
            "sea": 1
        }
        self.file_format = "jpg"
        self.assets = Path(__file__).resolve().parent / "assets"
        self.assets_count = self._count_files(self.assets)

    def _count_files(self, folder):
        return sum(1 for item in folder.iterdir() if item.is_file())

    def run(self):
        inputs, labels = self._parse_images()
        self.normalize(inputs)
        train_inputs, test_inputs, train_labels, test_labels = self._train_test_split(inputs, labels)
        self.train(train_inputs, train_labels)
        self.test(test_inputs, test_labels)


    def normalize(self, inputs):
        inputs = np.asarray(inputs, dtype=float) / 255.0

    def train(self, inputs, labels):
        self.brain.train(inputs, labels)


    def test(self, inputs, labels):
        total = len(labels)
        correct = 0
        wrong = 0
        for i in range(total):
            if self.brain.predict(inputs[i]) == labels[i]: 
                correct+=1
            else:
                wrong+=1

        # output results
        print(f"Percy classified correctly: {correct}")
        print(f"Percy classified incorrectly: {wrong}")
        print(f"Accuracy: {(correct / total) * 100}%")


    def _parse_images(self) -> tuple:
        inputs = []
        labels = []

        # iterate over all of the images, and build the inputs, labels lists
        for dir in self.classifiers.keys():
            curr_dir = curr_dir = self.assets / dir
            for i in range(1, self._count_files(curr_dir) + 1):
                # open the current image
                with Image.open(rf"{curr_dir}/{dir}{i}.{self.file_format}") as img:
                    # convert to a numpy array
                    arr = np.array(img, dtype=np.uint8)

                # update inputs and labels accordignly
                inputs.append(self._get_color_averages(arr))
                labels.append(self.classifiers[dir])
        return (inputs, labels)
        
        
    def _get_color_averages(self, arr) -> tuple:
        return (
            arr[:,:,0].mean(),
            arr[:,:,1].mean(),
            arr[:,:,2].mean()
        )

    def _train_test_split(self, inputs, labels) -> tuple:
        return train_test_split(
            inputs,
            labels,
            test_size=0.2,
            stratify=labels,
            random_state=42
        )