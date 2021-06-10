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

# [E. Скорая помощь](https://contest.yandex.ru/contest/27393/problems/E/)

```python
```

# [F. Расстановка ноутбуков](https://contest.yandex.ru/contest/27393/problems/F/)

```python
```

# [G. Детали](https://contest.yandex.ru/contest/27393/problems/G/)

```python
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

