# 1. Opposite number. [My_solution](https://www.codewars.com/kata/reviews/56deebdf6a5c28baa900003b/groups/60cf56c152dec600019598fc)

```python
def opposite(number):
    return -1 * number
```

# 2*. Even or Odd?. [My_solution](https://www.codewars.com/kata/reviews/5a2c002b57de08b5a8000f47/groups/60cf58ad13cbf7000196c58e)

```python
def odd_or_even(arr):
    #take the array and return odd/even of element's sum 
    amount = 0
    for element in arr:
        amount += element
    if amount % 2:
        return "odd"
    else:
        return "even"
```

# 2. Even or Odd. [My_solution](https://www.codewars.com/kata/reviews/53da3de52a289a37bc00128a/groups/60cf598a2d6e21000126364f)

```python
def even_or_odd(number):
    #take the number and return even/odd
    return "Even" if number % 2 == 0 else "Odd"
```

# 3. Vowel Count. [Task](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

```python
def get_count(input_str):
    #take the string and count in this string the vowels
    return sum([1 for x in input_str if x in set("aeiou")])
```

# 4. Disemvowel Trolls. [Task](https://www.codewars.com/kata/52fba66badcd10859f00097e)

```python
def disemvowel(string_):
    return ''.join(element for element in string_ if element.lower() not in set('aeiou'))
```

# 5. Get the Middle Character. [Task](https://www.codewars.com/kata/56747fd5cb988479af000028)

```python
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[(middle-1):(middle+1)]
    else:
        return s[middle]
```

# 6. All Star Code Challenge #1. [My_solution](https://www.codewars.com/kata/reviews/586435fe812998c93400129b/groups/60cf648d9a9bc1000154af0d)

```python
def sum_ppg(playerOne, playerTwo):
    return playerOne["ppg"] + playerTwo["ppg"]
```

# 1. Who likes it?. [Task](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

```python
def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
```

# 2. Array.diff. [Task](https://www.codewars.com/kata/523f5d21c841566fde000009/python)

```python
def array_diff(a, b):
    return [element for element in a if not element in b]
```

# 3. All Star Code Challenge #22. [My_solution](https://www.codewars.com/kata/reviews/60742b5f9150090001adc706/groups/60cf65352d6e21000126374d)

```python
def to_time(seconds):
    hours = seconds // 60 // 60
    minutes = seconds // 60 % 60
    return f"{hours} hour(s) and {minutes} minute(s)"
```
