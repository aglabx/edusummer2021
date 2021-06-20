# 2. Variables and Some Arithmetic. [Link](http://rosalind.info/problems/ini2/)

```python
with open("rosalind_ini2.txt") as fh:
    a, b = map(int, fh.readline().split())
    print(a**2 + b**2)
```

# 3. Strings and Lists. [Link](http://rosalind.info/problems/ini3/)

```python
with open("rosalind_ini3.txt") as fh:
    lines = fh.readlines()
    str = lines[0]
    s1, e1, s2, e2 = map(int, lines[1].split())
print(f"{str[s1:e1+1]} {str[s2:e2+1]}")
```

# 4. Conditions and Loops. [Link](http://rosalind.info/problems/ini4/)

```python
with open("rosalind_ini4.txt") as fh:
    a, b = map(int, fh.readline().split())
summa = 0
for i in range(a, b+1):
    if i % 2:
        summa += i
print(summa)
```

# 5. Working with Files. [Link](http://rosalind.info/problems/ini5/)

```python
with open('rosalind_ini5.txt')as fh:
    for i, line in enumerate(fh):
        if i % 2:
            print(line)
```

# 6. Dictionaries. [Link](http://rosalind.info/problems/ini6/)

```python
from collections import Counter

dict_of_word = Counter()
with open('rosalind_ini6.txt')as fh:
    list_of_words = fh.readline().split()
for element in list_of_words:
    dict_of_word[element] += 1
for key, value in dict_of_word.items():
        print(f"{key} {value}")
```
