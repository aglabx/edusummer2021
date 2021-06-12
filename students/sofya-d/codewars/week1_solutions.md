#Opposite number
def opposite(number):
  return -1 * number


#Even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return('Even')
    return('Odd')


#Vowel count
def get_count(input_str):
    num_vowels = 0
    for i in input_str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels += 1
    return num_vowels


#Disemvowel Trolls
def disemvowel(string_):
    string_l = string_.lower()
    c = 0
    for i in range(len(string_l)):
        if string_l[i] in 'aeiou':
            string_ = string_[:i - c] + string_[i + 1 - c:]
            c += 1
    return string_


#Get the Middle Character
def get_middle(s):
    lnth = len(s)
    if lnth % 2 == 0:
        return s[lnth // 2 - 1] + s[lnth // 2]
    else:
        return s[lnth(s) // 2]


#All Star Code Challenge #1
def sum_ppg(playerOne, playerTwo):
    return playerOne["ppg"] + payerTwo["ppg"]


#Who likes it?
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names)==1:
        return names[0]+' likes this'
    elif len(names)==2:
        return names[0]+' and '+names[1]+' like this'
    elif len(names)==3:
        return names[0]+', '+names[1]+' and '+names[2]+' like this'
    elif len(names)>3:
        return names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this'


#Array.diff
def array_diff(a, b):
    c = []
    for i in a:
        c.append(i)
    if len(a)==0 or len(b)==0:
        return a 
    else:
        for i in range(len(b)):
            for j in range(len(a)):
                if b[i]==a[j] and a[j] in c:
                    c.remove(a[j])
        return c


All Star Code Challenge #22
def to_time(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    return str(hours)+' hour(s) and '+str(minutes)+' minute(s)'
