def add():
    a_n, a_m = map(int, input("Enter size of first matrix: > ").split())
    A = list()
    print("Enter matrix:")
    for i in range(a_n):
        A.append(list(map(float, input("> ").split())))

    b_n, b_m = map(int, input("Enter size of second matrix: > ").split())
    B = list()
    print("Enter matrix:")
    for i in range(b_n):
        B.append(list(map(float, input("> ").split())))

    if a_n != b_n or a_m != b_m :
        return -1

    return [[A[i][j] + B[i][j] for j in range(a_m)] for i in range(a_n)]

def multiply_by_constant():
    a_n, a_m = map(int, input("Enter size of matrix: > ").split())
    A = list()
    print("Enter matrix:")
    for i in range(a_n):
        A.append(list(map(float, input("> ").split())))

    c = float(input("Enter constant: > "))

    return [[c * A[i][j] for j in range(a_m)] for i in range(a_n)]


def multiplay_matrices():
    a_n, a_m = map(int, input("Enter size of first matrix: > ").split())
    A = list()
    print("Enter matrix:")
    for i in range(a_n):
        A.append(list(map(float, input("> ").split())))

    b_n, b_m = map(int, input("Enter size of second matrix: > ").split())
    B = list()
    print("Enter matrix:")
    for i in range(b_n):
        B.append(list(map(float, input("> ").split())))

    if a_m != b_n :
        return -1

    return [[sum([a*b for a, b in zip(A_row, B_col)]) for B_col in zip(*B)] for A_row in A]


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices\n0. Exit")
    return int(input("Your choice: > "))

answer = menu()

while answer != 0:
    if answer == 1:
        result = add()
    elif answer == 2:
        result = multiply_by_constant()
    else:
        result = multiplay_matrices()
    if result != -1:
        print("The result is:")
        print(*[' '.join(map(str, result[i])) for i in range(len(result))], sep = '\n')
        print()
    else:
        print("The operation cannot be performed.")
        print()
    answer = menu()

