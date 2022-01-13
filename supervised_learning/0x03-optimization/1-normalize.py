#!/usr/bin/env python3
""" defines a function hat normalizes (standardizes) a matrix """


def normalize(X, m, s):
    """ function that normalizes (standardizes) a matrix

    Args:
        X: `numpy.ndarray` of shape `(d, nx)` to normalize, where
            `d` is the number of data points and
            `nx` is the number of features
        m: `numpy.ndarray` of shape `(nx,)` that contains the mean of all
            features of `X`
        s: `numpy.ndarray` of shape `(nx,)` that contains the standard
        deviation of all features of `X`

    Returns: The normalized `X` matrix
    """

    X -= m
    X /= s

    return X


if __name__ == '__main__':
    """ test """
    normalization_constants = __import__(
        '0-norm_constants').normalization_constants
    np.random.seed(0)
    a = np.random.normal(0, 2, size=(100, 1))
    b = np.random.normal(2, 1, size=(100, 1))
    c = np.random.normal(-3, 10, size=(100, 1))
    X = np.concatenate((a, b, c), axis=1)
    m, s = normalization_constants(X)
    print(X[:10])
    X = normalize(X, m, s)
    print(X[:10])
    m, s = normalization_constants(X)
    print(m)
    print(s)
