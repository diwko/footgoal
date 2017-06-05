import numpy as np
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
import os


def get_installation_dir():
    return os.path.dirname(os.path.abspath(__file__))


def y_convert(ar):
    for i in range(ar.size):
        if ar[i] > 0:
            ar[i] = 1
        elif ar[i] < 0:
            ar[i] = -1


def create_model():
    learn_x = np.loadtxt(get_installation_dir() + '/data/learning_data.csv',
                         dtype=int, delimiter=";", skiprows=0,
                         usecols=range(0, 9))
    learn_y = np.loadtxt(get_installation_dir() + '/data/learning_data.csv',
                         dtype=int, delimiter=";", skiprows=0, usecols=9)

    y_convert(learn_y)

    classifier = LogisticRegression()
    classifier.fit(learn_x, learn_y)

    joblib.dump(classifier, get_installation_dir() + '/data/classifier_model')


def test_model(test_data):
    test_x = np.loadtxt(get_installation_dir() + test_data,
                        dtype=int, delimiter=";", skiprows=0,
                        usecols=range(0, 9))
    test_y = np.loadtxt(get_installation_dir() + test_data,
                        dtype=int, delimiter=";", skiprows=0, usecols=9)

    y_convert(test_y)

    classifier = joblib.load(os.path.dirname(os.path.abspath(__file__)) +
                             '/data/classifier_model')

    return classifier.score(test_x, test_y)
