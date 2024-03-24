from customer import Customer
import pizza

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
            ingredients.update(line[1:])

            line = file.readline().split()
            num_disliked = int(line[0])
            assert num_disliked == len(line[1:])
            disliked = set(line[1:])
            ingredients.update(line[1:])
            clients.append(Customer(liked, disliked))
    
    p = pizza.Pizza(clients, ingredients)

    return p

if __name__ == '__main__':
    piz = parse_input('input/a_an_example.in.txt')
    # clients, ingredients = parse_input('../input/c_coarse.in.txt')
    # print(piz.customers)
    # print(piz.ingredients)
    # print(len(piz.ingredients))

    good = set()
    bad = set()

    for client in piz.customers:
        good.update(client.likes)
        bad.update(client.dislikes)
    
    good.difference_update(bad)

    # print(good)
    # print(bad)

    piz.solution = {'peppers', 'cheese', 'mushrooms', 'pineapple', 'tomatoes', 'basil'}
    print(pizza.hill_climbing(pizza.eval_function, piz).solution)
    print(pizza.hill_climbing(pizza.eval_function, piz).score)
