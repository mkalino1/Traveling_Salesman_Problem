from functools import lru_cache


def heuristic(non_visited_cities, current_city_index, roads, mode):
    if non_visited_cities:  # jesli zbior ten nie jest pusty to jest sens liczyc heurystyke
        if mode == 0:
            val = minimal_spanning_tree(non_visited_cities, roads)
        else: #mode = 3
            val = alternative_heuristic(non_visited_cities, roads)
        val += min([roads[current_city_index][i] for i in
                    non_visited_cities])  # odleglosc od aktualnego do najblizszego z setu
        val += min([roads[0][i] for i in
                    non_visited_cities])  # odleglosc od startowego do najblizszego z setu
    else:  # jesli wszystkie miasta sa juz odwiedzone to pozostala droge "szacujemy" przez powrot do miasta startowego
        val = roads[current_city_index][0]

    return val


def minimal_spanning_tree(non_visited_cities, roads):
    @lru_cache  # least recently used cache dla optymalizacji
    def minimal_spanning_tree_body(non_visited_cities):

        global min_val_vertex
        inner_roads = []
        for i in range(len(roads)):
            if i in non_visited_cities:
                inner_roads.append(
                    [roads[i][j] for j in range(len(roads)) if j in non_visited_cities])  # zmniejszamy tablice roads tylko do miast z non_visited_cities

        vertices_nr = len(inner_roads)
        if vertices_nr == 0 or vertices_nr == 1:
            return 0

        key = []
        parent_nodes = []  # lista do przechowywania poprzedników wierzcholkow w drzewie
        included_vert = []  # zbior wierzchołków w MST

        for i in range(vertices_nr): #tworzenie list
            parent_nodes.append(None)
            included_vert.append(False)
            key.append(float("inf"))

        key[0] = 0  # od wierzcholka nr 0 zaczynamy, reszta == nieskonczonoosc

        for i in range(vertices_nr):

            min_val = float("inf")
            for i in range(vertices_nr):    #szukanie klucza o min wartosci
                if included_vert[i] == False and key[i] < min_val:
                    min_val = key[i]
                    min_val_vertex = i

            u = min_val_vertex
            included_vert[u] = True

            for v in range(vertices_nr):
                if 0 < inner_roads[u][v] < key[v] and included_vert[v] == False:
                    key[v] = inner_roads[u][v]
                    parent_nodes[v] = u

        val = 0  # zmienna do sumowania wag
        for i in range(1, vertices_nr):
            par = parent_nodes[i]
            val += inner_roads[i][par]  # sumujemy wagi wyznaczonego grafu
        return val

    return minimal_spanning_tree_body(frozenset(non_visited_cities))


def alternative_heuristic(non_visited_cities, roads):
    inner_roads = []
    for i in range(len(roads)):
        if i in non_visited_cities:
            inner_roads.append(
                [roads[i][j] for j in range(len(roads)) if j in non_visited_cities]) # zmniejszamy tablice roads tylko do miast z non_visited_cities

    table = []
    for i in range(len(inner_roads)):
        for j in range(len(inner_roads)):
            table.append(inner_roads[i][j])
    table.sort()
    val = 0
    if len(table) == 0:
        return 0
    for i in range(len(inner_roads) - 1): #sumujemy N-1 najkrotszych odleglosci z inner_roads, gdzie N to liczba miast nieodwiedzonych
        val += table[i]
    return val
