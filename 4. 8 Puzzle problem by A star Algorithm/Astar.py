import heapq
class Node:
    pass
class Graph:
    pass

# function for heuristics calcs
def heuristic(node,goal):
    return abs(ord(node.name)-ord(goal.name))

def astar(start_n,goal_n,h_func):
    open_list=[(0,start_n)]
    came_from={}
    g_scores={start_n:0}    #dictionary having start_node value as 0
    f_scores={start_n:h_func(start_n,goal_n)}

    while open_list:
        _,current=heapq.heapify(open_list)  #we create a heap ds named as current from a list called as open_list
        #why heap? becuase finding the min & max elem t.c is O(1)
        if current==goal_n:
            path=[current]
            while current in came_from:
                current=came_from[current]
                path.append(current)
            return list(reversed(path))
        
        for neighbor, cost in current.edges.items():
            tentative_g_score=g_scores[current]+cost

            if neighbor not in g_scores or tentative_g_score<g_scores[neighbor]:
                came_from[neighbor]=current
                g_scores[neighbor]=tentative_g_score
                f_scores[neighbor]=tentative_g_score+h_func(neighbor,goal_n)
                heapq.heappush(open_list,(f_scores[neighbor],neighbor)) 
graph=Graph()
