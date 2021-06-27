# 1. Sort arrays - 1. https://www.codewars.com/kata/reviews/60926e96b2c8070001711d95/groups/60d0639452c15e0001f67283

```python
import random


def sortme(names):
    if len(names) < 2:
        return names
    pivot = names[random.randint(0, len(names) - 1)]
    
    middle = [i for i in names if i == pivot]
    less = [i for i in names if i < pivot]
    greater = [i for i in names if i > pivot]
    
    return sortme(less) + middle + sortme(greater)
```

# 2. Two to One. https://www.codewars.com/kata/5656b6906de340bd1b0000ac

```python
def longest(a1, a2):
    a = list(set(a1) | set(a2))
    
    for bypass in range(1, len(a)):
        for k in range(len(a) - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
    return ''.join(a)
```

# 3. Sort - one, three, two. https://www.codewars.com/kata/reviews/5af42785ec2ef4a12c0000b0/groups/60d051f82d6e210001264b2b

```python
import random

def quickSort(a):
    """

    :param a:
    :return: sorted a
    """
    if len(a) < 2:
        return a
    pivot = a[random.randint(0, len(a) - 1)]
    middle = [i for i in a if i == pivot]
    less = [i for i in a if i < pivot]
    # print('less', less)
    greater = [i for i in a if i > pivot]
    # print('greater', greater)
    return quickSort(less) + middle + quickSort(greater)


def sort_by_name(arr):
    def int_to_string(number):
        nonlocal transition
        if number:
            string = "{} {}"
            hundreds = {0: '',
                        1: "one hundred",
                        2: "two hundred",
                        3: "three hundred",
                        4: "four hundred",
                        5: "five hundred",
                        6: "six hundred",
                        7: "seven hundred",
                        8: "eight hundred",
                        9: "nine hundred"
                        }

            numerals = {
                0: '',
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine"
            }

            decimals = {
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen"
            }

            rounds = {
                20: "twen",
                30: "thir",
                40: "for",
                50: "fif",
                80: "eigh"
            }

            part_1 = number // 100
            decimal = number % 100

            if decimal < 10:
                part_2 = numerals[decimal]
            elif 10 <= decimal < 20:
                part_2 = decimals[decimal]
            else:
                part_2 = f"{rounds.get(decimal - decimal % 10, numerals[(decimal - decimal % 10) // 10])}ty {numerals[decimal % 10]}"

            name = string.format(hundreds[part_1], part_2).strip()
        else:
            name = "zero"
        if name not in transition:
            transition[name] = number
        return name

    transition = {}

    strings = quickSort(list(map(int_to_string, arr)))

    return [transition[number] for number in strings]
```

# 4. Merge two sorted arrays into one. https://www.codewars.com/kata/reviews/589b9bed66413d26e4000033/groups/60cf8d4d9a9bc1000154b317

```python
# merge sort practise
def merge(a1, a2):
    sorted_arr = [None for _ in range(len(a1) + len(a2))]
    
    i = j = k = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            sorted_arr[k] = a1[i]
            i += 1
        else:
            sorted_arr[k] = a2[j]
            j += 1
        k += 1
    
    sorted_arr[k:] = a1[i:]
    k += len(a1) - i
    sorted_arr[k:] = a2[j:]
    
    return sorted_arr

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    
    return merge(left, right)

def merge_arrays(arr1, arr2):
    array = list(set(arr1) | set(arr2))
    
    return merge_sort(array)
```

# 5. Don't Drink the Water. https://www.codewars.com/kata/reviews/56b26ac972b0b53b4400002e/groups/60d05f092d6e210001264c89

```python
from functools import reduce


def separate_liquids(glass):
    if glass:
        density_chart = {
            'H': 1.36,
            'W': 1.00,
            'A': 0.87,
            'O': 0.8
        }
        height = len(glass)
        width = len(glass[0])
        overall = height * width
        new_arr = reduce(lambda x, y: x + y, glass, [])  # x.extend returns None so it doesn`t work

        for bypass in range(1, overall):
            for i in range(overall - bypass):
                if density_chart[new_arr[i]] > density_chart[new_arr[i + 1]]:
                    new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
        return [[new_arr[w + width * h] for w in range(width)] for h in range(height)]
    return glass
```
