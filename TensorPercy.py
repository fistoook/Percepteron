import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

import tensorflow as tf
import numpy as np

class TensorPercy(tf.keras.Sequential):
    '''
        Using the ready to go Percepteron from tensor flow, in order to
        a) learn new activation function types and
        b) compare?!
    '''
    def __init__(self, number_entrances, epohcs=100, learning_rate=0.01):
        super().__init__([tf.keras.layers.Dense(
            1, activation="sigmoid", input_shape=(number_entrances,))])

        self.epochs = epohcs

        self.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate), 
            loss='binary_crossentropy', 
            metrics =['accuracy']
        )

    def train(self, train_inputs, train_labels, on_epoch_end):
        self.fit(
            np.array(train_inputs, dtype=float),
            np.array(train_labels, dtype=float),
            epochs=self.epochs, verbose=2
        )

    def print_results(self):
        print("Predictions:")
        print(self.predict(self.pixie.test_inputs))
        loss, accuracy = self.evaluate(
            np.array(self.pixie.test_inputs, dtype=float),
            np.array(self.pixie.test_labels, dtype=float), 
            verbose=0)
        print(f"loss={loss} acuracy={accuracy}")