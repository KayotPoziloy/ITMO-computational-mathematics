import math
import os
import random
import re
import sys

#
# Complete the 'approximate_linear_least_squares' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY x_axis
#  2. DOUBLE_ARRAY y_axis
#


def approximate_linear_least_squares(x_axis, y_axis):
    # подготовка данных
    xySum = sum([i*j for i, j in zip(x_axis, y_axis)])
    xSum = sum(x_axis)
    ySum = sum(y_axis)
    xCuadSum = sum([i**2 for i in x_axis])

    # Вычисление коэффициентов линейной аппроксимации
    a = (axis_count*xySum - xSum*ySum)/(axis_count*xCuadSum - xSum**2)
    b = (ySum - a*xSum)/axis_count

    # Вычисление отклонений
    max_deviation = max(abs(y - (a * x + b)) for x, y in zip(x_axis, y_axis))

    return max_deviation**2

# axis_count = 5
# x = [1, 2, 3, 4, 5]
# y = [1.1, 3.8, 6.5, 10.2, 13.1]
# approximate_linear_least_squares(x, y)


if __name__ == '__main__':
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    result = approximate_linear_least_squares(x_axis, y_axis)

    print(str(result) + '\n')