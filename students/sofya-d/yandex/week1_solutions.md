#Верно решено всего 2 задачи
#Кондиционер (верно)
t = input().split()
m = input()
t[0] = int(t[0])
t[1] = int(t[1])
if (m == 'freeze' and t[0] > t[1]) or (m == 'heat' and t[0] < t[1]) or (m == 'auto'):
    print(t[1])
else:
    print(t[0])

#Треугольник (верно)
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

#Телефонные номера (WA, тест 1)
n1 = ''.join(list(filter(lambda x: x not in ')(-+', input())))
n2 = ''.join(list(filter(lambda x: x not in ')(-+', input())))
n3 = ''.join(list(filter(lambda x: x not in ')(-+', input())))
new = ''.join(list(filter(lambda x: x not in ')(-+', input())))
n = [n1, n2, n3, new]
ed = []
for str in n:
    if len(str) == 11:
        str = str[1:len(str)]
    else:
        str = f"495{str}"
    ed.append(str)
for i in range(len(ed) - 1):
    if ed[3] in ed[i]:
        print("YES")
    else:
        print("NO")

#Уравнение с корнем (RE, тест 4)
a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print("NO SOLUTION")
else:
    if a == 0 and b >= 0 and b ** 0.5 == c:
        print("MANY SOLUTIONS")
    if a == 0 and (b < 0 or b ** 0.5 != c):
        print("NO SOLUTIONS")
    else:
        x = (c ** 2 - b) / a
        if (a * x + b) >= 0 and (a * x + b) ** 0.5 == c:
            if x == 0.0:
                print(int(x))
            elif x != 0.0 and abs(x % int(x)) == 0.0:
                print(int(x))
            else:
                print("NO SOLUTION")

#Скорая помощь (не сходятся ответы с ответами из примеров)
kv1, et, kv2, pod2, et2 = map(lambda x: int(x), input().split())
if kv2 % (et2 + et * (pod2 - 1)) > 0:
    pl = kv2 // (et2 + et * (pod2 - 1)) + 1
else:
    pl = kv2 // (et2 + et * (pod2 - 1))
if kv1 % pl > 0:
    vet1 = kv1 // pl + 1
else:
    vet1 = kv1 // pl
if vet1 % et > 0:
    pod1 = vet1 // et + 1
else:
    pod1 = vet1 // et
if (kv1 - (pod1 - 1) * pl * et) % pl > 0:
    et1 = (kv1 - (pod1 - 1) * pl * et) // pl + 1
else:
    et1 = (kv1 - (pod1 - 1) * pl * et) // pl
if kv2 not in range(((vet1 - 1) * pl + 1), vet1 * pl):
    pod1 = -1
    et1 = -1
print(pod1, et1)

#Расстановка ноутбуков (WA, тест 3)
inp = [int(c) for c in input().split(' ')]
S_laptops = inp[0] * inp[1] + inp[2] * inp[3]
a = 0
b = 0
table_side1 = max([min(inp[0:2]), min(inp[2:4])])
table_side2 = max(inp[0:2]) + max(inp[2:4]) + 1
m = range(table_side1, table_side2)
for i in range(len(m)):
    a = m[i]
    for j in range(len(m)):
        b = m[j]
        if a * b >= S_laptops:
            break
    break
print(a, b)

#Детали (TL, тест 14)
weight = [int(n) for n in input().split(' ')]
d = 0
while lst[0] >= lst[1]:
    nok = weight[0] % weight[1]
    ck = weight[0] // weight[1]
    kom = (weight[1] % weight[2]) * ck
    cm = (weight[1] // weight[2]) * ck
    d += cm
    lst[0] = nok + kom
print(d)

#Метро (ответ не сходится с ответом из примера, WA тест 1)
train_int_path1 = int(input())
train_int_path2 = int(input())
trains_path1 = int(input())
trains_path2 = int(input())
min1 = train_int_path1 * trains_path1 - train_int_path1 + trains_path1
max1 = train_int_path1 * trains_path1 + 2 * train_int_path1 + trains_path1
min2 = train_int_path2 * trains_path2 - train_int_path2 + trains_path2
max2 = train_int_path2 * trains_path2 + 2 * train_int_path2 + trains_path2
time_path1 = []
time_path2 = []
for time1 in range(min1, max1 + 1):
    time_path1.append(time1)
for time2 in range(min2, max2 + 1):
    time_path2.append(time2)
if len(list(set(time_path1) & set(time_path2))) == 0:
    print(-1)
else:
    print(max([min1, min2]), min([max1, max2]))

#Узник замка ИФ (WA, тест 5)
a = input()
b = input()
c = input()
d = input()
e = input()
block = [a, b, c]
hole = [d, e]
small_bsides = []
for bside in block:
    for hside in hole:
        if bside <= hside:
            small_bsides.append(bside)
if len(small_bsides) >= 2:
    print("YES")
else:
    print("NO")

#Система линейных уравнений - 2 (WA, тест1)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
#нет решений (предположение: знаменатели, делить на 0 нельзя)
if d * a - b * c == 0 or d * a - d * e == 0:
    print(0)
#множество решений вида y = k + bx (из примера)
if e / a = f / d and b / a = c / d:
    print(1, f / d, -1 * (c / d))
#единственное решение (из примера)
if (a == 0 and d == 0) or (b == 0 and c == 0):
    print(2, (d * e - f * b)/(d * a - b * c), (f * a - c * e)/(d * a - b * e))
#бесконечно много решений вида x = x0, y — любое (по аналогии)
if b == 0 and d == 0:
    print(3, (d * e - f * b) / (d * a - b * c))
#бесконечно много решений вида y = y0, x — любое (из примера)
if a == 0 and c == 0:
    print(4, (f * a - c * e)/(d * a - b * e))
#любая пара чисел (x,y) является решением (предположение)
if a == 0 and b == 0 and c == 0 and d == 0:
    print(5)
