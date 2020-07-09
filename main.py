from heapq import heappush, heappop
from math import hypot
from time import time
from itertools import permutations
import sys

from heuristic import *
mode = 0


def read_file(filename):
    with open(filename) as f:
        cities = []
        for line in f:
            tup = tuple(map(int, line.split()))
            cities.append(tup)
    return cities


def generate_childs(parent, cities_quantity, roads):
    '''Dla stanu parent zwraca liste wszystkich mozliwych potomnych stanow. Wywoluje odpowiednia heurystyke'''
    current_path = parent[1]
    current_path_distance = parent[2]
    # zbior liczb porzadkowych wszystkich miast potrzebny do operacji na zbiorach
    cities_id_set = set([i for i in range(cities_quantity)])

    childs = []
    if len(current_path) != cities_quantity:  # jesli nie jest to koncowy etap
        non_visited_cities = cities_id_set.difference(set(current_path))
        for next_city in non_visited_cities:
            child_path_distance = current_path_distance + roads[current_path[-1]][next_city]
            if mode == 0 or mode == 3:
                child_priority = child_path_distance + heuristic(non_visited_cities.difference({next_city}), next_city,
                                                                 roads, mode)
            else: #mode = 1
                child_priority = child_path_distance
            child_path = current_path + [next_city]

            childs.append((child_priority, child_path, child_path_distance))
    else:  # w przeciwnym razie wystarczy wrocic do pierwszego miasta
        childs.append((current_path_distance + roads[current_path[-1]][0], current_path + [0], 0))
    return childs


def traveling_salesman_problem_a_star(roads):
    """Dla grafu rozwiazuje problem komiwojazera algorytmem A* korzystajac z funkcji pomocniczej generate_childs"""
    cities_quantity = len(roads)

    states = []  # states to lista, ktora bedzie kolejka priorytetowa oparta na kopcu
    heappush(states, (0, [0], 0))  # do kolejki wrzuc sciezke zlozona tylko z pierwszego miasta z priorytetem 0
    while len(states[0][1]) != cities_quantity + 1:  # dopoki na pierwszej pozycji nie znalazl sie stan terminalny
        parent_state = heappop(states)
        childs = generate_childs(parent_state, cities_quantity, roads)
        for child in childs:  # dodaj do kolejki wszystkich potomkow rozwijanego stanu z odpowiednim priorytetem
            heappush(states, child)
    return states[0]


def traveling_salesman_problem_brute_force(roads):
    """Dla grafu rozwiazuje problem komiwojazera metoda brute force"""
    all_possible_routes = list(
        permutations(range(1, len(roads))))  # droga zawsze zaczyna i konczy sie w miescie pierwszym
    all_possible_routes = all_possible_routes[
                          :int(len(all_possible_routes) / 2)]  # usuwanie reverse duplicate (drugiej polowy permutacji)

    best_route_distance = float("inf")
    best_route = []
    for route in all_possible_routes:
        route_distance = roads[0][route[0]]
        for i in range(len(route) - 1):
            route_distance += roads[route[i]][route[i + 1]]
        route_distance += roads[0][route[-1]]
        if route_distance < best_route_distance:
            best_route_distance = route_distance
            best_route = [0] + list(route) + [0]

    return best_route_distance, best_route


def traveling_salesman_problem(cities):
    """Dla listy miast (par (x, y)) generuje graf (lista 2D) i przekazuje go do funkcji wybranego algorytmu"""
    cities_quantity = len(cities)

    # lista 2D roads przechowuje wartosc kazdej drogi z kazdego miasta do kazdego miasta
    roads = [[0 for _ in range(cities_quantity)] for _ in range(cities_quantity)]
    for row in range(cities_quantity):
        for col in range(cities_quantity):
            if row == col:
                continue
            roads[row][col] = hypot(cities[row][0] - cities[col][0], cities[row][1] - cities[col][1])
    # dzieki temu np roads[0][4] (i roads[4][0]) daja w prosty sposob wartosc odleglosci od miasta pierwszego do piatego

    if mode == 2:
        return traveling_salesman_problem_brute_force(roads)
    else:
        return traveling_salesman_problem_a_star(roads)


def menu():
    global mode
    mode = input("0 - A star\n"
                 "1 - Pierwszy najtanszy\n"
                 "2 - Brute force\n"
                 "3 - A star (alternatywna heurystyka)\n"
                 "Podaj swoj wybor: ")
    try:
        val = int(mode)
    except ValueError:
        try:
            val = float(mode)
            print("Wprowadzono niepoprawne dane.", val)
            sys.exit(-1)
        except ValueError:
            print("Wprowadzono niepoprawne dane.")
            sys.exit(-1)

    mode = int(mode)
    if not (mode == 0 or mode == 1 or mode == 2 or mode == 3):
        print("Wprowadzono niepoprawny numer.")
        sys.exit(-2)
    else:
        start_time = time()

        solution = traveling_salesman_problem(read_file('data.txt'))
        print("Koszt: ", solution[0])
        print("Droga: ", solution[1])
        print("--- %s sekund ---" % (time() - start_time))

    # mode=0 heurystyka
    # mode=1 pierwszy najtanszy
    # mode=2 brute force
    # mode=3 a* alternatywna heurystyka


menu()
