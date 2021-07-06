# 1. Opposite number. https://www.codewars.com/kata/reviews/56deebdf6a5c28baa900003b/groups/56ef47f804b6a49d7100190f

```python
def opposite(number):
    return -1 * number
```

# 2. Even or Odd. https://www.codewars.com/kata/reviews/53da3de52a289a37bc00128a/groups/53ea21bc7b5dfef3e30006f8

```python
def even_or_odd(number):
    if number % 2 != 0:
        return('Odd')
    else:
        return('Even')
        
#второе решение 

def even_or_odd(number):
    return 'Odd' if x % 2 == 0 else 'Even' 
```

# 3. Vowel Count. https://www.codewars.com/users/VicDik/completed_solutions

```python
#Старое решение
def get_count(input_str):
    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = "aeuoi"
    return sum(input_str.count(i) for i in vowels)
    
#Новое решение
def get_count(input_str):
    return sum(letter in 'aeiou' for letter in input_str)
```

# 4. Disemvowel Trolls. https://www.codewars.com/users/VicDik/completed_solutions

```python
#Старое решение 

def disemvowel(string_):
    for i in 'aeiouAEIOU':
        string_ = string_.replace(i,'')
    return string_
    
#Новое решение 

def disemvowel2(string):
    return ''.join(i for i in string if i not in "aeiouAEIOU")
    
#Еще одно

def disemvowel(string):
    return ''.join(filter(lambda x: not x in "aeiouAEIOU", string))
```

# 5. Get the Middle Character. https://www.codewars.com/users/VicDik/completed_solutions

```python
def get_middle(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    else:
        return s[len(s) // 2]
```

# 6. All Star Code Challenge #1. https://www.codewars.com/kata/reviews/586435fe812998c93400129b/groups/586570e0ece9e8b0a2000ed8

```python
def sum_ppg(player_one, player_two):
    return player_one['ppg'] + player_two['ppg']
```

# 7. Who likes it?. https://www.codewars.com/users/VicDik/completed_solutions

```python
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
```

# 8. Array_diff. https://www.codewars.com/users/VicDik/completed_solutions

```python
#Старое решение 

def array_diff(a, b):
    list_1 = []
    for i in a:
        if i in b:
            pass
        else:
            list_1.append(i)
    return(list_1)
    
#Новое решение 

def array_diff(a,b):
    return [i for i in a if not (i in b)]

```

# 9. All Star Code Challenge #22. https://www.codewars.com/users/VicDik/completed_solutions

```python
def to_time(seconds):
    time = f'{seconds//3600} hour(s) and {seconds%3600//60} minute(s)'
    return time
```

# 10. Unique on order. 

```python
#Старое исправленное решение

def unique_on_order(unique:str):
    elements = []
    len_unique = len(unique)
    for id in range(len_unique):
        if id == len_unique - 1:
            elements.append(unique[id])
        elif unique[id] == unique[id + 1]:
            pass
        else:
            elements.append(unique[id])
    return elements

#Сначала я сделала так

def unique_on_order2(unique):
    unique_list = []
    for i in unique:
        if len(unique_list) == 0 or i != unique_list[-1]:
            unique_list.append(i)
print(unique_list)

#Не поняла, как решать через filter в одну строчку, но сделала в одну вот так

unique_on_order3 = lambda str_unique: [str_unique[i] for i in range(len(str_unique)) if i == 0 or str_unique[i] != str_unique[i - 1]]
```
