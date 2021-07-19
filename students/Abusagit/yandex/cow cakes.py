import sys


def get_most_valuable_place(participants):
    places = set()
    winners = set()
    max_ = max(participants)
    possible_places = {}
    sorted_list = sorted(participants, reverse=True)
    for place, distance in enumerate(sorted_list, start=1):
        if distance % 10 == 5:
            if distance not in possible_places:
                possible_places[distance] = place
    # print(possible_places)
    # print(sorted_list)
    for index, distance in enumerate(participants):
        if distance == max_:
            winners.add(index)
        if all((distance % 10 == 5, index + 1 < len(participants), any((i < index for i in winners)))):
            if participants[index + 1] < distance:
                places.add(possible_places[distance])
    # print(sorted_list, possible_places, places, sep='\n')
    # print(places)
    return 0 if not places else min(places)


n, *particips = map(int, sys.stdin.read().strip().split())
print(get_most_valuable_place(particips))
