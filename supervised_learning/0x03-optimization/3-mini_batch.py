#!/usr/bin/env python3
""" Defines a function that trains a loaded neural network model using
mini-batch gradient descent
"""

import tensorflow.compat.v1 as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """ function that trains a loaded neural network model using mini-batch
    gradient descent

    Args:
    -----
        X_train: numpy.ndarray of shape (m, 784) containing the training data
            m is the number of data points
            784 is the number of input features\n
        Y_train: one-hot numpy.ndarray of shape (m, 10) containing the
            training labels where `10` is the number of classes the model
            should classify\n
        X_valid: numpy.ndarray of shape (m, 784) containing the validation data
        Y_valid: one-hot numpy.ndarray of shape (m, 10) containing the
            validation labels\n
        batch_size: number of data points in a batch\n
        epochs: number of times the training should pass through the whole
            dataset\n
        load_path: path from which to load the model\n
        save_path: path to where the model should be saved after training

    Returns: the path where the model was saved
    """


    # imp meta graph and restore session
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph(load_path + ".meta")
        new_saver.restore(sess, load_path)

        # Get the following tensors and ops from the collection restored
        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        accuracy = tf.get_collection("accuracy")
        loss = tf.get_collection("loss")
        train_op = tf.get_collection("train_op")

        # loop over epochs:
        for epoch in range(epochs):
            # shuffle the data
            X_train, Y_train = shuffle_data(X_train, Y_train)

            train_accuracy = sess.run(
                accuracy, feed_dict={x: X_train, y: Y_train})
            train_cost = sess.run(loss, feed_dict={x: X_train, y: Y_train})
            valid_accuracy = sess.run(
                accuracy, feed_dict={x: X_valid, y: Y_valid})
            valid_cost = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})

            print(f'After {epoch} epochs:')
            print(f'\tTraining Cost: {train_cost[0]}')
            print(f'\tTraining Accuracy: {train_accuracy[0]}')
            print(f'\tValidation Cost: {valid_cost[0]}')
            print(f'\tValidation Accuracy: {valid_accuracy[0]}')

            iteration = 1
            # loop over the batches:
            for batch_start in range(0, X_train.shape[0], batch_size):
                # get X_batch and Y_batch from data
                X_batch = X_train[batch_start:batch_start+batch_size]
                Y_batch = Y_train[batch_start:batch_start+batch_size]

                # train your model
                sess.run(train_op, feed_dict={x: X_batch, y: Y_batch})

                step_accuracy = sess.run(
                    accuracy, feed_dict={x: X_batch, y: Y_batch})
                step_cost = sess.run(loss, feed_dict={x: X_batch, y: Y_batch})

                # After every 100 steps gradient descent within an epoch,
                # the following should be printed:
                if iteration % 100 == 0:
                    print(f'\tStep {iteration}:')
                    print(f'\t\tCost: {step_cost[0]}')
                    print(f'\t\tAccuracy: {step_accuracy[0]}')

                iteration += 1
        print(f'After {epoch + 1} epochs:')
        print(f'\tTraining Cost: {train_cost[0]}')
        print(f'\tTraining Accuracy: {train_accuracy[0]}')
        print(f'\tValidation Cost: {valid_cost[0]}')
        print(f'\tValidation Accuracy: {valid_accuracy[0]}')

        # Save session
        return new_saver.save(sess, save_path)
