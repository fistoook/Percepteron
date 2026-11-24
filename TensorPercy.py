import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import numpy as np

class TensorPercy(tf.keras.Sequential):
    def __init__(self, number_entrances, epohcs=100, learning_rate=0.01, activation="sigmoid"):
        try:
            super().__init__([tf.keras.layers.Dense(
                1, activation=activation, input_shape=(number_entrances,))]
            )
        except:
            print("Wrong parameters to TensorPercy")

        self.epochs = epohcs

        self.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate), 
            loss='binary_crossentropy', 
            metrics =['accuracy']
        )
        self.name = "TensorPercy"

    def train(self, inputs, labels, on_epoch_end=None):
        inputs = np.asarray(inputs, dtype=float)
        labels = np.asarray(labels, dtype=float)

        
        def _epohc_handler(epohc, logs):
            weights, bias = self.layers[0].get_weights()
            on_epoch_end(self.name, weights.flatten(), bias[0])

        self.fit(
            inputs,
            labels,
            epochs=self.epochs, 
            verbose=0,
            callbacks=[tf.keras.callbacks.LambdaCallback(on_epoch_end=_epohc_handler)]
        )
            
    def predict_one(self, input) -> int:
        prediction = self.predict(np.array([input]), verbose=0)
        return int((prediction >= 0.5).item(0))

    def test(self, inputs, labels, on_test_end=None):
        loss, accuracy = self.evaluate(
            np.asarray(inputs, dtype=float),
            np.asarray(labels, dtype=float), 
            verbose=0
        )

        on_test_end(loss, accuracy)