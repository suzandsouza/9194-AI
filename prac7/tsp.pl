% Define the cities and their distances
distance(a, b, 10).
distance(a, c, 15).
distance(a, d, 20).
distance(b, c, 35).
distance(b, d, 25).
distance(c, d, 30).

% Define the predicate to calculate the total distance of a given route
total_distance([], 0).
total_distance([_], 0).
total_distance([City1, City2|Cities], TotalDist) :-
    distance(City1, City2, Dist),
    total_distance([City2|Cities], RestDist),
    TotalDist is Dist + RestDist.

% Define the main predicate to find the shortest route
tsp(StartCity, ShortestRoute, ShortestDist) :-
    findall(Route, permutation([a,b,c,d], Route), Routes),
    member(ShortestRoute, Routes),
    total_distance([StartCity|ShortestRoute], ShortestDist),
    \+ (member(Route, Routes),
        total_distance([StartCity|Route], Dist),
        Dist < ShortestDist).
