import itertools
with open('input.txt', 'r') as INPUT:
    min_length = 999999
    way = {}
    locations = []

    for i in range(28):
        our_input = INPUT.readline()
        array = our_input.split()
        first_place = array[0]
        second_place = array[2]
        road = int(array[4])
        way[first_place + second_place] = road
        way[second_place + first_place] = road
        locations.append(first_place)
        locations.append(second_place)
    locations = set(locations)

    for i in itertools.permutations(locations):
        length = 0
        for first_city, second_city in zip(i[:-1], i[1:]):
            length += way[first_city + second_city]
        if length < min_length:
            min_length = length

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(min_length))