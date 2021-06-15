#Installing Python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

#Variables and Some Arithmetic
a = int(input())
b = int(input())
square_c = a ** 2 + b ** 2
print(square_c)

#Strings and Lists
s = raw_input()
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())
asb = s[a:(b + 1)]
csd = s[c:(d + 1)]
ans = f"{asb} {csd}"
print(ans)

#Conditions and Loops
a = int(raw_input())
b = int(raw_input())
sum = 0
for num in range(a, b + 1):
    if num % 2 == 1:
        sum += num
print(sum)

#Working with Files
input_file = open('rosalind_ini.txt', 'r')
output_file = open('answer.txt', 'w')
count = -1
for line in input_file:
    count += 1
    if count % 2 == 1:
        output_file.write(line)
output_file.close()

#Dictionaries
lst = raw_input().split()
dct = {}
for s in lst:
    if s not in dct:
        dct[s] = 1
    else:
        dct[s] += 1
for key in dct:
    print(key, dct[key])
