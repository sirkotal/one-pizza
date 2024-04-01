from customer import Customer
from pizza import *

import os
import time

def parse_input(input_file):
    """
    Parses the contents of a specific file

    Args:
        input_file: The file to be parsed
        
    Returns a Pizza object containing two lists: one for clients and another for ingredients
    """
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

def display_menu(log):
    print("---------------------------- OnePizza ----------------------------")
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
    print("5. Learn more about OnePizza")
    print("")
    print("6. Enable logging" if not log else "6. Disable logging")
    print("")
    print("7. Exit")
    print("")

    choice = input("Enter your choice (1-7): ")
    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        raise ValueError("Invalid choice")

    return choice

def choose_input_file():
    print("Please select the input file:")
    print("1. Example (Simplest)")
    print("2. Basic")
    print("3. Coarse")
    print("4. Difficult")
    print("5. Elaborate (Most Complex)")
    file_choice = input("Enter your choice (1-5): ")

    files = {
        '1': 'a_an_example.in.txt',
        '2': 'b_basic.in.txt',
        '3': 'c_coarse.in.txt',
        '4': 'd_difficult.in.txt',
        '5': 'e_elaborate.in.txt',
    }

    chosen_file = files.get(file_choice, 'a_an_example.in.txt') # by default
    return os.path.join(os.path.dirname(__file__), f'../input/{chosen_file}')

def get_max_iterations():
    print("Please enter the maximum number of iterations (default -> 1000): ", end="")
    choice = input()
    print()
    return int(choice) if choice else 1000

def get_initial_temperature():
    print("Please enter the initial temperature (default -> 1000): ", end="")
    choice = input()
    print()
    return float(choice) if choice else 1000.0

def get_num_generations():
    print("Please enter the number of generations (default -> 100): ", end="")
    choice = input()
    print()
    return int(choice) if choice else 100

def get_mutation_rate():
    print("Please enter the mutation rate (default -> 0.1): ", end="")
    choice = input()
    print()
    return float(choice) if choice else 0.01

def get_selection_method():
    print("Available selection methods: tournament, roulette")
    print("Please enter the selection method (default -> roulette): ", end="")

    choice = input()
    if choice not in ['tournament', 'roulette', '']:
        raise ValueError("Invalid selection method")

    print()
    return choice if choice else 'roulette'

def get_tournament_size():
    print("Please enter the tournament size (default -> 4): ", end="")
    choice = input()
    print()
    return int(choice) if choice else 4

def get_tabu_size():
    print("Please enter the tabu list size (default -> 10): ", end="")
    choice = input()
    print()
    return int(choice) if choice else 10

def get_neighborhood_size():
    print("Please enter the neighborhood size (default -> 10): ", end="")
    choice = input()
    print()
    return int(choice) if choice else 10

def main():
    log = False

    while True:
        user_choice = display_menu(log)
        print("")
        if user_choice == '1': # Hill Climbing
            input_file_path = choose_input_file()
            pizza = parse_input(input_file_path)

            max_iterations = get_max_iterations()

            start_time = time.time()
            hill_climbing(pizza, max_iterations=max_iterations, log=log)
            end_time = time.time()
            print(f"Ingredients: {pizza.get_solution()}\nScore: {pizza.score}")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
        elif user_choice == '2': # Simulated Annealing
            input_file_path = choose_input_file()
            pizza = parse_input(input_file_path)

            max_iterations = get_max_iterations()
            initial_temperature = get_initial_temperature()

            start_time = time.time()
            simulated_annealing(pizza, max_iterations=max_iterations, temperature=initial_temperature, log=log)
            end_time = time.time()
            print(f"Ingredients: {pizza.get_solution()}\nScore: {pizza.score}")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
        elif user_choice == '3': # Genetic Algorithm
            input_file_path = choose_input_file()
            pizza = parse_input(input_file_path)

            num_generations = get_num_generations()
            mutation_rate = get_mutation_rate()
            selection_method = get_selection_method()
            tournament_size = 4
            if selection_method == 'tournament':
                tournament_size = get_tournament_size()

            start_time = time.time()
            genetic_algorithm(pizza, num_generations=num_generations, mutation_rate=mutation_rate, selection_method=selection_method, tournament_size=tournament_size, log=log)
            end_time = time.time()
            print(f"Ingredients: {pizza.get_solution()}\nScore: {pizza.score}")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
        elif user_choice == '4': # Tabu Search
            input_file_path = choose_input_file()
            pizza = parse_input(input_file_path)

            max_iterations = get_max_iterations()
            tabu_size = get_tabu_size()
            neighborhood_size = get_neighborhood_size()

            start_time = time.time()
            tabu_search(pizza, max_iterations=max_iterations, tabu_size=tabu_size, neighborhood_size=neighborhood_size, log=log)
            end_time = time.time()
            print(f"Ingredients: {pizza.get_solution()}\nScore: {pizza.score}")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
        elif user_choice == '5':
            # OnePizza explanation
            print("")
            print("------------------------------------------------------------------------------------------------------------")
            print("")
            print("We are opening a small pizzeria that sells only one pizza option to their customers.")
            print("Therefore, in order to maximize the amount of satisfied customers, we need to decide which ingredients our pizza contains.")
            print("Every customer has a set of liked and disliked ingredients.")
            print("It is our job to maximize sales by including the ingredients customers like and leave out the disliked ones.")
            print("Our pizza scores differently based on how many clients come to our shop!")
            print("Come see which pizza scores the best with our customers!")
            print("")
            print("------------------------------------------------------------------------------------------------------------")
        elif user_choice == '6':
            log = not log
            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif user_choice == '7':
            print("Exiting program.")
            break
        else:
            print("")
            print("Invalid choice, please try again.")

        print("")
        input("Press any key to return...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
