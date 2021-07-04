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
