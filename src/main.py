from customer import Customer
from pizza import *

import os

def parse_input(input_file):
    clients = []
    ingredients = set()

    with open(input_file, 'r') as file:
        num_clients = int(file.readline())
        for _ in range(num_clients):
            line = file.readline().split()
            num_liked = int(line[0])
            assert num_liked == len(line[1:])
            liked = set(line[1:])
            ingredients.update(liked)

            line = file.readline().split()
            num_disliked = int(line[0])
            assert num_disliked == len(line[1:])
            disliked = set(line[1:])
            ingredients.update(disliked)
            clients.append(Customer(liked, disliked))
    
    return Pizza(clients, list(ingredients))

if __name__ == '__main__':
    piz = parse_input(os.path.join(os.path.dirname(__file__), '../input/a_an_example.in.txt'))

    # Hill Climbing Testing
    # result = hill_climbing(eval_function, piz)
    # print(result.get_solution())
    # print(result.score)
    
    # Simulated Annealing Testing
    # annealing = simulated_annealing(eval_function, piz)
    # print(annealing.get_solution())
    # print(annealing.score)

    # Genetic Algorithm Testing
    # something = get_neightbors(piz)
    # best_solution = genetic_algorithm(something, 100, 0.01, "roulette", 4)  
    # print(f"Best solution found: {best_solution.get_solution()} ({best_solution.score})")

    # Tabu Search Testing
    # tabu_result = tabu_search(piz, eval_function, 1000, 10)
    # print("Tabu Search Result:")
    # print(f"Ingredients: {tabu_result.get_solution()}")
    # print(f"Score: {tabu_result.score}")
