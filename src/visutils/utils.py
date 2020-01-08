from functools import partial

import numpy as np
from scipy.interpolate import UnivariateSpline
from sklearn.base import BaseEstimator


def compute_total_distances(array, distance):
    """Computes the total distance between each point.

    .. math::
        f(x)_m = \sum_{n=1}^m d(x_n, x_n-1)
    """
    array = np.asarray(array)
    if array.ndim < 2:
        array = np.atleast_2d(array).T

    if not callable(distance):
        p = distance
        def distance(x, y):
            reduce_axes = tuple(range(1, array.ndim))
            return np.linalg.norm(x - y, p, axis=reduce_axes)

    distances = distance(array[1:], array[:-1])
    return np.concatenate(([0], np.cumsum(distances)))


def bisection_solve(left, right, f, target, eps=1e-16):
    eps = abs(right - left)*eps
    f_left = f(left) - target
    f_right = f(right) - target

    while abs(right - left) > eps:
        middle = (right + left)/2
        f_middle = f(middle) - target

        if np.sign(f_middle) == np.sign(f_left):
            left = middle
            f_left = f_middle
        else:
            right = middle
            f_right = f_middle


class UniformResampler(BaseEstimator):
    """Resample and interpolate a 2D array to have equidistant elements across the first axis-
    """

    def __init__(
        self,
        num_points=None,
        resampling_rate=None,
        spline_degree=1,
        smoothing_factor=0,
        distance_function=None,
    ):
        self.num_points = num_points
        self.resampling_rate = resampling_rate
        self.num_points = num_points
        self.spline_degree = spline_degree
        self.smoothing_factor = smoothing_factor
        self.distance_function = distance_function

    def fit(self, array):
        array = np.asarray(array)
        if array.ndim < 2:
            array = np.atleast_2d(array).T
        self.array_ = array
        self.reinterpolated_indices_ = self.find_reinterpolation_indices(array)
        self.reinterpolated_data_ = self.reinterpolate(array, self.reinterpolated_indices_)

    def predict(self):
        return self.reinterpolated_data_

    def fit_predict(self, array):
        self.fit(array)
        return self.predict()

    def distance(self, x, y):
        """Measure the distance between x and y.
        """
        if callable(self.distance_function):
            return self.distance_function(x, y)

        p = self.distance_function
        reduce_axes = tuple(range(1, x.ndim))
        return np.linalg.norm(x - y, p, axis=reduce_axes)

    def find_reinterpolation_indices(self, array):
        if self.num_points is not None and self.resampling_rate is not None:
            raise ValueError(
                "Cannot set both the number of points and the oversampling degree."
            )
        elif self.num_points is not None:
            num_points = self.num_points
        elif self.resampling_rate is not None:
            num_points = self.resampling_rate * len(array)
        else:
            num_points = 10 * len(array)

        distances = compute_total_distances(array, self.distance_function)
        distance_interpolant = UnivariateSpline(
            x=np.arange(0, len(distances)),
            y=distances,
            k=self.spline_degree,
            s=self.smoothing_factor,
        )
        spacing = distances[-1] / (num_points - 1)
        max_length = len(distances) / 4

        indices = [0]
        for index in range(1, num_points - 1):
            distance_function = partial(
                self.distance_function
            target = spacing * index
            indices.append(
                bisection_solve(
                    left=0,
                    right=len(distances)-1,
                    target=target,
                    f=,
                )
            """
            indices.append(
                newton_solve(
                    x0=2 * max_length,
                    target=target,
                    f=distance_interpolant,
                    df=distance_interpolant.derivative(),
                    max_length=max_length,
                    eps=1e-10 * spacing,
                )
            )
            """
        indices.append(len(distances)-1)

        return indices

    def reinterpolate(self, array, reinterpolation_indices):
        interpolators = [
            UnivariateSpline(
                x=np.arange(0, len(array)),
                y=array[:, i],
                k=self.spline_degree,
                s=self.smoothing_factor,
            )
            for i in range(array.shape[1])
        ]
        
        return np.array([i(reinterpolation_indices) for i in interpolators]).T
