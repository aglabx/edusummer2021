## [1. Opposite number](https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python)
```python
def opposite(number):
  # your solution here
    return number* -1

```
## [2. Even or Odd]( https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python)

```python
def even_or_odd(number):
    if number%2 == 0:
        return "Even" 
    if number%2 != 0:
        return "Odd"   
```

## [3 Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python)

```python
def get_count(input_str):
    num_vowels = 0
    start = -1
    count = 0
    while True:
        start = input_str.find("a", start+1)
        if start == -1:
            break
        count += 1
    while True:
        start = input_str.find("e", start+1)
        if start == -1:
            break
        count += 1
    while True:
        start = input_str.find("i", start+1)
        if start == -1:
            break
        count += 1
    while True:
        start = input_str.find("o", start+1)
        if start == -1:
            break
        count += 1
    while True:
        start = input_str.find("u", start+1)
        if start == -1:
            break
        count += 1
    return count
```
## [4 Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python)

```python
def disemvowel(string_):
    string_ = string_.replace('a','')
    string_ = string_.replace('e','')
    string_ = string_.replace('i','')
    string_ = string_.replace('o','')
    string_ = string_.replace('u','')
    string_ = string_.replace('O','')
    return string_
```

## [5  Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028/train/python)

```python
def get_middle(s):
    #your code here
    if len(s) == 2:
        a = s[:]
    elif len(s)%2 ==0:
        part = len(s)//2
        part1 = part - 1
        a = s[part1:-part1]
    else:
        part = len(s)//2 + 1
        part1 = part - 1
        a = s[part1:part]
    return a
```

## [6 All Star Code Challenge #1](https://www.codewars.com/kata/5863f97fb3a675d9a700003f/train/python)

```python
def sum_ppg(playerOne, playerTwo):
    # Your code here
    playerOne = { 'team': '76ers', 'ppg': 11.2 }
    playerTwo  = { 'team': '76ers', 'ppg': 20.2 }
    return playerOne['ppg'] + playerTwo['ppg']
```
