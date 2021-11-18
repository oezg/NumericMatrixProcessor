import copy


def show_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def axis_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")


def get_choice(choices: set) -> int:
    while True:
        choice = input("Your choice: ")
        if choice in choices:
            return int(choice)


def print_matrix(matrix):
    if isinstance(matrix, str):
        print(matrix)
    print("The result is:")
    if isinstance(matrix, (float, int)):
        print(matrix)
    elif isinstance(matrix, list):
        for row in matrix:
            print(*map(lambda x: str(round(x, 3)).rjust(6), row))
    print()


def get_matrices():
    rows_1, cols_1 = [int(x) for x in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:")
    first_matrix = [[float(x) for x in input().split()] for _ in range(rows_1)]
    rows_2, cols_2 = [int(x) for x in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:")
    second_matrix = [[float(x) for x in input().split()] for _ in range(rows_2)]
    return first_matrix, second_matrix


def get_matrix():
    rows, columns = [int(x) for x in input("Enter size of matrix: ").split()]
    print("Enter matrix:")
    return [[float(x) for x in input().split()] for _ in range(rows)]


def add_matrices():
    first, second = get_matrices()
    if len(first) == len(second) and len(first[0]) == len(second[0]):
        return [[f + s for f, s in zip(F, S)] for F, S in zip(first, second)]
    return "The operation cannot be performed."


def scalar_multiplication():
    matrix = get_matrix()
    scalar = float(input("Enter constant: "))
    return scale(matrix, scalar)


def scale(matrix, scalar):
    return [[scalar * x if x else 0 for x in row] for row in matrix]


def matrix_multiplication():
    first, second = get_matrices()
    if len(first[0]) == len(second):
        sec = transpose(second)
        return [[sum(f * s for f, s in zip(row, col)) for col in sec] for row in first]
    return "The operation cannot be performed."


def transpose(matrix, axis=1):
    if axis == 1:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    elif axis == 2:
        return [[matrix[-i-1][-j-1] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    elif axis == 3:
        return [row[::-1] for row in matrix]
    elif axis == 4:
        return [row for row in matrix[::-1]]


def matrix_transposition():
    axis_menu()
    axis_choice = get_choice(set('1234'))
    matrix = get_matrix()
    return transpose(matrix, axis_choice)


def determinant_calculation():
    matrix = get_matrix()
    if len(matrix) == len(matrix[0]):
        return determinant(matrix)
    return "Non square matrix does not have a determinant"


def minor(matrix, i, j):
    minor_matrix = copy.deepcopy(matrix)
    for row in minor_matrix:
        row.pop(j)
    minor_matrix.pop(i)
    return minor_matrix


def cofactor(matrix, i, j):
    return pow(-1, i + j) * determinant(minor(matrix, i, j))


def cofactor_matrix(matrix):
    return [[cofactor(matrix, i, j) for j, _ in enumerate(row)] for i, row in enumerate(matrix)]


def determinant(matrix, i=0):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum(matrix[i][j] * cofactor(matrix, i, j) for j in range(n))


def matrix_inversion():
    matrix = get_matrix()
    return invert(matrix)


def adjugate(matrix):
    return transpose(cofactor_matrix(matrix))


def invert(matrix):
    try:
        return scale(adjugate(matrix), pow(determinant(matrix), -1))
    except ZeroDivisionError:
        return "This matrix doesn't have an inverse."


def main():
    while True:
        show_menu()
        users_choice = get_choice(set('0123456'))
        if users_choice == 0:
            break
        elif users_choice == 1:
            result = add_matrices()
        elif users_choice == 2:
            result = scalar_multiplication()
        elif users_choice == 3:
            result = matrix_multiplication()
        elif users_choice == 4:
            result = matrix_transposition()
        elif users_choice == 5:
            result = determinant_calculation()
        elif users_choice == 6:
            result = matrix_inversion()
        print_matrix(result)


if __name__ == "__main__":
    main()
