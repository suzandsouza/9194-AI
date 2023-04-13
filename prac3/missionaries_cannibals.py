import math

class State():
    def __init__(self,cannibalLeft, missionaryLeft, boat, cannibalRigth, missionaryRight):
        self.cannibalLeft=cannibalLeft
        self.missionaryLeft=missionaryLeft
        self.boat=boat
        self.cannibalRight=cannibalRigth
        self.missionaryRight=missionaryRight
        self.parent=None    #parent is used for BFS Graph traversal

        #intialize completed
    #function to check if my goal state is already reached
    def is_goal(self):
        if self.cannibalLeft==0 and self.missionaryLeft==0:
            return True
        else:
            return False
    
    #making a note of all the valid & invalid cases
    def is_valid(self):
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
                   return True
        else:
            return False
            
    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight
    
    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))


def successors(cur_state):
	children = []

	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		## Two missionaries cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state) #since the state is valid append it into the list
        #update the new state by passing within the class state 
        #remove 2 cannibals from the left, add 2 cannibals to the right
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		
        ## Two cannibals cross left to right.

		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def my_breadth_first_search():
    initial_state=State(3,3,'left',0,0) #on the left
    if initial_state.is_goal():
        return initial_state
    
    # use a list named as frontier, set named as explored
    frontier=list()
    explored=set()
    frontier.append(initial_state)
    while frontier:
        state=frontier.pop(0)
        if state.is_goal():
            return state 
        # after exploring we add it to the set
        explored.add(state)
        children=successors(state)
        for child in children:
            if(child not in explored):
                frontier.append(child)
    return None 

def print_solution(solution):
    path=[]
    path.append(solution)
    parent=solution.parent
    while parent:
        path.append(parent)
        parent=parent.parent
    for t in range(len(path)):
        state=path[len(path)-t-1]
        print("\n["+str(state.cannibalLeft)+",\t"+str(state.missionaryLeft)+",\t"+str(state.boat)+",\t"+str(state.cannibalRight)+",\t"+str(state.cannibalRight)+"]")

def main():
    solution=my_breadth_first_search()
    print("------ Exp 3 Missionaries and cannibals ------")
    print("\nOrder is as follows, \n(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
    print_solution(solution)

if __name__=="__main__":
    main()

