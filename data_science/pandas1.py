import pandas as pd
import numpy as np
from .kwutils import *

import os

DATA_FILES_DIR = os.path.join(os.path.dirname(__file__),"FSM")

def df_test():

    a1 = np.array([["a1","a2","a3"], ["b1","b2","b3"]])

    df1 = pd.DataFrame(a1)
    print(df1.info())
    print(df1.head(3))

    file_name = os.path.join(DATA_FILES_DIR, "default_floor_objects.csv")
    objs = pd.read_csv(file_name, index_col=0)

    print(objs.dtypes)
    print(objs.head(4))
    print(objs.info())
    print(f'shape={objs.shape}')

    objs_filtered = objs[(objs["solid"] == True) & (objs["interactable"] == True) & (objs["collectable"] == True)]
    print(objs_filtered.head(4))

    objs.plot.hist(x="Name", y="width")


def df_test2():

    """ Use state transition data files and navigate them with pandas"""
    title = "Welcome to the finite state machine game!".title()
    print("*" * (len(title) + 5))
    print("* " + title + " *")
    print("*" * (len(title) + 4))

    x= input

    # Load in the states into a data frame
    file_name = os.path.join(DATA_FILES_DIR, "states.csv")
    states = pd.read_csv(file_name, index_col="ID")

    # Load in the state transitions into a data frame
    file_name = os.path.join(DATA_FILES_DIR, "state_transitions.csv")
    state_transitions = pd.read_csv(file_name, index_col="Current state")

    # Initialise the game scores and when they get displayed
    score_names = ("happiness", "health", "hunger", "money", "your_health")
    score_states = [1, 10, 16]
    scores = {}
    for score_name in score_names:
        scores[score_name] = 0

    # print(states)
    # print(state_transitions)

    # Start with the first state in the list
    current_state_id = states.index[0]

    while True:

        # If the current state does not exist then end
        if current_state_id not in states.index:
            print(f"Can't find state id {current_state_id}")
            break

        # Print the details of the current state
        current_state = states.loc[current_state_id].to_dict()
        print(f'{current_state["Name"].title()} : {current_state["Description"].capitalize()}')

        # If now is a good time to display the scores then do so
        if current_state_id in score_states:
            print("Scores:")
            for key,value in scores.items():
                print(f'\t{key.title()}:{value}')

        # If the current state has no transitions then end
        if current_state_id not in state_transitions.index:
            print(f'No choices available for state {current_state["Name"]}')
            break

        # Get the list of transitions for the current state
        # Not using .loc() as can return Series or DataFrame in certain scenarios
        transitions = state_transitions[state_transitions.index == current_state_id]

        try:
            # Ask the user to pick an input based on the available options
            choice = pick("Choice", list(transitions["Input"]), auto_pick=False)
        except:
            print("Bye Bye")
            break

        # Get the state transition details for the chosen state
        transition = transitions[(transitions["Input"] == choice)].to_dict(orient="index")[current_state_id]

        # Process the state transition using the dictionary data
        print(transition["Output"].capitalize())
        current_state_id = transition["Next State"]
        for score_name in score_names:
            scores[score_name] += transition[score_name]

        # User presses enter then loop
        x = input()

    # See how you got on in the game...
    print("\nFinal Scores:")
    for key, value in scores.items():
        print(f'\t{key.title()}:{value}')


def df_test3():

    adult = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                        names=['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
                               'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                               'hours_per_week', 'native_country', 'label'],
                        index_col=False)

    print("Shape of data{}".format(adult.shape))
    print(adult.head())
