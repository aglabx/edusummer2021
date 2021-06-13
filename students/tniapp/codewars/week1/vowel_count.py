# Return the number (count) of vowels in the given string.

def get_count(input_str):
    num_vowels = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for letter in input_str:
        if letter in vowel_list:
            num_vowels += 1
    return num_vowels
