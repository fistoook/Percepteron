import numpy as np

class Percy:
    '''
        Meet Percy, a percepteron. 
        All he needs is the number of parameters - from which he derives the weight vector, initializing it and the bias.
        With a prediction method of vector multiplying inputs by weights, adding bias, 
        and deciding with the activation funciton the classification, it learns by comparing
        his predicition to the actual label, and adjusting accordingly.
        In an Interview Percy mentions the motivation to become Nora. one day :)
    '''
    def __init__(self, number_entrances, epohcs=1000, learning_rate=0.01):
        self.bias = 1 
        self.learning_rate = learning_rate
        self.number_entrances = number_entrances
        self.weights = np.zeros(number_entrances)
        self.epohcs = epohcs

    def activation(self, prediction) -> int:
        if prediction > 0: return 1
        return 0

    def predict(self, input) -> int:
        sum = np.dot(self.weights, input) + self.bias
        return self.activation(sum)

    def train(self, inputs, labels):
        inputs = np.asarray(inputs, dtype=float)
        for _ in range(self.epohcs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                self.weights += (labels[i] - prediction) * inputs[i] * self.learning_rate
                self.bias += (labels[i] - prediction) * self.learning_rate