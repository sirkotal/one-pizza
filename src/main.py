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
    
    return Pizza(clients, sorted(list(ingredients)))

if __name__ == '__main__':
    piz = parse_input(os.path.join(os.path.dirname(__file__), '../input/a_an_example.in.txt'))
    # clients, ingredients = parse_input('../input/c_coarse.in.txt')
    # print(piz.customers)
    # print(piz.ingredients)
    # print(len(piz.ingredients))

    # good = set()
    # bad = set()

    # for client in piz.customers:
    #     good.update(client.likes)
    #     bad.update(client.dislikes)
    
    # good.difference_update(bad)

    # print(good)
    # print(bad)

    piz.solution = int('111111', 2)
    result = hill_climbing(eval_function, piz)
    print(result.get_solution())
    print(result.score)
