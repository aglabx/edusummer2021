## **[1. Opposite number](https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python)**

```python
def opposite(number):
  return(-number)
```

## **[2. Even or odd](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python)**

```python
def even_or_odd(number):
  if number % 2 == 0:
    return ("Even")
else:
  return ("Odd")
```

## **[3. Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python)**

```python
def get_count(input_str):
  num_vowels = 0
  for vowel in input_str:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
      num_vowels += 1
  return num_vowels
```

## **[4. Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python)**

```python
def disemvowel(string_):
  l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  s = []
  for vowel in string_:
    if not vowel in l:
      s.append(vowel)
  string_ = ''.join(s)
  return (string_)
```

## **[Get the Middle  Character](https://www.codewars.com/kata/56747fd5cb988479af000028/train/python)**

```python
def get_middle(s):
    index = (len(s)) // 2
    if len(s) % 2 != 0:
        return (s[index])
    else:
        return (s[index - 1: index + 1])
```

## **[All Star Code Challenge #1](https://www.codewars.com/kata/5863f97fb3a675d9a700003f/train/python)**

```python
def sum_ppg(playerOne, playerTwo):
    return (playerOne['ppg'] + playerTwo['ppg'])
```

## **[All Star Code Challenge #22](https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python)**

```python
def to_time(seconds):
    h = seconds // 3600
    m = (seconds - h*3600) // 60
    return (str(h) + " hour(s) and " + str(m) + " minute(s)") 
```

## **[Who likes it?](https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python)**

```python
def likes(names):
    if len(names) == 0:
        return ("no one likes this")
    elif len(names) == 1:
        return (str(names[0]) + " likes this")
    elif len(names) == 2:
        return (str(names[0]) + " and " + str(names[1]) + " like this")
    elif len(names) == 3:
        return (str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this")
    else:
        return (str(names[0]) + ", " + str(names[1]) + " and " + str(len(names) - 2) + " others like this")
    pass
```
