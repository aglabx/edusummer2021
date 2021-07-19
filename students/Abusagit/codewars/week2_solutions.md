# 1. Human Readable Time 5. 

```python
def make_readable(seconds):
    string = "{0}:{1}:{2}"
    hours = str(seconds // 3600)
    minutes = str((seconds % 3600 ) // 60)
    seconds = str(seconds % 60)
    
    form = map(lambda x: x.zfill(2) if len(x) < 2 else x, (hours, minutes, seconds))
    
    return string.format(*form)
```



# 2. Isograms 7.



```python
def is_isogram(string):
    return True if len(set(string.lower())) == len(string) else False
```



# 3. Categorize New Member. https://www.codewars.com/kata/reviews/5502c9e8b3216ec63c0001ac/groups/5f4c6dfd69f1cd00010f1425



```python
def open_or_senior(data):
    return ["Open" if age < 55 or handicap <=7 else "Senior" for (age,handicap) in data]
```



# 4. Vasya - Clerk. https://www.codewars.com/kata/reviews/55589d81abe7a58e08000060/groups/60d5c17eda859b000165f111



```python
def tickets(people, index=0,stock=None):
    stock = stock or {x: 0 for x in (25, 50, 100)}
    for i in range(index, len(people)):
        if people[i] == 25:
            stock[25] += 1
        elif people[i] == 50:
            if not stock[25]:
                return "NO"
            else:
                stock[25] -= 1
                stock[50] += 1
        else:
            if stock[25] >= 3:
                stock2 = stock.copy()
                stock2[25] -= 3
                stock2[100] += 1
                path_1 = tickets(people, index=i+1, stock=stock2)
            else:
                path_1 = "NO"
            if stock[50] >= 1 and stock[25] >= 1:
                stock3 = stock.copy()
                stock3[50] -= 1
                stock3[25] -= 1
                stock3[100] += 1
                path_2 = tickets(people, index=i+1, stock=stock3)
            else:
                path_2 = "NO"
            return "YES" if any((path_1 == "YES", path_2 == "YES")) else "NO"
    return "YES"
```



# 5. The Supermarket Queue 6. https://www.codewars.com/kata/57b06f90e298a7b53d000a86/solutions/python/me/best_practice



```python
class BinHeapMin:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def __bool__(self):
        return len(self.heapList) > 1
    
    def __len__(self):
        return len(self.heapList) - 1
    
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList.extend(alist)
        print(len(self.heapList), i)
        while i > 0:
            print(self.heapList, i)
            self.percDown(i)
            i -= 1
        print(self.heapList, i)
                        
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i], self.heapList[mc] = self.heapList[mc], tmp
            i = mc
                
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i //= 2
    
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def getMin(self):
        return self.heapList[1]
    
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False


def queue_time(customers, n):
    if customers:
        if n >= len(customers):
            return max(customers)
        prior_queue = BinHeapMin()
        time = 0
        for customer in customers:
            if len(prior_queue) < n:
                prior_queue.insert(time + customer)
            else:
                time = prior_queue.delMin()
                prior_queue.insert(time + customer)
        if prior_queue:
            while prior_queue:
                    time = prior_queue.delMin()
        return time
    return 0
```



# 6. Sum of a sequence. https://www.codewars.com/kata/reviews/587a9bf3e9665e4a4e00121a/groups/587fe4fbb43c40107b002110



```python
def sequence_sum(begin_number, end_number, step):
    return sum(i for i in range(begin_number, end_number + 1, step))
```



# 7. Sum of a Beach. https://www.codewars.com/kata/5b37a50642b27ebf2e000010/solutions/python/me/best_practice



```python
def prefix(s: str) -> list:
    """
    Creates prefix function for KMP algorithm
    """
    P = [0 for _ in range(len(s))]
    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]
        elif i:  # i > 0
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P


def kmp(string, substring):
    """
    Performs KMP search
    """
    sub_len = len(substring)
    str_len = len(string)
    if not str_len or sub_len > str_len:
        return []
    P = prefix(substring)
    entries = []
    i = j = 0
    while i < str_len and j < sub_len:
        if string[i] == substring[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        # string[i] != substring[j]:
        elif j:  # j > 0
            j = P[j - 1]
        else:
            i += 1
    return entries

def sum_of_a_beach(beach):
    return sum(len(kmp(beach.lower(), entry)) for entry in ("sand", "water", "fish", "sun"))


# OR
import re


def sum_of_a_beach(beach):
    return len(re.findall('Sand|Water|Fish|Sun', beach, re.IGNORECASE))
```



# 8. Alphabet war. https://www.codewars.com/kata/59377c53e66267c8f6000027/solutions/python/me/best_practice



```python
def alphabet_war(fight):
    war = {"left": 0, "right": 0}
    cost = {letter: [points, side] for letter, points, side in zip("wpbsmqdz", (4, 3, 2, 1, 4, 3, 2, 1), 
                                                              ("left", "left", "left", "left", "right", "right", "right", "right"))}
    for letter in fight.lower():
        if letter in cost:
            war[cost[letter][1]] += cost[letter][0]
        
    if war["left"] == war["right"]:
        return "Let's fight again!"
    
    win = "%s side wins!"
    
    return win % "Left" if war["left"] > war["right"] else win % 'Right'

```



# 9. Create Phone Number. https://www.codewars.com/kata/525f50e3b73515a6db000b83



```python
def create_phone_number(n):
    string = "({}{}{}) {}{}{}-{}{}{}{}"
    return string.format(*n)
```



# 10. Rot13. https://www.codewars.com/kata/530e15517bc88ac656000716/solutions/python/me/best_practice



```python
def rot13(message):
    a ="abcdefghijklmnopqrstuvwxyz"
    code = {letter: substitute for letter, substitute in zip(a, ''.join((a[13:], a[:13])))}
    
    encoded = [letter for letter in  message]
    for i, letter in enumerate(message):
        if letter.isalpha():
            if letter.islower():
                encoded[i] = code[letter]
            else:
                encoded[i] = code[letter.lower()].upper()
    
    return ''.join(encoded)
```



# 11. Strip Comments 4. https://www.codewars.com/kata/51c8e37cee245da6b40000bd/solutions/python/me/best_practice



```python
def solution(string,markers):
    markers = set(markers)
    lines = string.split('\n')
    
    print(lines)
    for i in range(len(lines)):
        for index, value in enumerate(lines[i]):
            if value in markers:
                lines[i] = lines[i][:index].strip()
                break
    return '\n'.join(lines)
```

