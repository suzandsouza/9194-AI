% Define the size of the world and the starting position of the agent.
world_size(4).
start_position(1,1).

% Define the location of the pits, the Wumpus, and the gold.
% 0 represents an empty cell, p represents a pit, w represents the Wumpus, and g represents the gold.
location(1,3,p).
location(2,2,p).
location(2,3,w).
location(3,4,p).
location(4,2,p).
location(4,4,g).

% Define the rules for moving the agent around the world.
% The agent can move up, down, left, or right.
move(up, X, Y, X, Y1) :-
    Y > 1,
    Y1 is Y - 1.
move(down, X, Y, X, Y1) :-
    world_size(N),
    Y < N,
    Y1 is Y + 1.
move(left, X, Y, X1, Y) :-
    X > 1,
    X1 is X - 1.
move(right, X, Y, X1, Y) :-
    world_size(N),
    X < N,
    X1 is X + 1.

% Define the rules for detecting hazards and the gold.
% If the agent is in a cell with a pit or the Wumpus, it dies.
% If the agent is in a cell with the gold, it collects it and wins.
detect_hazard(X, Y) :-
    location(X, Y, p),
    write('You fell into a pit and died.').
detect_hazard(X, Y) :-
    location(X, Y, w),
    write('You were eaten by the Wumpus and died.').
detect_gold(X, Y) :-
    location(X, Y, g),
    write('You found the gold and won!').

% Define the main game loop.
% The agent starts at the starting position and can move around the world until it either dies or wins.
play(X, Y) :-
    detect_hazard(X, Y),
    !.
play(X, Y) :-
    detect_gold(X, Y),
    !.
play(X, Y) :-
    write('You are at position ('),
    write(X),
    write(','),
    write(Y),
    write(').'),
    nl,
    write('Which direction do you want to move? (up, down, left, or right)'),
    nl,
    read(Direction),
    move(Direction, X, Y, X1, Y1),
    play(X1, Y1).
    
% Start the game at the starting position.
start :-
    start_position(X, Y),
    play(X, Y).
