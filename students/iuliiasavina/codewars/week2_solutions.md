# 1. Human Readable Time. https://www.codewars.com/kata/52685f7382004e774f0001f7

```python
def make_readable(seconds):
    HH = seconds // 3600
    if HH < 10:
        HH = f"0{HH}"
    MM = (seconds % 3600) // 60
    if MM < 10:
        MM = f"0{MM}"
    SS = (seconds % 3600) % 60
    if SS < 10:
        SS = f"0{SS}"
    return f"{HH}:{MM}:{SS}"
```

# 2. Isograms. https://www.codewars.com/kata/54ba84be607a92aa900000f1

```python
def is_isogram(string): 
    s = string.lower()
    s2 = set(s)
    if len(s) == len(s2):
        return True
    return False
```

# 3. Categorize New Member. https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

```python
def open_or_senior(data):
    r = list()
    for l in data:
        if l[0] >= 55 and l[1] > 7:
            r.append("Senior")
        else: 
            r.append("Open")
    return r
```

# 4. Vasya - Clerk. 

```python
def tickets(people):
    print(f'people = {people}')
    change25 = 0
    change50 = 0
    for i in range(len(people)):
        if people[i] == 25:
            change25 += 1
        elif people[i] == 50:
            if change25 == 0:
                return "NO"
            elif change25 > 0:
                change25 -= 1
                change50 += 1
        elif people[i] == 100:
            if change25 >= 3 and change50 == 0:
                change25 -= 3
            elif change25 >= 1 and change50 >= 1:
                change25 -= 1
                change50 -= 1
            else:
                return "NO"
    if change25 >= 0 and change50 >= 0 :
        return "YES"
    return "NO"
```

# 5. The Supermarket Queue. 

```python

```

# 6. Sum of a sequence. https://www.codewars.com/kata/586f6741c66d18c22800010a

```python
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))
```

# 7. Sum of a Beach. https://www.codewars.com/kata/5b37a50642b27ebf2e000010

```python
def sum_of_a_beach(beach):
    return sum(map(beach.lower().count, ("sand", "water", "fish", "sun"))) 
```

# 8. Alphabet war. https://www.codewars.com/kata/59377c53e66267c8f6000027

```python
def alphabet_war(fight):
    left = 0
    right = 0
    for i in fight:
        if i == "w":
            left += 4
        elif i == "p":
            left += 3
        elif i == "b":
            left += 2
        elif i == "s":
            left += 1
        elif i == "m":
            right += 4
        elif i == "q":
            right += 3
        elif i == "d":
            right += 2
        elif i == "z":
            right += 1
    if right > left:
        return "Right side wins!"
    elif right < left:
        return "Left side wins!"
    return "Let's fight again!"
```

# 9. Create Phone Number. https://www.codewars.com/kata/525f50e3b73515a6db000b83

```python
def create_phone_number(n):
    n = ([str(x) for x in n])
    return f"({''.join(n[0:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"
```
