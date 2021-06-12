# [2. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)

```python
with open("rosalind_ini2.txt") as fh:
    for line in fh:
        a = int(line.split(" ")[0])
        b = int(line.split(" ")[1])
    print(a**2 + b**2)
```

# [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
with open("rosalind_ini3.txt") as fh:
    lines = fh.readlines()
    str = lines[0]
    a,b,c,d = map(int, lines[1].split(" "))
print(f"{str[a:b+1]} {str[c:d+1]}")
```

# [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
with open("rosalind_ini4.txt") as fh:
    a,b = map(int, fh.readline().split(" "))
summa = 0
for i in range(a, b+1):
    if i % 2 != 0:
        summa += i
print(summa)
```

# [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
i = 0
with open('rosalind_ini5.txt')as fh:
    for line in fh:
        i += 1
        if i != 1:
            print(line)
            i = 0
```

# [6. Dictionaries](http://rosalind.info/problems/ini6/)

```python
dict_of_word = {}
with open('rosalind_ini6.txt')as fh:
    list_of_words = fh.readline().split(" ")
for element in list_of_words:
    if element not in dict_of_word.keys():
        dict_of_word[element] = 1
    else:
        dict_of_word[element] += 1
for key, value in dict_of_word.items():
        print(f"{key} {value}")
```
