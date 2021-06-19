# 1. Opposite number.

```python
def opposite(number):
    return -1 * number
```

# 2. Even or odd.

```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
```

# 3. Vowel count.

```python
def get_count(str):
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for letter in str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels
```

# 4. Disemvowel Trolls.

```python
def disemvowel(str):
    return "".join([x for x in str if not x in "aeiou"])
```

# 5. Get the Middle Character.

```python
def get_middle(str):
    length = len(str)
    if length % 2 == 0:
        return str[length // 2 - 1:length // 2 + 1]
    else:
        return str[length // 2]
```

# 6. All Star Code Challenge #1.

```python
def sum_ppg(playerOne, playerTwo):
    return playerOne["ppg"] + payerTwo["ppg"]
```

# 7. Who likes it?.

```python
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names)>3:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
```

# 8. Array.diff.

```python
def array_diff(a, b):
    return [num for num in a if num not in b]
```

# 9. All Star Code Challenge #22.

```python
def to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"
```
