## [1. Installing Python]
```python
import this
```

## [2. Variables and Some Arithmetic]
```python
def length(a,b):
    return a**2 + b**2
```

## [3. Strings and Lists]

```python
file = open('/home/unity/Downloads/rosalind_ini3.txt')
str1 = file.readline()
str2 = file.readline().split(' ')
print(str1[int(str2[0]):int(str2[1])+1], str1[int(str2[2]):int(str2[3])+1])
```

## [4. Conditions and Loops]

```python
file = open('/home/unity/Downloads/rosalind_ini4.txt')
str1 = file.readline().split(' ')
a=[]
for i in range(int(str1[0]),int(str1[1])+1):
    if i%2==1:
        a.append(i)
print(sum(a))
```

## [5. Working with Files]

```python
file_r = open('/home/unity/Downloads/rosalind_ini5.txt','r')
file_w=open('/home/unity/Downloads/answer_ini5.txt','w')
for i, j in enumerate(file_r):
    if i%2:
        file_w.write(j)
```
        
## [6. Dictionaries]

```python
file = open('/home/unity/Downloads/rosalind_ini4.txt')
counts={}
word_list=file.read().split()
for word in word_list:
    counts[word]=word_list.count(word)
for k, v in counts.items():
    print(k, v)
```
