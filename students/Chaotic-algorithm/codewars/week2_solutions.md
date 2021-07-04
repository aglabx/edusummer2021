# 2.1. Human Readable Time. https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

```python
def make_readable(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
```

# 2.2. Isograms. https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

```python
def is_isogram(string):
    string_low = string.lower()
    return len(string_low) == len(set(string_low))
```

# 2.3. Categorize New Member. https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

```python
def open_or_senior(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]
```

# 2.4. Vasya - Clerk. https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

```python
def tickets(people):
    dict_money = {25: 0, 50: 0, 100: 0}
    for i in people:
        if i == 25:
            dict_money[25] += 1
        elif i == 50:
            if dict_money[25] >= 1:
                dict_money[50] += 1
                dict_money[25] -= 1
            else:
                return "NO"
        elif i == 100 and dict_money[50] == 0:
            dict_money[100] += 1
            dict_money[25] -= 3
        elif i ==100 and dict_money[50] >= 1:
            dict_money[50] -= 1
            dict_money[25] -= 1
            dict_money[100] += 1
        if dict_money[25] < 0 or dict_money[50] < 0:
            return "NO"
    return "YES"
```

# 2.5. The Supermarket Queue. https://www.codewars.com/kata/57b06f90e298a7b53d000a86

```c++
long queueTime(std::vector<int> customers,int n){
  std::vector<long> cust_tills(n, 0);
  
  for (int i = 0; i < customers.size(); i++) {
    cust_tills[0]+=customers[i];
    std::sort(cust_tills.begin(), cust_tills.end());
}
  return cust_tills[n-1];
}

// На питоне получилось красивое решение через кучи, но раз нужно одно решение, закину его в виде коммента
// import heapq
// def queue_time(customers, n):
//     tills_time = [0] * n
//     for i in customers:
//         heapq.heapreplace(tills_time, tills_time[0] + i)
//     return max(tills_time)
```

# 2.6. Sum of a sequence. https://www.codewars.com/kata/586f6741c66d18c22800010a

```python
def sequence_sum(start, end, step):
    if end >= start:
        return sum([i for i in range(start, end + 1, step)])
    else:
        return 0
```

# 2.7. Sum of a Beach. https://www.codewars.com/kata/5b37a50642b27ebf2e000010

```python
def sum_of_a_beach(string):
    return sum(string.lower().count(i) for i in ["water", "sand", "fish", "sun"])
```

# 2.8. Alphabet war. https://www.codewars.com/kata/59377c53e66267c8f6000027

```python
def alphabet_war(fight):
    fight_list = list(fight)
    count_left = 0
    count_right = 0
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    for k1, k2 in zip(left_side.keys(), right_side.keys()):
        for i in fight_list:
            if i == k1:
                count_left += left_side[i]
            elif i == k2:
                count_right += right_side[i]
    if count_left == count_right:
        return "Let's fight again!"
    elif count_left > count_right:
        return "Left side wins!"
    else:
        return "Right side wins!"
```

# 2.9. Create Phone Number. https://www.codewars.com/kata/525f50e3b73515a6db000b83

```python
def create_phone_number(n):
    number = ''.join(str(ints) for ints in n)
    return "({}) {}-{}".format(number[:3], number[3:6], number[6:])
```

# 2.10. Rot13. https://www.codewars.com/kata/530e15517bc88ac656000716

```c++
#include <string>
#include <iostream>

std::string rot13(std::string msg)
{
  for (char& s : msg){
    s = islower(s) ? 'a' + (s - 'a' + 13) % 26:
        isupper(s) ? 'A' + (s - 'A' +13) % 26: \
    s;
  }
  return msg;
}
```

# 2.11. Strip Comments. https://www.codewars.com/kata/51c8e37cee245da6b40000bd

```python
def solution(string, markers):
    comment = string.split('\n')
    for i in markers:
        comment = [n.split(i)[0].rstrip() for n in comment]
    return '\n'.join(comment)
```
