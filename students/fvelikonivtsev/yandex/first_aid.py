import sys
import math as m


def get_entrance_floor(curr_flat, num_floors, prev_flat, prev_entrance, prev_floor):
    flats_per_floor = m.ceil(prev_flat / (num_floors * (prev_entrance - 1) + prev_floor))
    min_flat_on_prev_floor = ((prev_entrance - 1) * num_floors + prev_floor - 1) * flats_per_floor + 1
    max_flat_on_prev_flor = ((prev_entrance - 1) * num_floors + prev_floor) * flats_per_floor
    if not (min_flat_on_prev_floor <= prev_flat <= max_flat_on_prev_flor):
        return -1, -1



k1, m, k2, p2, n2 = map(int, sys.stdin.read().strip().split())
print(get_entrance_floor(k1, m, k2, p2, n2))
