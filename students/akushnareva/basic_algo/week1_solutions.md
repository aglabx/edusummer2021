## [0. ФИО]

```python
name=str(input())
print(name)
```

## [A. Кондиционер]

```python
troom,tcond=[int(x) for x in input().split()]
mode=str(input())
if -50<=troom<=50 and -50<=tcond<=50:
    if mode=='freeze' and troom<=tcond:
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

## [B. Треугольник]

```c++
#include <iostream>
#include <string>

int main()
{
    int a,b,c;
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

## [C. Телефонные номера]

```python
n=11
phones=''
for i in range(4):
    string=input()
    string=string.replace('+7','8')
    new_string=''.join(i for i in string if i.isalnum())
    if len(new_string)==7:
        new_string='8495'+new_string
    phones+=new_string
phone_list=[phones[i:i+n] for i in range(0, len(phones), n)]
if phone_list[0]==phone_list[1]:
    print("YES")
else:
    print("NO")
if phone_list[0]==phone_list[2]:
    print("YES")
else:
    print("NO")
if phone_list[0]==phone_list[3]:
    print("YES")
else:
    print("NO")
```

## [D. Уравнение с корнем]

```python
a=int(input())
b=int(input())
c=int(input())
if c < 0:
	print('NO SOLUTION')
elif (a == 0) and (b == c**2):
	print('MANY SOLUTIONS')
elif (a == 0) and (b != c**2):
	print('NO SOLUTION')
elif ((c**2)-b) % a != 0:
	print('NO SOLUTION')
else:
	x = int((c**2 - b) / a)
	print(x)
```
