import numpy as np
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression


def y_convert(ar):
    for i in range(ar.size):
        if ar[i] > 0:
            ar[i] = 1
        elif ar[i] < 0:
            ar[i] = -1


learn_X = np.loadtxt('data/learning_data.csv', dtype=int, delimiter=";", skiprows=0,
                     usecols=range(0, 9))
learn_Y = np.loadtxt('data/learning_data.csv', dtype=int, delimiter=";", skiprows=0,
                     usecols=9)

y_convert(learn_Y)

classifier = LogisticRegression()
classifier.fit(learn_X, learn_Y)

#joblib.dump(classifier, 'data/classifier_model')

test_X = np.loadtxt('data/test_data.csv', dtype=int, delimiter=";", skiprows=0,
                     usecols=range(0, 9))
test_Y = np.loadtxt('data/test_data.csv', dtype=int, delimiter=";", skiprows=0,
                     usecols=9)

y_convert(test_Y)


print(classifier.score(test_X, test_Y))
