from customer import Customer
from pizza import *

import os

# TODO: Make customer likes and dislikes a bitstring
# would be easier to evaluate the solution
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

def display_menu():
    print("------------- OnePizza -------------")
    print("")
    print("Welcome to OnePizza!")
    print("")
    print("Please choose an optimization algorithm to proceed:")
    print("")
    print("1. Hill Climbing")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm")
    print("4. Tabu Search")
    print("")
    print("If you would like to get to know more about OnePizza, press 5.")
    print("")
    print("6. Exit")
    print("")
    choice = input("Enter your choice (1-6): ")
    return choice

def main():
    piz = parse_input(os.path.join(os.path.dirname(__file__), '../input/a_an_example.in.txt'))

    while True:
        user_choice = display_menu()
        print("")
        if user_choice == '1':
            # Hill Climbing
            result = hill_climbing(eval_function, piz)
            print(f"Ingredients: {result.get_solution()}\nScore: {result.score}")
        elif user_choice == '2':
            # Simulated Annealing
            annealing = simulated_annealing(eval_function, piz)
            print(f"Ingredients: {annealing.get_solution()}\nScore: {annealing.score}")
        elif user_choice == '3':
            # Genetic Algorithm
            neighbors = get_neightbors(piz)
            best_solution = genetic_algorithm(neighbors, 100, 0.01, "roulette", 4)
            print(f"Best solution found: {best_solution.get_solution()} ({best_solution.score})")
        elif user_choice == '4':
            # Tabu Search
            tabu_result = tabu_search(piz, eval_function, 1000, 10)
            print(f"Ingredients: {tabu_result.get_solution()}\nScore: {tabu_result.score}")
        elif user_choice == '5':
            # OnePizza explanation
            print("")
            print("------------------------------------------------------------------------------------------------------------")
            print("")
            print("We are opening a small pizzeria that sells only one pizza option to their customers.")
            print("So, in order to maximize customers, we need to decide which ingredients our pizza contains.")
            print("Every customer has liked and disliked ingredients.")
            print("It is our job to maximize sales by including the ingredients customers like and leave out the disliked ones.")
            print("Our pizza scores differently based on how many clients come to our shop!")
            print("Come see which pizza maximizes the customers we get!")
            print("")
            print("------------------------------------------------------------------------------------------------------------")
        elif user_choice == '6':
            print("Exiting program.")
            break
        else:
            print("")
            print("Invalid choice, please try again.")

        print("")
        input("Press any key to return...")

if __name__ == '__main__':
    main()