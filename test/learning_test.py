from footgoal.learning import y_convert
import numpy as np


def test_y_convert():
    y = np.array([0, 10, -5, -5, 15])
    y_convert(y)
    assert np.array_equal(np.array([0, 1, -1, -1, 1]), y)