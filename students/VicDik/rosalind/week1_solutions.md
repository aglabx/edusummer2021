# 1. Installing Python. http://rosalind.info/problems/ini1/

```python
>>> import this
The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!
>>>
```

# 2. Variables and Some Arithmetic. http://rosalind.info/problems/ini2/

```python
def hypotenuse(a, b):
    c = int(( a ** 2 + b ** 2))
    return c
```

# 3. Strings and Lists. http://rosalind.info/problems/ini3/

```python
def file_slice(file):
    with open(file, 'r') as fr:
        data = fr.readlines()
        indexes = list(map(lambda x: int(x), data[1].split()))
    with open(file.replace('.txt', '_test.txt'), 'w') as fw:
        fw.write(' '.join([data[0][indexes[i]:indexes[i + 1] + 1] for i in range(0, len(indexes), 2)]))
```

# 4. Conditions and Loops. http://rosalind.info/problems/ini4/

```python
def sum_odd(file):
    with open(file, 'r') as fr:
        a, b = [int(i) for i in fr.readlines()[0].split()]
    with open(file.replace('.txt', '_sum.txt'), 'w') as fw:
        fw.write(str(sum((i for i in range(a, b + 1) if i % 2 != 0))))
```

# 5. Working files. http://rosalind.info/problems/ini5/

```python
#решение без enumerate, читаемое

def even_lines(file):
# избавляемся от множестевенной вложенности, потому что это тоже не очень
    with open(file) as fr, open(file.replace('.txt', '_even.txt'), 'w') as fw:
        i = 0
        for lines in fr:
            i += 1
            if i % 2 == 0:                                                        
                fw.write(lines)
                
#тоже самое, но с enumerate :) 

def even_lines2(file):
    with open(file) as fr, open(file.replace('.txt', '_even2.txt'), 'w') as fw:
        data = fr.readlines()
        for i in enumerate(data):
            if (i[0] + 1) % 2 == 0:
                fw.write(i[1])
```

# 6. Dictionaries. http://rosalind.info/problems/ini6/

```python
def count_words(file):
    with open(file) as fr:
        words_list = fr.read().strip().split()
        words_set = set(words_list)
        words_dict = {x:words_list.count(x) for x in words_set}
        for i in words_dict:
            print(f'{i} {words_dict[i]}')
```
