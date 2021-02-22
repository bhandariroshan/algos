import math
import heapq


class Node:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        
    def __eq__(self, another):
        # make the node comparable with another node
        return self.cost == another.cost
    
    def __lt__(self, another):
        # make the node comparable with another node
        return self.cost < another.cost
    
    def __gt__(self, another):
        # make the node comparable with another node
        return self.cost > another.cost
    
def euclidean_distance(x1, y1, x2, y2):
    # calculate the euclidean distance
    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return dist

def shortest_path(M,start,goal):
    print("shortest path called, implementation of A* algorithm")
    
    # define frontier as a heap
    frontier = [Node(start, 0)]
    heapq.heapify(frontier)
    
    # keep track of travelled nodes and their cost
    cost = {start: 0}
    
    # keep track of previous nodes for each node
    previous = {start: None}
    
    while len(frontier) > 0:
        # get the top of the min heap
        current_node = heapq.heappop(frontier)
        current = current_node.value
        
        if current == goal:
            break
        
        # get all the neighbor
        neighbors = M.roads[current]
        
        # do for all the neighbors, calculate f value and add to the heap
        for each_neighbor in neighbors:
            # get the coordinates
            start_coordinate = M.intersections[current]
            end_coordinate = M.intersections[each_neighbor]
            goal_coordinate = M.intersections[goal]
            
            # calculate the g value which is distance from the original start
            g = cost[current] + euclidean_distance(
                start_coordinate[0], start_coordinate[1], 
                end_coordinate[0], end_coordinate[1]
            )
            
            if each_neighbor not in cost or g < cost[each_neighbor]:
                # update the cost dictionary
                cost[each_neighbor] = g
                
                # update f with heuristics, which is distance from the neighbor to goal
                h = euclidean_distance(
                    end_coordinate[0], end_coordinate[1], 
                    goal_coordinate[0], goal_coordinate[1]
                )
                
                # calculate the f value
                f = g + h
                
                # add the neighbor to the frontier heap
                heapq.heappush(frontier, Node(each_neighbor, f))
                
                # update the previous dictionary
                previous[each_neighbor] = current_node.value
    
    # backtrack from goal using previous dict to get the path from start to goal
    path = []
    node = goal
    while node != start:
        path = [node] + path
        node = previous[node]
    path = [node] + path

    return path

#Reference: http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html