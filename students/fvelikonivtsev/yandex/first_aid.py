import sys
import math as m


def emergency(curr_apartment, num__of_floors, prev_apartment, prev_entrance, prev_floor):
    apartments_per_floor = m.ceil(prev_apartment / (num__of_floors * (prev_entrance - 1) + prev_floor))
    min_apart_num_on_prev_floor = ((prev_entrance - 1) * num__of_floors + prev_floor - 1) * apartments_per_floor + 1
    max_apart_num_on_prev_floor = ((prev_entrance - 1) * num__of_floors + prev_floor) * apartments_per_floor
    if not (min_apart_num_on_prev_floor <= prev_apartment <= max_apart_num_on_prev_floor):
        return -1, -1


def apps_per_floor(m, k, p, n):
    # Рассчитываем максимальное и минимальное количество квартир на этаже
    minimum_apf = k // (m * (p - 1) + n)
    maximum_apf = (k - 1) // (m * (p - 1) + n - 1)
    apfs = []
    for apf in range(minimum_apf, maximum_apf + 1):
        if apf and (m * (p - 1) + n - 1) * apf + (k - 1) % apf == k - 1:
            apfs.append(apf)
    return apfs


def emergency2(k1, m, k2, p2, n2):
    if not (0 <= n2 <= m):
        return -1, -1

    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            return 1, 1
        else:
            possible_apf = range(k2, k1 + 1)  # в данном случае квартир может быть не меньше,
                                                # чем номер К" и не больше, чем номер К1
    else:
        possible_apf = apps_per_floor(m, k2, p2, n2)

    entrance, floor = -1, -1  # Если вариантов по количеству квартир на этаже нет - то цикла не будет,
                                # единственный вариант, когда данные неправильные
    for apf in possible_apf:
        # floor_index = m * (p - 1) + n = ((k1 - 1 - (k1 - 1) % q) / q) + 1 = это вывели из главной формулы
        floor_index = ((k1 - 1 - (k1 - 1) % apf) // apf) + 1
        searching_floor = floor_index % m
        searching_entrance = (floor_index - searching_floor) // m + 1

        # так как этаж - это остаток от деления, то он можеть быть и нулевым, это значит
        if searching_floor == 0:
            searching_floor = m
            searching_entrance -= 1
        if all((floor == -1, entrance == -1)):
            entrance = searching_entrance
            floor = searching_floor
        else:
            if searching_floor != floor:
                floor = 0
            if searching_entrance != entrance:
                entrance = 0
    return entrance, floor


k1, m, k2, p2, n2 = map(int, sys.stdin.readline().strip().split())
print(*emergency2(k1, m, k2, p2, n2))
