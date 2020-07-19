def get_matrix(name=""):
    name = name if name == "" else name + " "
    input_str = input("Enter size of " + name + "matrix: > ")
    if input_str == "1":
        a_n = a_m = 1
    else:
        a_n, a_m = map(int, input_str.split())
    A = list()
    print("Enter matrix:")
    for i in range(a_n):
        A.append(list(map(float, input("> ").split())))
    return A


def pretty_print_result(result=None):
    if result is not None and isinstance(result, list):
        print("The result is:")
        # print(*[' '.join(map(str, result[i])) for i in range(len(result))], sep='\n')
        print('\n'.join([''.join(['{:12}'.format(round(item, 4)) for item in row]) for row in result]))
        print()
    elif result is not None and (not isinstance(result, list)):
        print("The result is:")
        print(result)
        print()
    else:
        print("The operation cannot be performed.")
        print()


def add():
    A = get_matrix("first")
    B = get_matrix("second")
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None

    return [[a + b for a, b in zip(A_row, B_row)] for A_row, B_row in zip(A, B)]


def multiply_by_constant():
    A = get_matrix()
    c = float(input("Enter constant: > "))

    return _multiply_by_constant(A, c)

def _multiply_by_constant(A, c):
    return [[c * a for a in A_row] for A_row in A]



def multiplay_matrices():
    A = get_matrix("first")
    B = get_matrix("second")
    if len(A[0]) != len(B):
        return None
    return [[sum([a * b for a, b in zip(A_row, B_col)]) for B_col in zip(*B)] for A_row in A]


def transpose():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = int(input("Your choice: > "))
    T = get_matrix()
    if choice == 1:
        return t_main_diag(T)
    elif choice == 2:
        return t_side_diag(T)
    elif choice == 3:
        return t_vertical(T)
    elif choice == 4:
        return t_horizontal(T)
    return None


def t_main_diag(A):
    return list(zip(*A))


def t_side_diag(A):
    return t_horizontal(t_vertical(t_main_diag(A)))


def t_horizontal(A):
    return [A_row for A_row in A[::-1]]


def t_vertical(A):
    return [[a for a in A_row[::-1]] for A_row in A]


def determinant():
    A = get_matrix()
    pretty_print_result(_determinant(A))


def _determinant(A):
    if len(A) == len(A[0]) == 1:
        return A[0][0]
    if len(A) == len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0

    for i in range(len(A)):
        det += (-1) ** i * A[0][i] * _determinant(
            [[A[k][l] for l in range(len(A)) if l != i] for k in range(1, len(A))])

    return det

def cofactor_matrix(A):
    Matrix = [[0 for x in range(len(A))] for y in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            Matrix[i][j] = (-1) ** (i+j) * _determinant([[A[k][l] for l in range(len(A)) if l != j] for k in range(len(A)) if k != i])
    return Matrix

def inverse():
    A = get_matrix()
    det = _determinant(A)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        result = cofactor_matrix(A)
        result = t_main_diag(result)
        result = _multiply_by_constant(result, 1/det)
        # result = [[round(r, 4) for r in res_row] for res_row in result]
        pretty_print_result(result)


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    return int(input("Your choice: > "))


answer = menu()

while answer != 0:
    if answer == 1:
        pretty_print_result(add())
    elif answer == 2:
        pretty_print_result(multiply_by_constant())
    elif answer == 3:
        pretty_print_result(multiplay_matrices())
    elif answer == 4:
        pretty_print_result(transpose())
    elif answer == 5:
        determinant()
    elif answer == 6:
        inverse()

    answer = menu()
