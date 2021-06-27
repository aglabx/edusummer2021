# A. Возрастает ли список? https://contest.yandex.ru/contest/27472/problems/A/

```pyt
import sys


def ascending(lst):
	if lst:
		prev = lst[0]
		for i in range(1, len(lst)):
			if lst[i] <= prev:
				break
			prev = lst[i]
		else:
			return 'YES'
	return 'NO'


array = tuple(map(int, sys.stdin.read().strip().split()))
print(ascending(array))
```



# 	B. Определить вид последовательности. https://contest.yandex.ru/contest/27472/problems/B/

```python
import sys


def seq_type(sequence):
    if len(set(sequence)) <= 1:
        return "CONSTANT"

    ascending = True
    descending = True
    weakness = False

    previous = sequence[0]
    for i in range(1, len(sequence)):
        weakness |= sequence[i] == previous
        ascending &= sequence[i] >= previous
        descending &= sequence[i] <= previous
        previous = sequence[i]

    if ascending:
        return "WEAKLY ASCENDING" if weakness else "ASCENDING"
    if descending:
        return "WEAKLY DESCENDING" if weakness else "DESCENDING"
    return "RANDOM"


stdin = list(map(float, sys.stdin.readlines()))
print(seq_type(stdin[:-1]))
```



# C. Ближайшее число.  https://contest.yandex.ru/contest/27472/problems/C/

```python
import sys

def finder(array, x):
    print(sorted(array, key=lambda y: abs(x - y))[0])


n_ = int(sys.stdin.readline().strip())
array_ = tuple(map(int, sys.stdin.readline().split()))
x_ = int(sys.stdin.readline().strip())
finder(array_, x_)
```



# D. Больше своих соседей. https://contest.yandex.ru/contest/27472/problems/D/

```python
import sys


def greater_then_to_neares(array):
    count = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)


array_ = tuple(map(float, sys.stdin.read().strip().split()))
greater_then_to_neares(array_)
```



# E. Чемпионат по метанию коровьих лепешек. https://contest.yandex.ru/contest/27472/problems/E/

```python
import sys


def get_most_valuable_place(participants):
    places = set()
    winners = set()
    max_ = max(participants)
    possible_places = {}
    sorted_list = sorted(participants, reverse=True)
    for place, distance in enumerate(sorted_list, start=1):
        if distance % 10 == 5:
            if distance not in possible_places:
                possible_places[distance] = place

    for index, distance in enumerate(participants):
        if distance == max_:
            winners.add(index)
        if all((distance % 10 == 5, index + 1 < len(participants), any((i < index for i in winners)))):
            if participants[index + 1] < distance:
                places.add(possible_places[distance])
    return 0 if not places else min(places)


n, *particips = map(int, sys.stdin.read().strip().split())
print(get_most_valuable_place(particips))
```



# F. Симметричная последовательность. https://contest.yandex.ru/contest/27472/problems/F/

```python
import sys



def refactor_for_symmetry(length, array):
    for i in range(length):
        start = i
        j = length - 1
        while i < length and j >= 0 and array[i] == array[j]:
            i += 1
            j -= 1
        if j < i:
            additionals = [array[i] for i in range(start - 1, -1, -1)]
            yield (len(additionals), )
            yield additionals
            return
    yield (0,)


length_, *array_ = map(int, sys.stdin.read().strip().split())
for part in refactor_for_symmetry(length_, array_):
    print(*part)
```



# G. Наибольшее произведение двух чисел. https://contest.yandex.ru/contest/27472/problems/G/

```python
import sys


def max_double_product(array):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for value in array:
        if value >= max2:
            max1 = max2
            max2 = value
        elif max1 < value < max2:
            max1 = value

    for value in array:
        if value <= min2:
            min1 = min2
            min2 = value
        elif min1 > value > min2:
            min1 = value

    return (max1, max2) if max1 * max2 > min1 * min2 else (min2, min1)




arr = tuple(map(int, sys.stdin.read().strip().split()))
print(*max_double_product(arr))
```





# H. Наибольшее произведение трех чисел. https://contest.yandex.ru/contest/27472/problems/H/

```python
import sys
import itertools


def max_triple_product(array):
    max1 = 0
    max2 = 1
    max3 = 2
    min1 = 0
    min2 = 1
    min3 = 2

    for index, value in enumerate(array):
        if array[max3] <= value:
            max1 = max2
            max2 = max3
            max3 = index
        elif array[max2] <= value < array[max3]:
            max1 = max2
            max2 = index
        elif array[max1] <= value < array[max2]:
            max1 = index

    for index, value in enumerate(array):
        if array[min3] >= value:
            min1 = min2
            min2 = min3
            min3 = index
        elif array[min2] >= value > array[min3]:
            min1 = min2
            min2 = index
        elif array[min1] >= value > array[min2]:
            min1 = index

    unique_values = (array[i] for i in tuple({min1, min2, min3, max1, max2, max3}))

    combinations = itertools.combinations(unique_values, 3)

    return max(combinations, key=lambda x: x[0] * x[1] * x[2])


arr = tuple(map(int, sys.stdin.read().strip().split()))
# print(*max_double_product(arr))
print(*max_triple_product(arr))
```



# I. Сапер. https://contest.yandex.ru/contest/27472/problems/I/

```python
import sys


n, m, k = map(int, sys.stdin.readline().strip().split())  # n - rows, m - columns
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
    a[row][col] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end=' ')
        else:
            print(a[i][j], end=' ')
    print()
```



# J. Треугольник Максима. https://contest.yandex.ru/contest/27472/problems/J/

```python
import sys


def get_freq_range(initial, frequencies):
    left = 30.0
    right = 4000.0
    prev = initial
    for freq, comment in frequencies:
        expression = round((freq + prev) / 2, 6)
        if comment == "further":
            if freq > prev:
                right = min(right, expression)
            else:
                left = max(left, expression)
        else:
            if freq > prev:
                left = max(left, expression)
            else:
                right = min(right, expression)
        prev = freq

    return left, right


n = int(sys.stdin.readline().strip())
initial_ = float(sys.stdin.readline().strip())
others = ((float(i.split()[0]), i.split()[1]) for i in sys.stdin.readlines())

print(*get_freq_range(initial_, others))
```

