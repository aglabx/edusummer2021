## [1. Opposite number] (https://www.codewars.com/kata/56dec885c54a926dcd001095)

```c++
int opposite(int number) 
{
  return number*(-1);
}
```

## [2. Even or Odd] (https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)

```c++
std::string even_or_odd(int number) 
{
  if (number%2==0) {
    return "Even";
  }
  else {
    return "Odd";
  }
}
```

## [3. Vowel Count] (https://www.codewars.com/kata/54ff3102c1bad923760001f3)

```c++
#include <string>

using namespace std;

int getCount(const string& inputStr){
  int num_vowels = 0;
  int a_count = std::count(inputStr.begin(), inputStr.end(), 'a');
  int e_count = std::count(inputStr.begin(), inputStr.end(), 'e');
  int i_count = std::count(inputStr.begin(), inputStr.end(), 'i');
  int o_count = std::count(inputStr.begin(), inputStr.end(), 'o');
  int u_count = std::count(inputStr.begin(), inputStr.end(), 'u');
  num_vowels=a_count+e_count+i_count+o_count+u_count;
  return num_vowels;
}
```

## [4.Disemvowel Trolls] (https://www.codewars.com/kata/52fba66badcd10859f00097e)

```python
import re
def disemvowel(string_):
    return re.sub('[aeiou]','',string_,flags=re.IGNORECASE)
```

## [5. Get the Middle Character] (https://www.codewars.com/kata/56747fd5cb988479af000028)

```c++
#include <string>
std::string get_middle(std::string input) 
{
  // return the middle character(s)
  int mid=input.length()/2;
  std::string characters = "";
  if (input.length()%2==0) {
    characters += input[mid-1];
    characters += input [mid];
    return characters;
  }
  else {
     return characters += input [mid];
  }
}
```

## [6. All Star Code Challenge #1] (https://www.codewars.com/kata/5863f97fb3a675d9a700003f/python)

```python
def sum_ppg(playerOne, playerTwo):
    for (k1,v1), (k2,v2) in zip(playerOne.items(), playerTwo.items()):
        if k1=='ppg' and k2=='ppg':
            return v1+v2
```

## [7. Who likes it?] (https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

```python
def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return "{} likes this".format(names[0])
    elif len(names)==2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names)==3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1],len(names)-2)
```

## [8. Array.diff] (https://www.codewars.com/kata/523f5d21c841566fde000009/python)

```python
def array_diff(a, b):
    diff_list = [x for x in a if x not in b]
    return diff_list
```

## [9. All Star Code Challenge #22] (https://www.codewars.com/kata/5865cff66b5699883f0001aa)

```python
def to_time(seconds):
    if seconds<3600:
        minutes=int(round(seconds/3600*60, 2))
        return '0 hour(s) and {} minute(s)'.format(minutes)
    if seconds>=3600:
        hours=int(seconds/3600)
        for_min=(seconds/3600 - int(seconds/3600))
        minutes=int(round(for_min*60,2))
        return '{} hour(s) and {} minute(s)'.format(hours,minutes)
```
