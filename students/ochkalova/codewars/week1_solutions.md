## [1. Opposite number]()

```python
def opposite(number):
    return -1 * number
```

## [2. Even or Odd]()

```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

## [3. Vowel Count]()

```python

```

## [4. Disemvowel Trolls]()

```python
def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for i in string_:
        if i.lower() not in vowels:
            new_string += i
    return new_string
```

## [5. Get the Middle Character]()

```python

```

## [6. All Star Code Challenge #1]()

```python


```

## [1. Who likes it?]()

```python
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        name1, name2 = names
        return f"{name1} and {name2} like this"
    elif len(names) == 3:
        name1, name2, name3 = names
        return f"{name1}, {name2} and {name3} like this"
    elif len(names) >= 4:
        name1, name2, *others = names
        return f"{name1}, {name2} and {len(others)} others like this"
```

## [2. Array.diff]()

```python
def array_diff(a, b):
    return [i for i in a if i not in b]
```

## [3. All Star Code Challenge #22]()

```python
def to_time(seconds):
    n_hours = seconds // 3600
    n_mins = (seconds % 3600) // 60
    return f'{n_hours} hour(s) and {n_mins} minute(s)'
```
