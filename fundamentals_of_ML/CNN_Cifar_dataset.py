# Learn about the CIFA-10 dataset -> https://www.cs.toronto.edu/~kriz/cifar.html


import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# normalize pixel values to be between 0 and 1

train_images = train_images / 255.0
test_images = test_images / 255.0

FIRST_LAYER = layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3))#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_1 = layers.MaxPooling2D(2, 2)#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_2 = layers.Conv2D(64, (3, 3), activation='relu')#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_3 = layers.MaxPooling2D(2, 2)#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_4 = layers.Conv2D(64, (3, 3), activation='relu')#YOUR CODE HERE#
HIDDEN_LAYER_TYPE_5 = layers.Dense(128, activation='relu')#YOUR CODE HERE#
LAST_LAYER = layers.Dense(10, activation='softmax')#YOUR CODE HERE#

model = models.Sequential([
       FIRST_LAYER,
       HIDDEN_LAYER_TYPE_1,
       HIDDEN_LAYER_TYPE_2,
       HIDDEN_LAYER_TYPE_3,
       HIDDEN_LAYER_TYPE_4,
       layers.Flatten(),
       HIDDEN_LAYER_TYPE_5,
       LAST_LAYER,
])

LOSS = 'sparse_categorical_crossentropy' #YOUR CODE HERE#
NUM_EPOCHS = 20 #You can change this value if you like to experiment with it to get better accuracy

# Compile the model
model.compile(optimizer='sgd',
              loss=LOSS,
              metrics=['accuracy'])

# Fit the model
history = model.fit(train_images, train_labels, epochs=NUM_EPOCHS, 
                    validation_data=(test_images, test_labels))

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.xlim([0,NUM_EPOCHS])
plt.ylim([0.4,1.0])
plt.show()