## **[1. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)**

```python
a = int(input())
b = int(input())
print (a**2 + b**2)
```

## **[2. Strings and Lists](http://rosalind.info/problems/ini3/)**

```python
s = str(input())
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print (s[a:b+1] + ' ' + s[c:d+1])
```

## **[3. Conditions and Loops](http://rosalind.info/problems/ini4/)**

```python
a = int(input())
b = int(input())
l = []
while a <= b:
    if a % 2 != 0:
        l.append(a)
    a = a + 1
print (sum(l))
```

## **[4. Working with Files](http://rosalind.info/problems/ini5/)**

```python
f = open('input.txt', 'r')
lines = f.readlines()
e = []
for i in range (0, len(lines)):
    if i % 2 != 0:
        e.append(i)
even_lines = []
for i in e:
    even_lines.append(lines[i])
f.close()
f2 = open('output.txt', 'w')
for i in even_lines:
    f2.write(str(i) + '\n')
f2.close()
```

## **[5. Dictionaries](http://rosalind.info/problems/ini6/)**

```python
string = open('string.txt', 'r')
s = str(string.readline())
d = {}
for word in s.split(): 
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for key, value in d.items():
    print (key, value)
string.close()
```



