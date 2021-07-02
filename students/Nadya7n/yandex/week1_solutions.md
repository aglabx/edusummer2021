# 1. Кондиционер. [Link](https://contest.yandex.ru/contest/27393/problems/A/)

```python
temparature = input()
mode = str(input())
current_temparature = int(temparature.split()[0])
expected_temparature = int(temparature.split()[1])

state_machine = {
    "heat": [current_temparature, expected_temparature],
    "freeze": [current_temparature, expected_temparature],
    "auto": [expected_temparature],
    "fan": [current_temparature]}

if mode == "heat" and current_temparature < expected_temparature:
    output = state_machine[mode][1]
elif mode == "freeze" and current_temparature > expected_temparature:
    output = state_machine[mode][1]
else:
    output = state_machine[mode][0]
print(output)
```

# 2. Треугольник. [Link](https://contest.yandex.ru/contest/27393/problems/B/)

```python
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else: 
    print("NO")
```

# 3. Телефонные номера. [Link](https://contest.yandex.ru/contest/27393/problems/C/)

```python
import re

def format(input):
    return re.sub("[-()+]", "", input)

def normal_len(number):
    code_default = "495"
    if len(number) == 11:
        return number[1:]
    elif len(number) == 10:
        return number
    elif len(number) == 7:
        return f"{code_default}{number}"
    else:
        None

def is_or_not(number):
    if number == normal_len(number_needed):
        return print("YES")
    else:
        return print("NO")  

number_needed = format(input())
number_1 = format(input())
number_2 = format(input())
number_3 = format(input())

is_or_not(normal_len(number_1))
is_or_not(normal_len(number_2))
is_or_not(normal_len(number_3))
```

# 4. Уравнение с корнем. [Link](https://contest.yandex.ru/contest/27393/problems/D/)

```python
from math import sqrt
a = int(input())
b = int(input())
c = int(input())

if c >= 0:
    if a == 0:
        if b >= 0:
            if sqrt(b) == c:
                print("MANY SOLUTIONS")
            else:
                print("NO SOLUTION")
        else:
            print("NO SOLUTION")
    else:
        x = (c**2 - b) / a
        if x.is_integer():
            if (x*a + b) >= 0:
                if sqrt(x*a + b) == c:
                    print(int(x))
                else: 
                    print("NO SOLUTION")
            else:
                print("NO SOLUTION")
        else:
            print("NO SOLUTION")
else:
    print("NO SOLUTION")
```
