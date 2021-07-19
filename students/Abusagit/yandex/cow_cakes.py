import sys


def get_place(particips):
    winners = set()

    max_ = max(particips)
    possible_places = {}
    for index, value in enumerate(sorted(particips, reverse=True), start=1):
        if all((value % 5 == 0, value not in possible_places)):
            possible_places[value] = index
        if value == max_:
            winners.add(index)
    print(sorted(particips, reverse=False))
    print(possible_places)
    places = set()
    for index, value in enumerate(particips):
        if value % 5 == 0 and index + 1 < len(particips):
            if all((
                    any((i < index for i in winners)),  # index > index of the winner,
                    value > particips[index + 1]
            )):
                places.add(possible_places[value])

    return 0 if not places else max(places)


n, *participants = map(int, sys.stdin.read().strip().split())
print(get_place(participants))

