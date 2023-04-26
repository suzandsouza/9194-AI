from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

def isValid(state):
    # check if the state is valid
    m1, c1, b, m2, c2 = state
    return m1 >= 0 and c1 >= 0 and m2 >= 0 and c2 >= 0 \
        and (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2)

def isGoal(state):
    # check if the state is the goal state
    m1, c1, b, m2, c2 = state
    return m1 == 0 and c1 == 0 and b == 0

def expand(node):
    # generate next possible states
    m1, c1, b, m2, c2 = node.state
    nextStates = []
    for m, c, cost in [[1, 0, 1], [2, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1]]:
        if b == 1:
            newState = [m1 - m, c1 - c, 0, m2 + m, c2 + c]
        else:
            newState = [m1 + m, c1 + c, 1, m2 - m, c2 - c]
        if isValid(newState):
            nextStates.append(Node(newState, node, node.depth + 1, node.cost + cost))
    return nextStates

def ucs(initialState):
    # uniform cost search
    frontier = PriorityQueue()
    frontier.put(Node(initialState))
    explored = set()
    while not frontier.empty():
        node = frontier.get()
        if isGoal(node.state):
            path = []
            while node is not None:
                path.append(node.state)
                node = node.parent
            return path[::-1]
        explored.add(tuple(node.state))
        for child in expand(node):
            if tuple(child.state) not in explored:
                frontier.put(child)

# test the code with the initial state [3, 3, 1, 0, 0]
path = ucs([3, 3, 1, 0, 0])
for state in path:
    print(state)
