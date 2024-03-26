import random
import utils

class Pizza:
    def __init__(self, customers, ingredients):
        self.customers = customers
        self.ingredients = ingredients
        self.solution = 0
        self.score = 0

    def get_solution(self):
        """
        Returns a set of ingredints that are in the solution
        TODO: Check if a list is more appropriate
        """
        return {self.ingredients[i] for i in range(len(self.ingredients)) if self.solution & (1 << i)}
        

def eval_function(pizza): 
    pizza.score = 0
    for client in pizza.customers:
        # TODO: find a more efficient way to evaluate the solution without generating the set
        if ((client.likes & pizza.get_solution()) == client.likes) and ((client.dislikes & pizza.get_solution()) == set()):
            pizza.score += 1
    return pizza.score

def generate_neighbors(pizza): # TODO
    neighbors = []
    
    return neighbors
    
# x0 is the initial solution
def hill_climbing(f, x0):
    x = x0

    p1 = Pizza(x0.customers, x0.ingredients)
    p2 = Pizza(x0.customers, x0.ingredients)

    # Hardcoded solutions for testing (a_an_example.in.txt)
    # ['basil', 'cheese', 'mushrooms', 'peppers', 'pineapple', 'tomatoes']
    p1.solution = int('101111', 2) # ['basil', 'mushrooms', 'peppers', 'pineapple', 'tomatoes']
    p2.solution = int('011101', 2) # ['cheese', 'mushrooms', 'peppers', 'tomatoes']
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
