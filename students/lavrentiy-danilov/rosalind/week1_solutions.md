
**Task 1**

After downloading and installing Python, type import this into the Python command line and see what happens. Then, click the "Download dataset" button below and copy the Zen of Python into the space provided.

_**code:**_

```import this```

**Task 2**

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

_**code:**_

```
def triangle_hypotenuse(path):
       '''This function allows you to calculate the square 
       of the hypotenuse of a triangle from the two cathets.
       As an input, the function takes the path to the file that 
       contains two numbers - the lengths of the cathets 
       '''
       with open(path, 'r') as file:
           a, b = map(int, file.readline().split())
       return a**2 + b**2 
```
    
_**Task 3**_

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

_**code:**_
```
  def slice_string(path):
      '''This function allows you to slice a line in two places.
      The function receives as input a file with a string and coordinates
      '''
      with open(path, 'r') as file:
          firstNlines = file.readlines()[0:2]
          s = firstNlines[0][:-1]
          coordinates = firstNlines[1].split()
      return s[int(coordinates[0]):int(coordinates[1])+1] + str(' ') + s[int(coordinates[2]):int(coordinates[3])+1]
```

_**Task 4**_

Given: Two positive integers a and b (a< b < 10000).

Return: The sum of all odd integers from a through b, inclusively.

_**code:**_
```
def sum_between(path):
    '''Calculates the sum of all integers for a given range.'''
    with open(path, 'r') as file:
        a, b = map(int, file.readline().split())
    return sum(range(a, b+1))
```

_**Task 5**_   

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

_**code:**_
```
import itertools
import sys

def get_even_rows(path, path_out):
    with open(path, 'r') as file, open(path_out, 'w') as output:
        for el in  list(itertools.islice(file, 1, None, 2)):
            output.write(el)
```

_**Task 6**_   

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

_**code:**_
```
def calculate_words(path, out_path):
    words_list = []
    words_dict = {}
    with open(path, 'r') as file:
        for line in file:
            words_list = line.split()
    for el in words_list:
        if el in words_dict.keys():
            words_dict.update({el: words_dict.get(el)+1})
        else:
            words_dict.update({el: 1})
```    
    with open(out_path, 'w') as output_file:
        for keys in words_dict:
            st_wr = str(keys) + str(' ') + str(words_dict.get(keys))
            output_file.write(st_wr)
