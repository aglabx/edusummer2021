## [1. Opposite number](https://github.com/Nadya7n/edusummer2021/blob/main/codewars.com/kata/56dec885c54a926dcd001095)

```python
def opposite(number):
    return -1 * number
```

## [*2. Even or Odd?](https://www.codewars.com/kata/5949481f86420f59480000e7)

```python
def odd_or_even(arr):
    summa = 0
    for element in arr:
        summa += element
    if summa % 2 == 0:
        return "even"
    else:
        return "odd"
```


## [2. Even or Odd](https://www.codewars.com/kata/5949481f86420f59480000e7)

```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

## [3. Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

```python
def get_count(input_str):
    num_vowels = 0
    set_of_vowels = set('aeiou')
    for element in input_str:
        if element in set_of_vowels:
            num_vowels += 1
    return num_vowels
```

## [4. Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e)

```python
def disemvowel(string_):
    set_of_vowels = set('aeiou')
    new_string = []
    for element in string_:
        lower_element = element.lower()
        if lower_element not in set_of_vowels:
            new_string.append(element)
    new_string = ''.join(new_string)
    return new_string
```

## [5. Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028)

```python
def get_middle(s):
    length = len(s)
    average_index = length // 2
    if length % 2 == 0:
        return s[(average_index-1):(average_index+1)]
    else:
        return s[average_index]
```

## [6. All Star Code Challenge #1](https://www.codewars.com/kata/5863f97fb3a675d9a700003f/python)

```python
def sum_ppg(playerOne, playerTwo):
    sum_ppg = playerOne["ppg"] + playerTwo["ppg"]
    return  sum_ppg
```

## [1. Who likes it?](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

```python
def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
```

## [2. Array.diff](https://www.codewars.com/kata/523f5d21c841566fde000009/python)

```python
def array_diff(a, b):
    return [element for element in a if not element in b]
```

## [3. All Star Code Challenge #22](https://www.codewars.com/kata/5865cff66b5699883f0001aa)

```python
def to_time(seconds):
    hours = seconds // 60 // 60
    minutes = seconds // 60 % 60
    return f"{hours} hour(s) and {minutes} minute(s)"
```
