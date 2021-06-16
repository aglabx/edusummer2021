## [1. Installing Python](http://rosalind.info/problems/ini1/)

```python
import this
```

## [2. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)

```python
a,b = map(int,input().split())
c = a**2 + b**2
print(c)

```

## [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
text = input()
a, b, c, d = map(int,input().split())
text_zero = ' '
text1 = text[a:b+1] + text_zero + text[c:d+1]
print(text1)

```

## [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
a, b = map(int, input().split())
c = 0
if a%2 == 0:
    a += 1

    for i in range (a, b+1, 2):
        c  += i
print(c)

```

## [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
f = open('./rosalind_ini666.txt',  'r')
for line in lines[1::2]:
    print(line)
f.close()
```
