import numpy as np


def signed_dist(point, theta, theta_0):
    dotProduct = np.dot(point, theta)
    linearClassifier = np.absolute(dotProduct + theta_0)
    squareRoots = np.sqrt(np.square(theta[0]) + np.square(theta[1]))
    return linearClassifier/squareRoots
