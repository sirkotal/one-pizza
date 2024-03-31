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
    pizza = parse_input(os.path.join(os.path.dirname(__file__), '../input/a_an_example.in.txt'))
    # pizza = parse_input(os.path.join(os.path.dirname(__file__), '../input/b_basic.in.txt'))
    # pizza = parse_input(os.path.join(os.path.dirname(__file__), '../input/c_coarse.in.txt'))

    # Hill Climbing Testing
    # hill_climbing(pizza)
    # print(pizza.get_solution())
    # print(pizza.score)
    
    # Simulated Annealing Testing
    # simulated_annealing(pizza)
    # print(pizza.get_solution())
    # print(pizza.score)

    # Genetic Algorithm Testing
    # genetic_algorithm(pizza)
    # print(f"Best solution found: {pizza.get_solution()} ({pizza.score})")

    # Tabu Search Testing
    tabu_search(pizza)
    print("Tabu Search Result:")
    print(f"Ingredients: {pizza.get_solution()}")
    print(f"Score: {pizza.score}")
