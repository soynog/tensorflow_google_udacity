print("BUILDING GRAPH IN TENSORFLOW WITH RELUS...")

batch_size = 128
n_h1 = 1024

graph = tf.Graph()
with graph.as_default():

    # Input data. For the training data, we use a placeholder that will be fed
    # at run time with a training minibatch.
    tf_train_dataset = tf.placeholder(tf.float32,
                                    shape=(batch_size, image_size * image_size))
    tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, num_labels))
    tf_valid_dataset = tf.constant(valid_dataset)
    tf_test_dataset = tf.constant(test_dataset)

    # Variables.
    weights = {
        'h1': tf.Variable(tf.random_normal([image_size * image_size, n_h1])),
        'out': tf.Variable(tf.random_normal([n_h1, num_labels]))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([n_h1])),
        'out': tf.Variable(tf.random_normal([num_labels]))
    }

    # buils a neural network model with relus
    def neural_net_relus(x):
        # Hidden fully connected layer with 256 neurons
        h1_layer = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
        h1_layer = tf.nn.relu(h1_layer)
        # Output fully connected layer with a neuron for each class
        out_layer = tf.matmul(h1_layer, weights['out']) + biases['out']
        return out_layer

    # Training computation.
    logits = neural_net_relus(tf_train_dataset)
    loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=tf_train_labels, logits=logits))

    # Optimizer.
    optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    # Predictions for the training, validation, and test data.
    train_prediction = tf.nn.softmax(logits)
    valid_prediction = tf.nn.softmax(neural_net_relus(tf_valid_dataset))
    test_prediction = tf.nn.softmax(neural_net_relus(tf_test_dataset))
