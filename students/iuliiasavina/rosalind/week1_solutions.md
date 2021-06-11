## Variables and Some Arithmetic

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

Solution:

`a = int(input())`

`b = int(input())`

`print (a**2 + b**2)`

## Strings and Lists

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Solution:

`s = str(input())`

`a, b, c, d = int(input()), int(input()), int(input()), int(input())`

`print (s[a:b+1] + ' ' + s[c:d+1])`

## Conditions and Loops 

Given: Two positive integers aa and bb (a<b<10000a<b<10000).

Return: The sum of all odd integers from aa through bb, inclusively.

Solution:

`a = int(input())`
`b = int(input())`
`l = []`
`while a <= b:`
    `if a % 2 != 0:`
        `l.append(a)`
    `a = a + 1`
`print (sum(l))`

## Working with Files

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Solution:

`f = open('input.txt', 'r')`
`lines = f.readlines()`
`e = []`
`for i in range (0, len(lines)):`
    `if i % 2 != 0:`
        `e.append(i)`
`even_lines = []`
`for i in e:`
    `even_lines.append(lines[i])`
`f.close()`
`f2 = open('output.txt', 'w')`
`for i in even_lines:`
    `f2.write(str(i) + '\n')`
`f2.close()`

## Dictionaries

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

Solution:

`string = open('string.txt', 'r')`
`s = str(string.readline())`
`d = {}`
`for word in s.split():` 
    `if word in d:`
        `d[word] += 1`
    `else:`
        `d[word] = 1`
`for key, value in d.items():`
    `print (key, value)`
`string.close()
