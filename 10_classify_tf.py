# Classify data using a basic TF model

print("CLASSIFYING...")

import tensorflow as tf
from tensorflow import keras

# Build the Model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

letter_labels = ['a','b','c','d','e','f','g','h','i','j']

# Configure optimizer, loss function, and monitoring metrics.
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model on dataset
model.fit(train_dataset, train_labels, epochs=5)

# See how trained model performs on test set
test_loss, test_acc = model.evaluate(test_dataset, test_labels)
print('Test accuracy: ', test_acc)

# Make some predictions
predictions = model.predict(test_dataset)

# Plot the first 25 test images, their predicted label, and the true label
# Color correct predictions in green, incorrect predictions in red
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid('off')
    plt.imshow(test_dataset[i], cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]
    if predicted_label == true_label:
      color = 'green'
    else:
      color = 'red'
    plt.xlabel("{} ({})".format(letter_labels[predicted_label],
                                  letter_labels[true_label]),
                                  color=color)

plt.show()
