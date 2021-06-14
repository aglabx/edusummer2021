## [1. Installing Python](http://rosalind.info/problems/ini1/)

```python
import this
```

## [2. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)

```python
dataset = "/path/to/dataset.txt"

with open(dataset) as fh:
    for line in fh:
        a = int(line.split()[0])
        b = int(line.split()[1])
        if a > 1000 or b > 1000:
            print("Try another numbers")
        else:
            print(a**2 + b**2)
```

## [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
dataset = "/path/to/dataset.txt"

with open(dataset) as fh:
    for line in fh:
        line = line.strip().split()
        if len(line) == 1:
            string = line
        if len(line) > 1:
            print(line)
            for element in line:
                element = int(element)
                if element not in slices:
                    slices.append(element)
string = string[0]
if len(string) > 200:
    print("Something wrong in string format. Try another string with length less than 200 symbols")

print(string[slices[0]: slices[1]+1], string[slices[2]: slices[3]+1])
```

## [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
dataset = "/mnt/c/Users/pchesnokova/Desktop/dataset.txt"

with open(dataset) as fh:
    for line in fh:
        line = line.strip().split()
        a = int(line[0])
        b = int(line[1])

if a > b or a >= 10000 or b >= 10000:
    print("Please, select a < b or a, b < 10000")
else:
    if a % 2 == 0:
        a += 1

    odd_sum = 0
    for number in range(a, b, 2):
        odd_sum += number

    print(odd_sum)
```

## [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
dataset = "/mnt/c/Users/pchesnokova/Desktop/dataset.txt"
cnt = 1

with open(dataset) as fh:
    for line in fh:
        line = line.strip()
        if cnt > 1000:
            print("Too huge text")
            break
        if cnt % 2 == 0:
            print(line)
        cnt += 1
```

## [6. Dictionaries](http://rosalind.info/problems/ini6/)

```python
dataset = "/mnt/c/Users/pchesnokova/Desktop/dataset.txt"
word2count = {}

with open(dataset) as fh:
    for line in fh:
        if len(line) > 10000:
            print("Try string with length at most 10000 letters")
        line = line.strip().split()
        for word in line:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1

for word, count in word2count.items():
    print(word, count)
```
