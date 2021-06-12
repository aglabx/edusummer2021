import sys
import math as m


def emergency(curr_apartment, num__of_floors, prev_apartment, prev_entrance, prev_floor):
    apartments_per_floor = m.ceil(prev_apartment / (num__of_floors * (prev_entrance - 1) + prev_floor))
    min_apart_num_on_prev_floor = ((prev_entrance - 1) * num__of_floors + prev_floor - 1) * apartments_per_floor + 1
    max_apart_num_on_prev_floor = ((prev_entrance - 1) * num__of_floors + prev_floor) * apartments_per_floor
    if not (min_apart_num_on_prev_floor <= prev_apartment <= max_apart_num_on_prev_floor):
        return -1, -1


def apps_per_floor(m, k, p, n):
    min_bound = k // (m * (p - 1) + n)
    max_bound = (k - 1) // (m * (p - 1) + n - 1)
    possible_qs = []
    for q in range(min_bound, max_bound + 1):
        if q != 0 and (m * (p - 1) + n - 1) * q + (k - 1) % q == k - 1:
            possible_qs.append(q)

    return possible_qs


def emergency2(k1, m, k2, p2, n2):
    if not (0 <= n2 <= m):
        return -1, -1

    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            return 1, 1
        else:
            possible_apf = range(k2, k1 + 1)
    else:
        possible_apf = apps_per_floor(m, k2, p2, n2)

    result = [-1, -1]
    for apf in possible_apf:
        # floor_index = m * (p - 1) + n = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        floor_index = ((k1 - 1 - (k1 - 1) % apf) // apf) + 1
        searching_floor = floor_index % m
        searching_entrance = (floor_index - searching_floor) // m + 1

        if searching_floor == 0:
            searching_floor = m
            searching_entrance -= 1
        if result == [-1, -1]:
            result = [searching_entrance, searching_floor]
        else:
            if searching_floor != result[1]:
                result[1] = 0
            if searching_entrance != result[0]:
                result[0] = 0

    return result


k1, m, k2, p2, n2 = map(int, sys.stdin.readline().strip().split())
print(*emergency2(k1, m, k2, p2, n2))
