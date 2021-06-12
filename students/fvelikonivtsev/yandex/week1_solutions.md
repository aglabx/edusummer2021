# [A. Кондиционер](https://contest.yandex.ru/contest/27393/problems/A/?error=EDUPLICATE#30404/2021_05_13/rFKSEzJqpU)

Не переводил в int, т.к. текстовые литералы также могут сравниваться в Питоне

_(на скорость перевод в int не влияет)_

<u>Временная сложность</u> - **O(1)** (просчёт 2-х операций сравнения и вывод по хэш-значению)

<u>Пространственная сложность</u> - **O(1)**

```python
import sys

stdin = iter(sys.stdin)
current_temp, conditioner_temp = map(int, next(stdin).strip().split())
mode = next(stdin).strip()



def conditioner(temp1, temp2, mode_):
	decisions = {'auto': temp2, 
                 'fan': temp1, 
                 'heat': max(temp1, temp2), 
                 'freeze': min(temp1, temp2)}
	
	return str(decisions[mode_])

sys.stdout.write(conditioner(current_temp, conditioner_temp, mode))
```

# [B. Треугольник](https://contest.yandex.ru/contest/27393/problems/B/)

Необходимо воспользоваться неравенством треугольника

<u>Временная сложность</u> - **O(1)**

<u>Пространственная сложность</u> - **O(1)**

```python
import sys


def is_triangle(first, second, third):

    triangle_inequality = all((first < second + third,
                               second < first + third,
                               third < first + second))

    return 'YES' if triangle_inequality else 'NO'


a, b, c = map(int, sys.stdin.read().strip().split('\n'))
sys.stdout.write(is_triangle(a, b, c))
```

# [C. Телефонные номера](https://contest.yandex.ru/contest/27393/problems/C/)

##### _Work in progress_

```python
import sys


def transform(number: str):
    for sign in '+()-':
        if sign in number:
            number = number.replace(sign, '')
    if len(number) < 11:
        number = '8495' + number
    return number[1:]


def comparator(current_number, number_to_compare): # TODO
    return 'YES' if current_number == number_to_compare else 'NO'


stdin = iter(sys.stdin.read().strip().split('\n'))
initial_number = transform(next(stdin))
for number_ in stdin:
    sys.stdout.write(f'{comparator(initial_number, transform(number_))}\n')
```

# [D. Уравнение с корнем](https://contest.yandex.ru/contest/27393/problems/D/)

Валится на 8 тесте

```python
import sys


def equation(a, b, c):
    # sqrt(ax + b) = c
    if c < 0 or (a == 0 and b < 0) or (a == 0 and b != c ** 2):
        return 'NO SOLUTION'
    if a == 0 and 0 <= b == c ** 2 and c >= 0:
        return 'MANY SOLUTIONS'
    return f'{int((c ** 2 - b) / a)}'


a_, b_, c_ = map(int, sys.stdin.read().strip().split('\n'))

sys.stdout.write(equation(a_, b_, c_))


```

Теперь не валится:

```python
def equation(a, b, c):
    # sqrt(a*x + b) = c
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        return "MANY SOLUTIONS" if c ** 2 == b else "NO SOLUTION"
    x = (c ** 2 - b) / a
    return f'{int(x)}' if x.is_integer() else "NO SOLUTION" # !!!!!!!!!! check int nature


a_, b_, c_ = map(int, sys.stdin.read().strip().split('\n'))

sys.stdout.write(equation(a_, b_, c_))
```

# [E. Скорая помощь](https://contest.yandex.ru/contest/27393/problems/E/)

```python
import sys
import math as m

# здесь старался считать сразу всё, но не вышло, т.к. могут быть различные варианты
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
```

# [F. Расстановка ноутбуков](https://contest.yandex.ru/contest/27393/problems/F/)

Вариант со **словарём** занимает чуть больше памяти, нежели вариант с **кортежем** и аргументом функции **min**:

```python
def optimize(a1, b1, a2, b2):
    squares = {
        (a1 + a2) * max(b1, b2): (a1 + a2, max(b1, b2)),
        (a1 + b2) * max(b1, a2): (a1 + b2, max(b1, a2)),
        (b1 + a2) * max(a1, b2): (b1 + a2, max(a1, b2)),
        (b1 + b2) * max(a1, a2): (b1 + b2, max(a1, a2))
    }
    return squares[min(squares.keys())]


```

```python
def optimize(a1, b1, a2, b2):
    squares = (
        (a1 + a2, max(b1, b2)),
		(a1 + b2, max(b1, a2)),
		(b1 + a2, max(a1, b2)),
		(b1 + b2, max(a1, a2))
    )
    return min(squares, key=lambda x: x[0] * x[1])


a1, b1, a2, b2 = map(int, sys.stdin.read().strip().split())

print(*optimize(a1, b1, a2, b2))
```



# [G. Детали](https://contest.yandex.ru/contest/27393/problems/G/)

Нужна проверка на правильность комбинации - если ни из одного заготовка никакая деталь не получится, то возвращаем 0

```python
import sys


def details(n, k, m):
    mass = n
    parts_per_piece = k // m
    if parts_per_piece:
        while mass >= k:
            mass -= parts_per_piece * (mass // k) * m
        return (n - mass) // m
    return 0


n, k, m = map(int, sys.stdin.readline().strip().split())
print(details(n, k, m))
```

# [H. Метро](https://contest.yandex.ru/contest/27393/problems/H/)

```python

```

# [I. Узник замка Иф](https://contest.yandex.ru/contest/27393/problems/I/)

```python
```

# [J. СЛУ](https://contest.yandex.ru/contest/27393/problems/J/)

```python
```

