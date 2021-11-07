from termcolor import colored
import planner

import main

inputs = open('input_file.txt')
lines = inputs.readlines()
a = []
for line in lines:
    data = (line.split(":"))
    a.append(data[1].strip())

initial_state = main.generate_state(a[0],a[1],a[2],a[3],a[4])
goal_state = main.generate_state(a[5],a[6],a[7],a[8],a[9])

goal_stack = planner.GSP(initial_state=initial_state, goal_state=goal_state)
plan_queue = goal_stack.get_operations()
print(colored("\n\n--------------------------------------------------------------------------------\nInitial State: ","white"))
planner.print_state(initial_state)
print(colored("\n\nGoal State: ","white"))
planner.print_state(goal_state)
print(colored("\n\nPlan Queue: ","white"))
planner.print_state(plan_queue)
print()