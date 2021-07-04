# task1 

```python
def IsAscending(A):
    ans = ''
    i = 0
    count = 0
    while i < len(A)-1:
        if float(A[i]) >= float(A[i+1]):
            ans = 'NO'
            break
        else:
            i += 1
    if ans == '':
        ans = 'YES'
    print(ans)
A = input().split()

IsAscending(A)
```

#task 4

```python
n = int(input())
prev = n
s = ''
n = int(input())
if n == -2 * 10 ** 9:
  s = 'CONSTANT'
while n != -2 * 10 ** 9:
  if s != 'RANDOM':
    if prev > n and s == 'DESCENDING':
      s = 'DESCENDING'
    elif prev == n and s == 'DESCENDING':
      s = 'WEAKLY DESCENDING'
    elif prev < n and s == 'DESCENDING':
      s = 'RANDOM'
    elif prev > n and s == 'CONSTANT':
      s = 'WEAKLY DESCENDING'
    elif prev == n and s == 'CONSTANT':
      s = 'CONSTANT'
    elif prev < n and s == 'CONSTANT':
      s = 'WEAKLY ASCENDING'
    elif prev > n and s == 'ASCENDING':
      s = 'RANDOM'
    elif prev == n and s == 'ASCENDING':
      s = 'WEAKLY ASCENDING'
    elif prev < n and s == 'ASCENDING':
      s = 'ASCENDING'
    elif prev > n and s == 'WEAKLY DESCENDING':
      s = 'WEAKLY DESCENDING'
    elif prev == n and s == 'WEAKLY DESCENDING':
      s = 'WEAKLY DESCENDING'
    elif prev < n and s == 'WEAKLY DESCENDING':
      s = 'RANDOM'
    elif prev > n and s == 'WEAKLY ASCENDING':
      s = 'RANDOM'
    elif prev == n and s == 'WEAKLY ASCENDING':
      s = 'WEAKLY ASCENDING'
    elif prev < n and s == 'WEAKLY ASCENDING':
      s = 'WEAKLY ASCENDING'
    elif prev == n and s == '':
      s = 'CONSTANT'
    elif prev > n and s == '':
      s = 'DESCENDING'
    elif prev < n and s == '':
      s = 'ASCENDING'
  prev = n
  n = int(input())
print(s)
```
