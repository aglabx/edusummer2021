# 1. Unique on order
```
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
