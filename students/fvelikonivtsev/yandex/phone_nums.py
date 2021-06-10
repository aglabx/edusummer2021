import sys


def transform(number: str):
    for sign in '+()-':
        if sign in number:
            number = number.replace(sign, '')
    if len(number) < 11:
        number = '8495' + number
    return number[1:]


def comparator(current_number, number_to_compare): # TODO
    return 'YES' if current_number == number_to_compare else 'NO'

def comparator2(initial, number_to_compare):
    i = j = -1
    while - i <= len(initial) and - j <= len(number_to_compare):
        sign1 = initial[i]
        sign2 = number_to_compare[j]
        


stdin = iter(sys.stdin.read().strip().split('\n'))
# initial_number = transform(next(stdin))
# for number_ in stdin:
#     sys.stdout.write(f'{comparator(initial_number, transform(number_))}\n')

initial_num = next(stdin)

for
