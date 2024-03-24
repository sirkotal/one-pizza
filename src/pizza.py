import random

class Pizza:
    def __init__(self, customers, ingredients):
        self.customers = customers
        self.ingredients = ingredients
        self.solution = set()
        self.score = 0

def eval_function(pizza): 
    pizza.score = 0
    for client in pizza.customers:
        if ((client.likes & pizza.solution) == client.likes) and ((client.dislikes & pizza.solution) == set()):
            pizza.score += 1
    return pizza.score

def generate_neighbors(pizza): # steepest ascent, BFS -> TODO
    neighbors = []
    
    return neighbors
    
# x0 is the initial solution
def hill_climbing(f, x0):
    x = x0

    p1 = Pizza(x0.customers, x0.ingredients)
    p2 = Pizza(x0.customers, x0.ingredients)

    p1.solution = {'peppers', 'mushrooms', 'pineapple', 'tomatoes', 'basil'}
    p2.solution = {'peppers', 'cheese', 'mushrooms', 'tomatoes'}
    while True:
        # neighbors = generate_neighbors(x)  # generate current solution neighbors
        neighbors = [p1, p2]
        best_neighbor = max(neighbors, key=f) # find neighbor with highest fitness value
        if f(best_neighbor) <= f(x):  # if the best neighbor is not better than the current solution, stop
            print("P0 Score:", x0.score)
            print("P1 Score:", p1.score)
            print("P2 Score:", p2.score)
            return x
        x = best_neighbor  # otherwise, continue with the best neighbor
