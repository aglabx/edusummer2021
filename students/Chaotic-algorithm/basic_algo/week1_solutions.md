# 0. ФИО.

```python
name = str(input())
print(name)
```

# A. Кондиционер.

```python
troom,tcond = [int(x) for x in input().split()]
mode = str(input())

if -50 <= troom <= 50 and -50 <= tcond<=50:
    if mode == 'freeze' and troom <= tcond:
        print(troom)
    elif mode == 'freeze' and troom > tcond:
        print(tcond)
    elif mode == 'heat' and troom < tcond:
        print(tcond)
    elif mode == 'heat' and troom >= tcond:
        print(troom)
    elif mode == 'auto':
        print(tcond)
    elif mode == 'fan':
        print(troom)
```

# B. Треугольник.

```c++
#include <iostream>
#include <string>

int main()
{
  int a, b, c;
  std::cin >> a >> b >> c;
  if (a + b > c && a + c > b && c + b >a) {
    std::cout << "YES";
    }
  else {
    std::cout << "NO";
    }
  return 0;
}
```

# C. Телефонные номера.

```python
n = 11
phones = ''

for i in range(4):
    string = input()
    string = string.replace('+7', '8')
    new_string = ''.join(i for i in string if i.isalnum())
    if len(new_string) == 7:
        new_string = '8495' + new_string
    phones += new_string
phone_list = [phones[i:i+n] for i in range(0, len(phones), n)]
if phone_list[0] == phone_list[1]:
    print("YES")
else:
    print("NO")
if phone_list[0] == phone_list[2]:
    print("YES")
else:
    print("NO")
if phone_list[0] == phone_list[3]:
    print("YES")
else:
    print("NO")
```

# D. Уравнение с корнем.

```python
a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print('NO SOLUTION')
elif a == 0 and b == c**2:
    print('MANY SOLUTIONS')
elif a == 0 and b != c**2:
    print('NO SOLUTION')
elif ((c**2)-b) % a != 0:
    print('NO SOLUTION')
else:
    x = int((c**2 - b) / a)
    print(x)
```

# F. Расстановка ноутбуков.

```python
#F
a = int(input())
b = int(input())
c = int(input())
d = int(input())
l1=[]
l2=[]

if a > c:
    l1.append(a)
else:
    l1.append(c)
l2.append(b+d)
S1_param = [l1[0], b + d]
if a > d:
    l1.append(a)
else:
    l1.append(d)
l2.append(b + c)
S2_param = [l1[1], b + c]
if b > c:
    l1.append(b)
else:
    l1.append(c)
l2.append(a + d)
S3_param = [l1[2], a + d]
if b > d:
    l1.append(b)
else:
    l1.append(d)
l2.append(a + c)
S4_param = [l1[3], a + c]
S_params = []
S=[]
S_params.extend((S1_param, S2_param, S3_param, S4_param))
for i in range(len(l1)):
    S.append(l1[i] * l2[i])
S_dict={}
for i, j in zip(S_params, S):
    S_dict[j] = i
print(S_dict[min(S_dict.keys())][0], S_dict[min(S_dict.keys())][1])
```

# I. Узник замка ИФ.

```python
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A <= E and B <= D or A <= D and B <= E:
    print("YES")
elif C <= E and B <= D or C <= D and B <= E:
    print("YES")
elif A <= E and C <= D or A <= D and C <= D:
    print("YES")
else:
    print("NO")
```

# J. Система линейных уравнений - 2

```python
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

#прописываем флаги для некоторых состояний
noExist1 = False
noExist2 = False
isPlain1 = False
isPlain2 = False
isVertical1 = False
isVertical2 = False
isHorizontal1 = False
isHorizontal2 = False
if (a == 0 and b == 0 and e != 0):
    noExist1 = True
if (c == 0 and d == 0 and f != 0):
    noExist2 = True
if (a == 0 and b == 0 and e == 0):
    isPlain1 = True
if (c == 0 and d == 0 and f == 0):   
    isPlain2 = True
if (a != 0 and b == 0):
    isVertical1 = True
if (c != 0 and d == 0):
    isVertical2 = True
if (a == 0 and b != 0):
    isHorizontal1 = True
if (c == 0 and d != 0):
    isHorizontal2 = True

if isPlain1 and isPlain2:
    print(5)
elif noExist1 or noExist2:
    print(0)
elif isVertical1 and isVertical2 and a * f != c * e:
    print(0)
elif isHorizontal1 and isHorizontal2 and b * f != d * e:
    print(0)
elif a * d == b * c and a * f != c * e:
    print(0)

elif a * f == c * e and a * d == b * c:
    if b == 0 and d == 0:
        if a == 0:
            if e == 0:
                print(3, f / c)
        elif a != 0 and c != 0:
            print(3, e / a)
        elif c == 0:
            if f == 0:
                print(3, e / a)
    elif a == 0 and c == 0:
        if d != 0:
            print(4, f / d)
        elif b != 0:
            print(4, e / b)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    det = a * d - b * c
    detx = e * d - b * f
    dety = a * f - e * c
    x = detx / det
    y = dety / det
    print(2, x, y)
```
