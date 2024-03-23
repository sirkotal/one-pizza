from collections import deque
import pizza

def generate_neighbors(current_solution): # steepest ascent, BFS -> TODO
    neighbors = []
    for child in current_solution.children:      
        neighbors.append(child)

    return neighbors
    
def eval_function(solution): # TODO
    return sum(solution)
    
# x0 is the initial solution
def hill_climbing(f, x0):
    x = x0
    while True:
        neighbors = generate_neighbors(x)  # generate current solution neighbors
        best_neighbor = max(neighbors, key=f) # find neighbor with highest fitness value
        if f(best_neighbor) <= f(x):  # if the best neighbor is not better than the current solution, stop
            return x
        x = best_neighbor  # otherwise, continue with the best neighbor