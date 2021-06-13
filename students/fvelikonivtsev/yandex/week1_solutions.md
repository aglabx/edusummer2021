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

### Главная формула, которую я ненавижу:

**k - 1 = [m * (p - 1) + n - 1] * apf + (k - 1) mod  apf** - вычисляет номер квартиры

первое слагаемое - количество квартир в предыдущих подъездах и квартир на нижних этажах данного подъезда, второе - количество квартир на этаже

<u>k - 1</u>- номер квартиры, начинается с нуля (самая первая квартира имеет индекс 0, так единственное, как у меня получилось сосчитать)

<u>n  - 1</u>- кол-во этажей до нашего этажа

<u>apf</u> - количество квартир на этаже

<u>mod</u> - alias % 

<u>p - 1</u> - кол-во подъездов до нашего подъезда

<u>m</u> - количество этажей в доме



Максимальные и минимальные границы в функции **app_per_floor** взяты подставлением в мега-формулу двух случаев - когда **(k - 1) mod apf = 0** - это самый минимальн возможный индекс квартиры на этаже, и когда **(k - 1) mod  apf = apf - 1**  - это когда наша квартира на этаже последняя по счёту (следующая уже на следующем этаже)

```python
import sys

def apps_per_floor(m, k, p, n):
    # Рассчитываем максимальное и минимальное количество квартир на этаже
    minimum_apf = k // (m * (p - 1) + n)
    maximum_apf = (k - 1) // (m * (p - 1) + n - 1)
    apfs = []
    # ведётся подсчёт на совпадение, пока без проверок на достоверность данных
    for apf in range(minimum_apf, maximum_apf + 1):
        if apf and (m * (p - 1) + n - 1) * apf + (k - 1) % apf == k - 1:
            apfs.append(apf)
    return apfs


def emergency2(k1, m, k2, p2, n2):
    if not (0 <= n2 <= m):
        return -1, -1

    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            return 1, 1  # без этого теста не проходило, тут всё логично по условию
        else:
            possible_apf = range(k2, k1 + 1)  # в данном случае квартир может быть не меньше,
                                                # чем номер К2 и не больше, чем номер К1, так как они обе на 1 этаже 1 подъёзда
    else:
        possible_apf = apps_per_floor(m, k2, p2, n2)

    entrance, floor = -1, -1  # Если вариантов по количеству квартир на этаже нет - то цикла не будет,
    # единственный вариант, когда данные неправильные
    
    # Цикл для просчёта возможных комбинаций при разных показателях количества квартир на этаже - нужно для роверки достоверности информации (здесь идёт неявная проверка)
    for apf in possible_apf:
        # floor_index = m * (p - 1) + n = ((k1 - 1 - (k1 - 1) % q) / q) + 1 = это вывели из главной формулы
        # это индекс этажа, на котором находится квартира
        floor_index = ((k1 - 1 - (k1 - 1) % apf) // apf) + 1
        searching_floor = floor_index % m
        searching_entrance = (floor_index - searching_floor) // m + 1

        # так как этаж - это остаток от деления, то он можеть быть и нулевым, это значит, это последний этаж предыдущего подъезда
        if searching_floor == 0:
            searching_floor = m
            searching_entrance -= 1
        # обновляем данные по мере необходимости
        if all((floor == -1, entrance == -1)):
            entrance = searching_entrance
            floor = searching_floor
        else:
            # здесь идёт явная проверка на двойственность информации, можно ли правильно оценить подъезд и этаж
            if searching_floor != floor:
                floor = 0
                # break - с ним не работает
            if searching_entrance != entrance:
                entrance = 0
                # break - с ним не работает
    return entrance, floor


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

Скорость алгоритма O(1), зато моя скорость O(2 часа) из-за неправильного подсчёта максимума в начале



когда ищем максимум, надо считать минимум, потому что иначе Таня может заметить доп. поезд, и параметры будут неверными



Критерий того, что Таня запуталась - максимум меньше минимума (нет такого временного промежутка, когда она бы насчитала столько составов на 1  второй линии)

```python
import sys


def trains2(a, b, n, m):
    minimum = max(n + a * (n - 1), m + b * (m - 1))
    maximum = min(n + a * (n + 1), m + b * (m + 1))
    return f"{minimum} {maximum}" if minimum <= maximum else f'{-1}'


a, b, n, m = map(int, sys.stdin.read().strip().split('\n'))
sys.stdout.write(trains2(a, b, n, m))
```

# [I. Узник замка Иф](https://contest.yandex.ru/contest/27393/problems/I/)

```python
import sys

def escape2(a, b, c, d, e):
    sizes = sorted((a, b, c))
    size1, size2 = sizes[0], sizes[1]
    return "YES" if any((size1 <= d and size2 <= e, size1 <= e and size2 <= d)) else "NO"


A, B, C, D, E = map(int, sys.stdin.read().strip().split('\n'))
print(escape2(A, B, C, D, E))
```



# [J. СЛУ](https://contest.yandex.ru/contest/27393/problems/J/)

```python
def sle2(a, b, c, d, e, f):
    det = a * d - b * c
    
    if det:
        # самый простой случай - когда определитель ненулевой, то есть, матрица невырожденна ==> СЛУ имеет только одно единственное решение
        if d: # если d положителен, то на него можно делить и использовать - ниже приведены шаги элиминации Гаусса, которые я проверял пошагово дабы вывести явную формулу
            k = (e - b * f / d) / (a - b * c / d)
            b_ = (f - c * k) / d
        else: 
            k = (f - d * e / b) / (c - d * a / b)
            b_ = (e - a * k) / b
        return f'{2} {k:.5f} {b_:.5f}'
    else:  # det = 0
        if all((a == 0, c == 0)):
            if all((b == 0, d == 0)): # нулевая система не имеет ненулевых решений
            # проверка на равенство рангов обычной и аугментированной матрицы (Теорема Кронекера-Капелли)
                return f'{5}' if all((e == 0, f == 0)) else f'{0}'  
            if b * f != e * d:  
                return f'{0}'
            # ранги не совпадает, так как 2 и 3 столбцы линейно независимы,
            # и тогда при элиминации нижняя строка не будет нулевой - систма не имеет решений
            else:
                return f'{4} {(e / b):.5f}' if b else f'{4} {(f / d):.5f}'
     
        # та же самая проверка, только для первого столбца
        if all((b == 0, d == 0)):
            if e * c != a * f:
                return f'{0}'
            else:
                return f'{3} {(e / a):.5f}' if a else f'{3} {(f / c):.5f}'
            
       	# Случай, когда одна переменная свободная, а другая найдена - тоже элиминация Гаусса и тоже формула, показывающая все действия
        if a:
            # a != 0, считаем по первой строке, а втроую элиминируем (она должна быть нулевая, так как определитель = 0, строки.столбцы матрицы зависимы)
            d -= b * c / a
            f -= e * c / a # ==>  c = 0
            if all((c == 0, d == 0, f == 0)):
                return f"{1} {-a / b:.5f} {e / b:.5f}"
        else:
            b -= d * a / c
            e -= f * a / c # ==> a = 0
            if all((a == 0, b == 0, e == 0)):
                return f"{1} {-c / d:.5f} {f / d:.5f}"
		# если после элиминации остались ненулевые элементы в нижней строке, когда оставляем верхнюю, или в верхней строке, когда оставляем нижнюю, то у СЛУ нет решений
        return f'{0}'
```

