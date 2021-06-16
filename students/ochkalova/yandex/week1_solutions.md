## [1. Кондиционер](https://contest.yandex.ru/contest/27393/problems/A/)

```python
troom, tcond = (int(i) for i in input().split())
mode = input()
if mode == "auto":
	print(tcond)
elif mode == "freeze":
	if troom > tcond:
		print(tcond)
	else:
		print(troom)
elif mode == "heat":
	if troom < tcond:
		print(tcond)
	else:
		print(troom)
elif mode == "fan":
	print(troom)
```

## [2. Треугольник](https://contest.yandex.ru/contest/27393/problems/B/)

```python
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and c + b > a:
	print("YES")
else:
	print("NO")
```

## [3. Телефонные номера](https://contest.yandex.ru/contest/27393/problems/C/)

```python
old_num, *nums = tuple(input().replace("-", "") for i in range(4))
if len(old_num) > 7:
	old_code = old_num.replace(")","")[-10:-7]
else:
	old_code = "495"
for num in nums:
	if num[-7:] == old_num[-7:]:
		if len(num) > 7:
			code = num.replace(")","")[-10:-7]
		else:
			code = "495"
		if code == old_code:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
```
