import random
import sys

def quickSort(a):
    """

    :param a:
    :return: sorted a
    """
    if len(a) < 2:
        return a
    pivot = a[random.randint(0, len(a) - 1)]
    middle = [i for i in a if i == pivot]
    less = [i for i in a if i < pivot]
    # print('less', less)
    greater = [i for i in a if i > pivot]
    # print('greater', greater)
    return quickSort(less) + middle + quickSort(greater)


def sort_by_name(arr):
    def int_to_string(number):
        nonlocal transition
        if number:
            string = "{} {}"
            hundreds = {0: '',
                        1: "one hundred",
                        2: "two hundred",
                        3: "three hundred",
                        4: "four hundred",
                        5: "five hundred",
                        6: "six hundred",
                        7: "seven hundred",
                        8: "eight hundred",
                        9: "nine hundred"
                        }

            numerals = {
                0: '',
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine"
            }

            decimals = {
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen"
            }

            rounds = {
                20: "twen",
                30: "thir",
                40: "for",
                50: "fif",
                80: "eigh"
            }

            part_1 = number // 100
            decimal = number % 100

            if decimal < 10:
                part_2 = numerals[decimal]
            elif 10 <= decimal < 20:
                part_2 = decimals[decimal]
            else:
                part_2 = f"{rounds.get(decimal - decimal % 10, numerals[(decimal - decimal % 10) // 10])}ty {numerals[decimal % 10]}"

            name = string.format(hundreds[part_1], part_2).strip()
        else:
            name = "zero"
        if name not in transition:
            transition[name] = number
        return name

    transition = {}

    strings = quickSort(list(map(int_to_string, arr)))

    return [transition[number] for number in strings]


if __name__ == '__main__':
    array = list(map(int, sys.stdin.read().strip().split(", ")))
    print(sort_by_name(array))
