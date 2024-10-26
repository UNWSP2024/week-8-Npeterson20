# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).


import random

# Dictionary of states and capitals
states_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "New York": "Albany",
    "Florida": "Tallahassee",
    "Illinois": "Springfield",
}

def quiz():
    correct = 0
    incorrect = 0
    for state in random.sample(list(states_capitals.keys()), len(states_capitals)):
        capital = input(f"What is the capital of {state}? ")
        if capital.lower() == states_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The capital of {state} is {states_capitals[state]}.")
            incorrect += 1
    print(f"\nResults: {correct} correct, {incorrect} incorrect.")

# Start the quiz
quiz()
