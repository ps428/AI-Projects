import planner, predicates
from termcolor import colored

def generate_state(on_predicates, on_table_predicates, clear_predicates, arm_empty, holding):
    state = []
    on_list = on_predicates.split(";")
    on_table_list = on_table_predicates.split(",")
    clear_list = clear_predicates.split(",")

    # print(on_list)
    # print(on_table_list)
    # print(clear_list)
    for on_elements in on_list:
        element_X = on_elements[1]
        element_y = on_elements[3]
        on = predicates.ON(element_X, element_y)
        # print(on)
        state.append(on)

    for on_table in on_table_list:
        element_X = on_table
        on_t = predicates.ONTABLE(element_X)
        # print(on_t)
        state.append( on_t)

    for cleared in clear_list:
        element_X = cleared
        clear = predicates.CLEAR(element_X)
        # print(clear)
        state.append(clear)
    
    if arm_empty=='y':
        empty = predicates.ARMEMPTY()
        # print(empty)
        state.append(empty)
    elif arm_empty == 'n':
        state.append(predicates.HOLDING(holding))
    return state

# print("Enter Initial State: ")
# on_predicates = input("Enter ON predicates seperated by semicolon (E.g. [A,B];[D,C]): ")
# on_table_predicates = input("Enter ONTABLE predicates seperated by commas(E.g. B,C): ")
# clear_predicates = input("Enter CLEAR predicates seperated by commas(E.g. A,D): ")
# arm_empty = input("Is arm empty: y or n")
# holding = ""
# if arm_empty=='n':
#     holding = input("Enter HOLDING element:")

# initial_state = generate_state(on_predicates, on_table_predicates, clear_predicates, arm_empty, holding)
# # planner.print_state(initial_state)

# print("Enter Goal State: ")
# on_predicates = input("Enter ON predicates seperated by semicolon (E.g. [A,B];[D,C]): ")
# on_table_predicates = input("Enter ONTABLE predicates seperated by commas(E.g. B,C): ")
# clear_predicates = input("Enter CLEAR predicates seperated by commas(E.g. A,D): ")
# arm_empty = input("Is arm empty: y or n")
# if arm_empty=='n':
#     holding = input("Enter HOLDING element:")



# goal_state = generate_state(on_predicates, on_table_predicates, clear_predicates, arm_empty, holding)

# print()
# planner.print_state(goal_state)


# goal_stack = planner.GSP(initial_state=initial_state, goal_state=goal_state)
# plan_queue = goal_stack.get_operations()
# print(colored("\n\n--------------------------------------------------------------------------------\nInitial State: ","white"))
# planner.print_state(initial_state)
# print(colored("\n\nGoal State: ","white"))
# planner.print_state(goal_state)
# print(colored("\n\nPlan Queue: ","white"))
# planner.print_state(plan_queue)
# print()