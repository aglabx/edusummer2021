## [1. Installing Python](http://rosalind.info/problems/ini1/)

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

## [2. Variables and Some Arithmetic](http://rosalind.info/problems/ini2/)

```python
with open(r'D:\Downloads\rosalind_ini2.txt', 'r') as fr, open('hypoth_square.txt', 'w') as fw:
    for line in fr:
        print(line)
        fw.write(f'{sum(map(lambda x: int(x) ** 2, line.strip().split()))}')
```

## [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
with open(r'D:\Downloads\rosalind_ini3.txt', 'r') as fr, open('str_list.txt', 'w') as fw:
    string = fr.readline().strip()
    a, b, c, d = map(int, fr.readline().strip().split())
    fw.write(f'{string[a:b + 1]} {string[c:d + 1]}')
```

## [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
with open(r'D:\Downloads\rosalind_ini4.txt', 'r') as fr, open('cond_loops.txt', 'w') as fw:
    a, b = map(int, fr.read().strip().split())
    fw.write(f'{sum(integer for integer in range(a, b + 1) if integer % 2)}')
```

## [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
with open(r'D:\Downloads\rosalind_ini5.txt', 'r') as fr, open(f'{__file__[:-3]}.txt', 'w') as fw:
    for index, string in enumerate(fr):
        if index % 2:
            fw.write(string)
```

## [6. Dictionaries](http://rosalind.info/problems/ini6/)

```python
with open(r'D:\Downloads\rosalind_ini6(1).txt', 'r') as fr, open(f'{__file__[:-3]}.txt', 'w') as fw:
    words = {}
    for line in fr:
        for word in line.strip().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    to_write = (f'{word} {words[word]}\n' for word in words)

    fw.writelines(to_write)

```

**Можно сразу записывать без буфера:**

```python
with open(r'D:\Downloads\rosalind_ini6(1).txt', 'r') as fr, open(f'{__file__[:-3]}.txt', 'w') as fw:
    words = {}
    for line in fr:
        for word in line.strip().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    for word, count in words.items():
        fw.write(f'{word} {count}\n')
```

