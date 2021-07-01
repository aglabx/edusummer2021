# [1. Opposite number](https://www.codewars.com/kata/reviews/56deebdf6a5c28baa900003b/groups/56ef47f804b6a49d7100190f).
```python
def opposite(number):
    return -1 * number
```

# [2 [Even or Odd].(https://www.codewars.com/kata/reviews/53da3de52a289a37bc00128a/groups/53ea21bc7b5dfef3e30006f8)
```python
def even_or_odd(number):
    if number % 2 != 0:
        return("Odd")
    else:
        return("Even")
```

# [3. Vowel Count].(https://www.codewars.com/users/VicDik/completed_solutions)

```python
def get_count(input_str):
    vowels = ["a", "e", "i", "o", "u"]
    return sum(input_str.count(i) for i in vowels)
```

# [4. Disemvowel Trolls].(https://www.codewars.com/users/VicDik/completed_solutions)

```python
def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i,"")
    return string_
```
# [5. Get the Middle Character].(https://www.codewars.com/users/VicDik/completed_solutions)

```python
def get_middle(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    elif len(s) % 2 != 0:
        return s[len(s) // 2]
```

# [6. All Star Code Challenge #1].(https://www.codewars.com/kata/reviews/586435fe812998c93400129b/groups/586570e0ece9e8b0a2000ed8)

```python
def sum_ppg(player_one, player_two):
    return player_one['ppg'] + player_two['ppg']
```

# [Other. Unique on order.] 
```python
def unique_in_order(unique:str):
    list_1 = []
    for id in range(len(unique)):
        if id == len(unique) - 1:
            list_1.append(unique[id])
        elif unique[id] == unique[id + 1]:
            pass
        else:
            list_1.append(unique[id])
    return list_1
 ```
