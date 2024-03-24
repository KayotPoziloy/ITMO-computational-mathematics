
# Метод Гаусса-Зейделя
class Result:
    isMethodApplicable = True
    errorMessage = ""
    #
    # Complete the 'solveByGaussSeidel' function below.
    #
    # The function is expected to return a DOUBLE_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. 2D_DOUBLE_ARRAY matrix
    #  3. INTEGER epsilon
    #

    def solveByGaussSeidel(n, matrix, epsilon):
        x = [0]*n  # Инициализация массива значений неизвестных
        isMethodApplicable = True

        # Проверка на диагональное преобладание, дописать с переставлением строк
        for i in range(n):
            sum_val = sum(abs(matrix[i][j]) for j in range(n))  # сумма модулей значений строки в матрице
            diag_val = abs(matrix[i][i])  # элемент диагонали
            if 2*diag_val <= sum_val:  # проверка на диагональное преобладание
                isMethodApplicable = False
                break

        if not isMethodApplicable:
            Result.isMethodApplicable = False
            Result.errorMessage = ("The system has no diagonal dominance for this method."
                                   " Method of the Gauss-Seidel is not applicable.")
            return


        # Итерационный метод Зейделя
        for _ in range(1000):  # цикл выполняется пока не будет достигнута допустимая погрешность
            max_diff = 0  # Максимальная разница между предыдущим и текущим значением
            for i in range(n):  # Выполняет итерацию Зейделя
                # коэф при свободном члене первой строки на диагональный элемент строки
                new_x = matrix[i][n] / matrix[i][i]
                for j in range(n):
                    if j != i:
                        new_x -= matrix[i][j] / matrix[i][i]*x[j]

                # Проверка сходимости по epsilon
                max_diff = max(max_diff, abs(new_x - x[i]))
                x[i] = new_x

            if max_diff < epsilon:
                break
        return x


if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n+1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())

    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}")


