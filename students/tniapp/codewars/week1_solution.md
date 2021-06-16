[1. Opposite number](https://codewars.com/kata/56dec885c54a926dcd001095)
```python
def opposite(number):
    return -number
```
[2. Even or Odd](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)
```python
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
```
[3. Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3)
```python
def get_count(input_str):
    num_vowels = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for letter in input_str:
        if letter in vowel_list:
            num_vowels += 1
    return num_vowels
```
[4. Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e)
```python
def disemvowel(string_):
    return ''.join([i for i in string_ if i not in 'aeiouAEIOU'])
```
[5. Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028)
```python
def get_middle(s):
  return string[int(len(string) / 2)] if len(string) % 2 != 0 else string[int(len(string) / 2) - 1: int(len(string) / 2) + 1]
```
[6. All Star Code Challenge #1](https://www.codewars.com/kata/5863f97fb3a675d9a700003f/python)
```python
def sum_ppg(playerOne, playerTwo):
    return playerOne['ppg'] + playerTwo['ppg']
```
[7. Who likes it?](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)
```python
def likes(array):
    if len(array) <= 1:
        return "%s likes this" % (array[0] if len(array) == 1 else "no one")
    else:
        if 2 <= len(array) <= 3:
            array.insert(-1, 'and')
            if len(array) == 3:
                return "%s like this" % ' '.join(array)
            else:
                return "%s like this" % (', '.join(array[0:2]) + ' ' + ' '.join(array[2:]))
        else:
            cnt = len(array) - 2
            return "%s and %s others like this" % (', '.join(array[0:2]), cnt)
```
[8. Array.diff](https://www.codewars.com/kata/523f5d21c841566fde000009/python)
```python
def array_diff(list1, list2):
    new_list = []
    [new_list.append(i) for i in list1 if i not in list2]
    return new_list
```
[9. All Star Code Challenge #22](https://www.codewars.com/kata/5865cff66b5699883f0001aa)
```python
def number2hour_minutes(seconds):
    return f"{seconds//3600} hour(s) and {seconds%3600//60} minute(s)"
```
