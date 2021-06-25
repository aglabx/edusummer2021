### Task 1
Opposite number (https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python)

```
def opposite(number):
    return -number
```

### Task 2
Even or Odd 

Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

```
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
```

### Task 3
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

```
def count_vowels(short_string):
    return reduce(lambda x, y: x + (y in 'aeiou'), short_string, 0)
```

### Task 4
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

```
def disemvowel(string):
    string_ = ''.join(char for char in string if char not in set('aeiouAEIOU'))
    return string_
```

### Task 5
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

```
def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2-1):int(len(s)/2+1)]
    else:
        return s[int(len(s)/2)]
```

### Task 6
Write a function, called sumPPG, that takes two NBA player objects/struct/Hash/Dict/Class and sums their PPG


```
def sum_ppg(playerOne, playerTwo):
    return  playerOne.get('ppg') + playerTwo.get('ppg')
```

### Task 7
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item

```
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
         return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:
        return '{}, {} and {} others like this'. format(names[0], names[1], (len(names) - 2))
```

### Task 8
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

```
def array_diff(a, b):
    a_new = []
    for el in a:
        if el not in b:
            a_new.append(el)
        else:
            continue
    return a_new
```

### Task 9
Create a function that takes an integer argument of seconds and converts the value into a string describing how many hours and minutes comprise that many seconds.

Any remaining seconds left over are ignored.

```
def to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return '{} hour(s) and {} minute(s)'.format(hours, minutes)
```
