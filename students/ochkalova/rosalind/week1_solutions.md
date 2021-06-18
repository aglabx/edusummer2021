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
a, b = (int(i) for i in input().split())
print(a**2 + b**2)
```

## [3. Strings and Lists](http://rosalind.info/problems/ini3/)

```python
string = input()
start1, end1, start2, end2 = (int(i) for i in input().split())
print(string[start1:end1 + 1], string[start2:end2 + 1])

```

## [4. Conditions and Loops](http://rosalind.info/problems/ini4/)

```python
a, b = (int(i) for i in input().split())
sum = 0
for num in range(a, b + 1):
    if num % 2 == 1:
        sum += num
print(sum)
```

## [5. Working with Files](http://rosalind.info/problems/ini5/)

```python
with open("task.txt") as fh:
    for num, line in enumerate(fh):
        if num %2 == 0:
            print(line.strip())
```

## [6. Dictionaries](http://rosalind.info/problems/ini6/)

```python
from collections import Counter
line = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
counter = Counter()
for word in line.split():
    counter[word] += 1
for (word, freq) in counter.items():
    print(word, freq)
```
