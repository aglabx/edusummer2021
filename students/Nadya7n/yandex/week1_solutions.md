## [1. Кондиционер](https://contest.yandex.ru/contest/27393/problems/A/)

```python
temparature = input()
mode = input(str())
current_temparature = int(temparature.split(" ")[0])
expected_temparature = int(temparature.split(" ")[-1])

if mode == "heat":
    if current_temparature > expected_temparature:
        output = current_temparature
    else:
        output = expected_temparature
elif mode == "freeze":
    if current_temparature < expected_temparature:
        output = current_temparature
    else:
        output = expected_temparature
elif mode == "auto":
    output = expected_temparature
else:
    output = current_temparature

print(output)
```

## [2. Треугольник](https://contest.yandex.ru/contest/27393/problems/B/)

```python
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else: 
    print("NO")
```

## [3. Телефонные номера](https://contest.yandex.ru/contest/27393/problems/C/)

```python
import re
number_needed = re.sub("[-()+]", "", input())
number_1 = re.sub("[-()+]", "", input())
number_2 = re.sub("[-()+]", "", input())
number_3 = re.sub("[-()+]", "", input())

code_default = "495"

def normal_len(number):
    if len(number) == 11:
        return number[1:]
    elif len(number) == 10:
        return number
    elif len(number) == 7:
        return f"{code_default}{number}"
    else:
        return "NO"

def is_or_not(number):
    if number == normal_len(number_needed):
        return print("YES")
    else:
        return print("NO")     

list_numbers = [normal_len(number_1), normal_len(number_2), normal_len(number_3)]
for element in list_numbers:
    is_or_not(element)
```

## [4. Уравнение с корнем](https://contest.yandex.ru/contest/27393/problems/D/)

```python
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
x = 0

def is_int(n):
    return int(n) == float(n)

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
        if is_int(x):
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

## [7. Детали](https://contest.yandex.ru/contest/27393/problems/G/)

```python
# пока падает на 14 тесте (Time Limit)
N, K, M = map(int, input().split(" "))

pull_residue = 0
number_details = 0

def process(N,K,M):  
    n_template = N // K
    global pull_residue
    pull_residue += N - n_template * K
    for element in range(1,n_template+1):
        global number_details
        number_details += K // M
        pull_residue += K - M * (K // M)
    
process(N,K,M)

while pull_residue >= K:
    new_N = pull_residue
    pull_residue = 0
    process(new_N, K, M)
    
print(number_details)

```
