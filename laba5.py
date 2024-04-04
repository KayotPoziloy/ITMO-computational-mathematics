import math


class Result:

    def first_function(x: float, y: float):
        return math.sin(x)

    def second_function(x: float, y: float):
        return (x * y) / 2

    def third_function(x: float, y: float):
        return y - (2 * x) / y

    def fourth_function(x: float, y: float):
        return x + y

    def default_function(x: float, y: float):
        return 0.0

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        else:
            return Result.default_function

    #
    # Complete the 'solveByEuler' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    def solveByEuler(f, epsilon, a, y_a, b):
        function = Result.get_function(f)
        h = epsilon / 10  # Начальное значение шага

        while abs(a - b) > epsilon:
            y_b = y_a + h * function(a, y_a)  # Вычисляем новое значение y(b) по методу Эйлера
            a += h  # Увеличиваем x на шаг h
            y_a = y_b  # Обновляем значение y(a) для следующей итерации

        return y_b



if __name__ == '__main__':
    f = int(input().strip())

    epsilon = float(input().strip())

    a = float(input().strip())

    y_a = float(input().strip())

    b = float(input().strip())

    result = Result.solveByEuler(f, epsilon, a, y_a, b)

    print(str(result) + '\n')
