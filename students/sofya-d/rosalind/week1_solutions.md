# 1. Installing Python.

```python
"The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"
```

# 2. Variables and Some Arithmetic.

```python
a = int(input())
b = int(input())
square_c = a ** 2 + b ** 2
print(square_c)
```

# 3. Strings and Lists.

```python
s = raw_input()
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())
asb = s[a:(b + 1)]
csd = s[c:(d + 1)]
ans = f"{asb} {csd}"
print(ans)
```

# 4. Conditions and Loops.

```python
a = int(raw_input())
b = int(raw_input())
sum = 0
for num in range(a, b + 1):
    if num % 2 == 1:
        sum += num
print(sum)
```

# 5. Working with Files.

```python
with open('rosalind_ini.txt', 'r') as input_file, open('answer.txt', 'w') as output_file:
    count = -1
    for line in input_file:
        count += 1
        if count % 2 == 1:
            output_file.write(line)
```

# 6. Dictionaries.

```python
data = input().split()
from collections import Counter
data = dict(Counter(data))
for key in data:
    print(key, data[key])
```
