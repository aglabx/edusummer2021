## [1. Opposite number](https://github.com/Nadya7n/edusummer2021/blob/main/codewars.com/kata/56dec885c54a926dcd001095)

```python
def opposite(number):
    return number * -1
```

## [2. Even or Odd](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)

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

## [3. Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

```python
def get_count(input_str):
    num_vowels = 0
    list_of_vowels = ['a','e','i','o','u']
    for element in input_str:
        if element in list_of_vowels:  
            num_vowels += 1
    return num_vowels
```

## [4. Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e)

```python
def disemvowel(string_):
    list_of_vowels = ['a','e','i','o','u']
    new_string = []
    for element in string_:
        lower_element = element.lower()
        if lower_element not in list_of_vowels:
            new_string.append(element)
        else:
            continue
    new_string = "".join(new_string)
    return new_string
```

## [5. Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028)

```python
def get_middle(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2)-1:(len(s) // 2)+1]
    else:
        return s[len(s) // 2]
```

## [6. All Star Code Challenge #1](https://www.codewars.com/kata/5863f97fb3a675d9a700003f/python)

```python
def sum_ppg(playerOne, playerTwo):
    for key_1, value_1 in playerOne.items():
        if key_1 == "ppg":
            new_value_1 = value_1 
    for key_2, value_2 in playerTwo.items():
        if key_1 == "ppg":
            new_value_2 = value_2
    sum_ppg = new_value_1 + new_value_2
    return  sum_ppg
```

## [1. Who likes it?](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

```python
def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[-1]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[-1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[-1]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
```

## [2. Array.diff](https://www.codewars.com/kata/523f5d21c841566fde000009/python)

```python
def array_diff(a, b):
    new_a = []
    for element_1 in a:
        if element_1 in b:
            continue
        else:
            new_a.append(element_1)
    return new_a
```

## [3. All Star Code Challenge #22](https://www.codewars.com/kata/5865cff66b5699883f0001aa)

```python
def to_time(seconds):
    hours = int(seconds / 60 // 60)
    minutes = int(seconds / 60 % 60)
    return f"{hours} hour(s) and {minutes} minute(s)"
```
