from termcolor import colored
import planner

import main

# change the file name here for different files
inputs = open('input_file4.txt')
lines = inputs.readlines()
a = []

# iterating over the file to store the initial and goal state 
for line in lines:
    data = (line.split(":"))
    a.append(data[1].strip())

#generating the states in particular order from the raw input
initial_state = main.generate_state(a[1],a[2],a[3],a[4],a[5])
goal_state = main.generate_state(a[8],a[9],a[10],a[11],a[12])

# call the goal stack planner from the planner file
goal_stack = planner.GSP(initial_state=initial_state, goal_state=goal_state)

# get the plan queue from the algorithm
plan_queue = goal_stack.get_operations()

# print the final output
print(colored("\n\n--------------------------------------------------------------------------------\nInitial State: ","white"))
planner.print_state(initial_state)
print(colored("\n\nGoal State: ","white"))
planner.print_state(goal_state)
print(colored("\n\nPlan Queue: ","white"))
planner.print_state(plan_queue)
print()