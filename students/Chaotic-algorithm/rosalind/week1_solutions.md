# 1. Installing Python. http://rosalind.info/problems/ini1/
```python
import this
```

# 2. Variables and Some Arithmetic. http://rosalind.info/problems/ini2/
```python
def length(a,b):
    return a**2 + b**2
```

# 3. Strings and Lists. http://rosalind.info/problems/ini3/

```python
with open('/home/unity/Downloads/rosalind_ini3.txt') as file:
    str1 = file.readline()
    str2 = file.readline().split(' ')
    a = int(str2[0])
    b = int(str2[1]) + 1
    c = int(str2[2])
    d = int(str2[3]) + 1
    print(str1[a:b], str1[c:d])
```

# 4. Conditions and Loops. http://rosalind.info/problems/ini4/

```python
with open('/home/unity/Downloads/rosalind_ini4.txt') as file:
    str1 = file.readline().split(' ')
    a=[]
    for i in range(int(str1[0]), int(str1[1])+1):
        if i % 2 == 1:
            a.append(i)
print(sum(a))
```

# 5. Working with Files. http://rosalind.info/problems/ini5/

```python
with open('/home/unity/Downloads/rosalind_ini5.txt') as file:
    file_w=open('/home/unity/Downloads/answer_ini5.txt', 'w')
    for i, j in enumerate(file):
        if i % 2:
            file_w.write(j)
    file_w.close()
```
        
# 6. Dictionaries. http://rosalind.info/problems/ini6/

```python
file = open('/home/unity/Downloads/rosalind_ini4.txt')
counts={}
word_list=file.read().split()
for word in word_list:
    counts[word]=word_list.count(word)
for k, v in counts.items():
    print(k, v)
```
