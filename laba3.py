import math

k = 0.4
a = 0.9


def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return math.tan(args[0] * args[1] + k) - pow(args[0], 2)


def fourth_function(args: []) -> float:
    return a * pow(args[0], 2) + 2 * pow(args[1], 2) - 1


def fifth_function(args: []) -> float:
    return pow(args[0], 2) + pow(args[1], 2) + pow(args[2], 2) - 1


def six_function(args: []) -> float:
    return 2 * pow(args[0], 2) + pow(args[1], 2) - 4 * args[2]


def seven_function(args: []) -> float:
    return 3 * pow(args[0], 2) - 4 * args[1] + pow(args[2], 2)


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        k = 0.4
        a = 0.9
        return [third_function, fourth_function]
    elif n == 3:
        k = 0
        a = 0.5
        return [third_function, fourth_function]
    elif n == 4:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    funcs = get_functions(system_id)

    # Функция вычисляет производную по index заданной функции func в точке args
    # использует метод конечных разностей
    def derivative(func, args, index, h=1e-5):
        args_plus_h = args.copy()
        args_minus_h = args.copy()
        args_plus_h[index] += h
        args_minus_h[index] -= h
        return (func(args_plus_h) - func(args_minus_h)) / (2 * h)

    # Строит Якобиан матрицу для функций
    def jacobian_matrix(functions, variables):
        jacobian = [[0 for _ in range(len(variables))] for _ in range(len(functions))]
        for i, func in enumerate(functions):
            for j in range(len(variables)):
                jacobian[i][j] = derivative(func, variables, j)
        return jacobian

    # Умножение матрицы A на матрицу B
    def matrix_multiplication(A, B):
        result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        return result

    # Метод Жордана-Гаусса для решения слу
    def gauss_jordan(m, eps=1.0 / (10 ** 10)):
        (h, w) = (len(m), len(m[0]))
        for y in range(0, h):
            maxrow = y
            for y2 in range(y + 1, h):
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2
            (m[y], m[maxrow]) = (m[maxrow], m[y])
            if abs(m[y][y]) <= eps:
                return False
            for y2 in range(y + 1, h):
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h - 1, 0 - 1, -1):
            c = m[y][y]
            for y2 in range(0, y):
                for x in range(w - 1, y - 1, -1):
                    m[y2][x] -= m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):
                m[y][x] /= c
        return True

    # Вычисляет обратную матрицу с использованием метода Жордана-Гаусса
    def inverse(matrix):
        tmp = [[] for _ in matrix]
        for i, row in enumerate(matrix):
            assert len(row) == len(matrix)
            tmp[i].extend(row + [0] * i + [1] + [0] * (len(matrix) - i - 1))
        gauss_jordan(tmp)
        inv = []
        for i in range(len(tmp)):
            inv.append(tmp[i][len(tmp[i]) // 2:])
        return inv

    # Вычисляет разность двух векторов
    def subtract_vectors(a, b):
        return [a_i - b_i for a_i, b_i in zip(a, b)]

    # Вычисляет значения функций для заданных значений
    def calculate_function_values(functions, variables):
        return [func(variables) for func in functions]

    x = initial_approximations
    for _ in range(100):  # Max iterations
        Fx = calculate_function_values(funcs, x)
        J = jacobian_matrix(funcs, x)
        J_inv = inverse(J)
        delta_x = matrix_multiplication(J_inv, [[fx_i] for fx_i in Fx])
        x = subtract_vectors(x, [delta_x_i[0] for delta_x_i in delta_x])
        if all(abs(delta_x_i[0]) < 1e-5 for delta_x_i in delta_x):  # Convergence criterion
            break

    return [round(xi, 5) for xi in x]


if __name__ == '__main__':
    # Номер системы
    system_id = int(input('Введи k: ').strip())

    # кол-во неизвестных и ур-ий
    number_of_unknowns = int(input('Введи кол-во неизвестных: ').strip())

    # начальные приближения
    initial_approximations = []
    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input('Введи начально приближение: ').strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))
    print('\n')
