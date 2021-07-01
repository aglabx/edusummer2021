# 1. Human Readable Time https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

```python
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    sec = seconds - hours*3600 - minutes*60
    if len(str(hours)) == 1:
        hours = '0'+ str(hours)
    
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    
    if len(str(sec)) == 1:
        sec = '0' + str(sec)
    return f'{hours}:{minutes}:{sec}'
```

# 2. Isograms https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

```python
def is_isogram(string):
    letter_set = []
    for el in string.upper():
        if el not in letter_set:
            letter_set.append(el)
        else:
            out = False
    try:
        out
    except NameError:
        out = True
    return out
```

# 3. Categorize New Member https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
```python
def openOrSenior(data):
    result=[]
    for _ in data:
        if _[0]>=55 and _[1]>7:
            result.append('Senior')
        else:
            result.append('Open')
    return result
```

# 4. Vasya https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

```python
def tickets(people):
    l=[0,0]
    for i in people:
        if i==25:
            l[0]+=1
        elif i==50:
            if l[0]==0:
                return "NO"
            else:
                l[0]-=1
                l[1]+=1
        else:
            if l[1]>=1:
                if l[0]==0:
                    return "NO"
                else:
                    l[0]-=1
                    l[1]-=1
            else:
                if l[0]<3:
                    return "NO"
                else:
                    l[0]-=3
    return "YES"
```

# 5. The Supermarket Queue https://www.codewars.com/kata/57b06f90e298a7b53d000a86
```python
def queue_time(customers, n):
    list_temp = [0]*n
    for item in customers:
        list_temp[list_temp.index(min(list_temp))] += item
    return max(list_temp)
```

# 6. Sum of a sequence https://www.codewars.com/kata/586f6741c66d18c22800010a
```python
def sequence_sum(begin_number, end_number, step):
    sum_tot = int()
    for i in range(begin_number, end_number+1, step):
        sum_tot+=i
```

# 7. Sum of a Beach https://www.codewars.com/kata/5b37a50642b27ebf2e000010
```python
def sum_of_a_beach(beach):
    name_list = ["sand", "water", "fish", "sun"]
    tot_sum = 0
    for el in name_list:
        tot_sum += beach.lower().count(el)
    return tot_sum
```


# 8. Alphabet war https://www.codewars.com/kata/59377c53e66267c8f6000027
```python
def alphabet_war(fight):
    count = 0
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for i in fight:
        if i in left:
            count += left[i]
        elif i in right:
            count -= right[i]
    if count < 0:
        return "Right side wins!"
    if count > 0:
        return "Left side wins!"
    elif count == 0:
        return "Let's fight again!"
```

# 9. Create Phone Number https://www.codewars.com/kata/525f50e3b73515a6db000b83
```python
def create_phone_number(n):
    begin = "".join([str(elem) for elem in n[0:3]])
    middle = "".join([str(elem) for elem in n[3:6]])
    end = "".join([str(elem) for elem in n[6:]])

    return f'({begin}) {middle}-{end}'
```

# 10. Rot13 https://www.codewars.com/kata/530e15517bc88ac656000716 
```python
def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)
```

# 11. Strip Comments https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

```python
def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)
```



