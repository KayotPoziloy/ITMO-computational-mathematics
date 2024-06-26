import math


class Result:
    error_message = ""
    has_discontinuity = False

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
        return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x: float):
        return math.log(x) if x > 0 else math.inf

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
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def func(x):
        return math.sqrt(x - 1)

    def calculate_integral(a, b, f, epsilon):
        # получаем функцию
        function = Result.get_function(f)
        # кол-во трапеций
        n = 1
        s_old = 0
        while True:
            trapeze_len = (b - a)/n

            # площадь каждой трапеции
            s_new = 0.5*(function(a) + function(b))
            for i in range(1, n):
                s_new += (function(a + i*trapeze_len))
            s_new *= trapeze_len

            # проверка погрешности
            if abs(s_old - s_new) < epsilon:
                return s_new
            s_old = s_new
            n += 1

            # проверка на разрыв
            for i in range(n + 1):
                x = a + i * ((b - a)/n)
                if math.isnan(function(x)) or math.isinf(function(x)):
                    Result.has_discontinuity = True
                    Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
                    return 0


if __name__ == '__main__':
    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')
