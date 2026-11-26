import numpy as np
class Percy:
    def __init__(self, number_entrances, epohcs=1000, learning_rate=0.01):
        self.bias = 0.0
        self.learning_rate = learning_rate
        self.number_entrances = number_entrances
        self.weights = np.zeros(number_entrances)
        self.epohcs = epohcs
        self.name = "Percy"

    def get_bias(self) -> float:
        return self.bias

    def get_input_weights(self) -> np.array:
        return self.weights

    def get_name(self):
        return self.name

    def activation(self, prediction) -> int:
        if prediction > 0: return 1
        return 0

    def train(self, inputs, labels, on_epoch_end=None):
        inputs = np.asarray(inputs, dtype=float)

        for j in range(self.epohcs):
            for sample, label in zip(inputs, labels):
                prediction = self.predict_one(sample)

                self.weights += (label - prediction) * sample * self.learning_rate
                self.bias += (label - prediction) * self.learning_rate

            if j % 10 == 0 or j == self.epohcs - 1:
                if on_epoch_end is not None:
                    on_epoch_end(self.name, self.weights.copy(), self.bias)

    def predict_one(self, input) -> int:
        sum = np.dot(self.weights, input) + self.bias
        return self.activation(sum)

    def test(self, inputs, labels, on_test_end=None):
        correct = 0
        wrong = 0

        for sample, label in zip(inputs, labels, strict=True):
            if self.predict_one(sample) == label: correct += 1
            else: wrong += 1

        accuracy = correct / (correct + wrong)
        loss = wrong / (correct + wrong)

        if on_test_end is not None:
            on_test_end(self.name, loss, accuracy)