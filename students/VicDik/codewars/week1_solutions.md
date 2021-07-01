# 1. [Opposite number](https://www.codewars.com/kata/reviews/56deebdf6a5c28baa900003b/groups/56ef47f804b6a49d7100190f)
```python
def opposite(number):
    return -1 * number
```
    
# 1. Unique on order
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
