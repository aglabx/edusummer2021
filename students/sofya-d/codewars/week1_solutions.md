#Opposite number
def opposite(number):
  return -1 * number


#Even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


#Vowel count
def get_count(str):
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for letter in str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels


#Disemvowel Trolls
def disemvowel(str):
    return "".join([x for x in str if not x in "aeiou"])


#Get the Middle Character
def get_middle(str):
    length = len(str)
    if length % 2 == 0:
        return str[length // 2 - 1:length // 2 + 1]
    else:
        return str[length // 2]


#All Star Code Challenge #1
def sum_ppg(playerOne, playerTwo):
    return playerOne["ppg"] + payerTwo["ppg"]


#Who likes it?
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names)>3:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


#Array.diff
def array_diff(a, b):
    return [num for num in a if num not in b]


#All Star Code Challenge #22
def to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"
