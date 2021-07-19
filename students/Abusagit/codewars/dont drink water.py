from functools import reduce


def separate_liquids(glass):
    density_chart = {
        'H': 1.36,
        'W': 1.00,
        'A': 0.87,
        'O': 0.8
    }
    height = len(glass)
    width = len(glass[0])
    overall = height * width
    new_arr = reduce(lambda x, y: x + y, glass, [])  # x.extend returns None so it doesn`t work

    for bypass in range(1, overall):
        for i in range(overall - bypass):
            if density_chart[new_arr[i]] > density_chart[new_arr[i + 1]]:
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
    return [[new_arr[w + width * h] for w in range(width)] for h in range(height)]


    print(new_arr)
if __name__ == '__main__':
    example = [
        ['H', 'H', 'W', 'O'],
        ['W', 'W', 'O', 'W'],
        ['H', 'H', 'O', 'O'],
    ]
    print(separate_liquids(example))