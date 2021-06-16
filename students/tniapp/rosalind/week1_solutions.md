## [1. Installing Python](http://rosalind.info/problems/ini1/)

```python
import this
```

## [2. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)

```python
dataset = "/path/to/dataset.txt"

with open(dataset) as fh:
    for line in fh:
        a, b = map(int, line.strip().split())
        print(a**2 + b**2)
```

## [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
dataset = "/path/to/dataset.txt"

dataset_open = open(dataset_file)
line = dataset_open.readlines()
string = line[0].split()[0]
a, b, c, d = map(int, line[1].strip().split())

print(string[a: b+1], string[c: d+1])
```

## [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
dataset = "/path/to/dataset.txt"

dataset_open = open(dataset)
line = dataset_open.readline()
a, b = map(int, line.strip().split())
odd_sum = 0

for number in range(a, b+1):
    if number % 2 != 0:
        odd_sum += number
print(odd_sum)
```

## [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
dataset = "/path/to/dataset.txt"
count = 1

with open(dataset) as fh:
    for line in fh:
        line = line.strip()
        if count % 2 == 0:
            print(line)
        count += 1
```

## [6. Dictionaries](http://rosalind.info/problems/ini6/)

```python
import collections
counter = collections.Counter()

dataset = "/path/to/dataset.txt"
dataset_open = open(dataset)
line = dataset_open.readline()
word_list = line.strip().split()

for word in word_list:
    counter[word] += 1
    
for key, value in counter.items():
    print(key, value)
```
