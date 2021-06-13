import sys
import numpy as np


def elimination(matrix: np.ndarray):
    if matrix[0, 0]:
        matrix[1, 1] -= matrix[0, 1] / matrix[0, 0] * matrix[1, 0]
        matrix[1, 2] -= matrix[0, 2] / matrix[0, 0] * matrix[1, 0]
        matrix[1, 0] -= matrix[0, 1] / matrix[0, 0] * matrix[1, 0]
    else:
        matrix[1, 2] -= matrix[0, 2] / matrix[0, 1] * matrix[1, 1]
        matrix[1, 1] -= matrix[0, 1] / matrix[0, 1] * matrix[1, 1]

    # ==> c = 0
    # print(matrix)
    if matrix[1, 1]:
        matrix[1, 2] /= matrix[1, 1]
        matrix[1, 0] /= matrix[1, 1]
        matrix[1, 1] /= matrix[1, 1]
    # ==> d = 0
    # print(matrix)
    matrix[0, 0] -= matrix[1, 0] * matrix[0, 1]
    matrix[0, 2] -= matrix[1, 2] * matrix[0, 1]
    matrix[0, 1] -= matrix[1, 1] * matrix[0, 1]
    # print(matrix)
    if matrix[0, 0]:
        matrix[0, 0] /= matrix[0, 0]
        matrix[0, 1] /= matrix[0, 0]
        matrix[0, 2] /= matrix[0, 0]
    else:
        matrix[0, 2] /= matrix[0, 1]
        matrix[0, 1] /= matrix[0, 1]
    # print(matrix)
    return matrix


def sle(a, b, c, d, e, f):
    A = np.array([[a, b],
                  [c, d]], dtype=float)
    Ax = np.array([[a, b, e],
                    [c, d, f]], dtype=float)

    rank_A = np.linalg.matrix_rank(A)
    rank_Ax = np.linalg.matrix_rank(Ax)

    if rank_A == rank_Ax: # Case 1, 2, 3, 4
        det = a * d - b * c
        # case 5
        if det == 0 and a == b == c == d == e == f == 0:
            return f'{5}'
        # case 2
        if rank_A == 2:
            J = (f - e / a * c) / (d - b / a * c)
            K = (e - J * b) / a
            return f"{2} {K:.5f} {J:.5f}"

        rref = elimination(Ax)
        print('----------------!!!')
        # case 1, 3, 4:
        # print(rref[0, 0:2])
        if np.all(rref[0, 0:2]):
            a = int(rref[0, 1]) if rref[0, 1].is_integer() else rref[0, 1]
            return f"{1} {(-1 * a):.5f} {rref[0, 2]:.5f}"
        else:
            return f"{(3 + bool(not rref[0, 0])):.5f} {rref[0, 2]:.5f}"

    return f'{0}'  # case 0


def sle2(a, b, c, d, e, f):
    det = a * d - b * c
    if det:
        if d:
            k = (e - b * f / d) / (a - b * c / d)
            b_ = (f - c * k) / d
        else:
            k = (f - d * e / b) / (c - d * a / b)
            b_ = (e - a * k) / b
        return f'{2} {k:.5f} {b_:.5f}'
    else:  # det = 0
        if all((a == 0, c == 0)):
            if all((b == 0, d == 0)):
                # print(all((e, f)))
                return f'{5}' if all((e == 0, f == 0)) else f'{0}'  # нулевая система не имеет ненулевых решений
        # проверка на равенство рангов обычной и аугментированной матрицы (Теорема Кронекера-Капелли)
            if e * d != f * b:  # ранги не совпадает, так как 2 и 3 столбцы линейно независимы,
                # и тогда при элиминации нижняя строка не будет нулевой - систма не имеет решений
                return f'{0}'
            else:
                return f'{4} {(e / b):.5f}' if b else f'{4} {(f / d):.5f}'
        # та же самая проверка, только для первого столбца
        if all((b == 0, d == 0)):
            if e * c != a * f:
                return f'{0}'
            else:
                return f'{3} {(e / a):.5f}' if a else f'{3} {(f / c):.5f}'
        if a != 0:
            coefficient = c / a
            # c = 0
            d -= coefficient * b
            f -= coefficient * e
            if all((c == 0, d == 0, f == 0)):
                return f"{1} {-a / b:.5f} {e / b:.5f}"
        else:
            coefficient = a / c
            # a = 0
            b -= coefficient * d
            e -= coefficient * f
            if all((a == 0, b == 0, e == 0)):
                return f"{1} {-c / d:.5f} {f / d:.5f}"

        return f'{0}'


a, b, c, d, e, f = map(float, sys.stdin.read().strip().split('\n'))
print(sle2(a, b, c, d, e, f))
if __name__ == '__main__':
    import random

    # while True:
    #     a, b, c, d, e, f = (random.randint(0, 10) for _ in range(6))
    #     print(f"""Testing
    #     a = {a}
    #     b = {b}
    #     c = {c}
    #     d = {d}
    #     e = {e}
    #     f = {f}""")
    #     x = sle2(a, b, c, d, e, f)
    #     y = sle(a, b, c, d, e, f)
    #     if x != y:
    #         print(f'INCORRECT: False {x} vs. True {y}')
    #         break
    #     else:
    #         print(f'DONE!!!!!!!!!!!\n {x}')