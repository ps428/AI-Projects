from os import stat
import predicates, operations
from termcolor import colored
# Text colors:

#       - grey
#       - red
#       - green
#       - yellow
#       - blue
#       - magenta
#       - cyan
#       - white




def print_state(state):
    for item in state:
        base_name = item.base_name()
        if(base_name == "ON"):
            print(colored(" ON("+item.X+","+item.Y+"),",'magenta'),end="")
        
        if(base_name == "ONTABLE"):
            print(colored(" ONTABLE("+item.X+"),","yellow"),end="")
        if(base_name == "CLEAR"):
            print(colored(" CLEAR("+item.X+"),",'cyan'),end="")
        if(base_name == "HOLDING"):
            print(colored(" HOLDING("+item.X+"),",'red'),end="")
        if(base_name == "ARMEMPTY"):
            print(colored(" ARMEMPTY,",'blue'),end="")
        if(base_name == "S"):
            print(" S("+item.X+","+item.Y+")",end="")
        if(base_name == "US"):
            print(" US("+item.X+","+item.Y+")",end="")
        if(base_name == "PU"):
            print(" PU("+item.X+")",end="")
        if(base_name == "PD"):
            print(" PD("+item.X+")",end="")

def check_for_predicates(object):
    my_predicates = ["ON","ONTABLE","CLEAR","ARMEMPTY","HOLDING"]
    for predicate in my_predicates:
        if predicate == object.base_name():
            return True
    
    return False

def check_for_operation(object):
    my_operations = ["S","US","PD","PU"]
    for operation in my_operations:
        if operation == object.base_name():
            return True
    
    return False

def arm(state_s0):
    for predicate in state_s0:
        if predicate.base_name() == "HOLDING":
            return predicate
    
    return predicates.ARMEMPTY()


class GSP:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_operations(self):
        #final operations needed: PLAN QUEUE
        plan_queue = []

        #stack of conjourned sub goals
        goal_stack = []

        # state 0,
        state_s0 = self.initial_state.copy()

        # copy of initial goal state in stack of conjourned sub goals
        goal_stack.append(self.goal_state.copy())
        goal_stack = goal_stack[0]
        # flag as true
        flag = True

        # while the stack is not empty
        while(len(goal_stack)!=0 and flag is True):

            # print(plan_queue)
            # get top element of the stack
            top_element = goal_stack[-1]
            # print_state(goal_stack)
            # print()
            # print( goal_stack )
            # print( "Outside, name: ",top_element.base_name())
            
            if type(top_element) is list:
                
                # print("ii_________",goal_stack)
                conjurned_goal = goal_stack.pop()
                # print("_________",goal_stack)
                # print("\n_________",conjurned_goal)
                for goal in conjurned_goal:
                    if goal not  in state_s0:
                        goal_stack.append(goal)
                # print("_________",goal_stack)
                continue

            
            print()
            print()
            print(colored("CURRENT STATE: ","white"),end="")
            print_state(state_s0)
            print()

            print(colored("GOAL STATE: ","white"),end="")
            print_state(goal_stack)

            if(check_for_operation(top_element)):
                print(colored("\nOperator: ","white"),end="")
                print_state([top_element])
                print()
                
                operator = goal_stack[-1]

                preconditions_met = True

                
                if preconditions_met:   
                    goal_stack.pop()     
                    plan_queue.append(operator)
                    

                    # print("operator: ", operator)
                    for delete_conditions in operator.delete():
                        for predicate in state_s0:
                            if predicate.is_equal(delete_conditions):
                                state_s0.remove(predicate)
                    for add_conditions in operator.add():
                        state_s0.append(add_conditions)

                    
            
            elif(check_for_predicates(top_element)):
                # print("predicate: ", top_element)
                print(colored("\nPredicate: ","white"),end="")
                print_state([top_element])
                print()
                            
                is_true = False
                for predicate in state_s0:
                    if predicate.is_equal(top_element):
                        
                        goal_stack.pop()
                        is_true = True
                        # if predicate.base_name() is not "ARMEMPTY":
                            # print("--SIMPLE POP--",predicate.base_name(), top_element.base_name(),predicate.X,top_element.X)

                if(not is_true):
                    # print("Complex, not found in the state, so something")
                    goal_stack.pop()
                    
                    new_operations_needed = top_element.perform_action(state_s0)
                    
                    if(new_operations_needed is None):
                        # print(top_element.X)
                        flag = False

                    goal_stack.append(new_operations_needed[0])

                    goal_stack.append(new_operations_needed[0].precondition())
                    # print(goal_stack)
                    
        return plan_queue

                # for predicate in




initial_state = [
predicates.ON('A','B'),
predicates.ONTABLE('B'),predicates.ONTABLE('C'),predicates.ONTABLE('D'),
predicates.CLEAR('A'),predicates.CLEAR('C'),predicates.CLEAR('D'),
predicates.ARMEMPTY()
]

goal_state = [  
predicates.ON('B','D'),predicates.ON('D','C'),predicates.ON('C','A'),
predicates.ONTABLE('A'),
predicates.CLEAR('B'),
predicates.ARMEMPTY()
]

goal_stack = GSP(initial_state=initial_state, goal_state=goal_state)
steps = goal_stack.get_operations()
print(colored("\n\n--------------------\nInitial State: ","white"))
print_state(initial_state)
print(colored("\n\nGoal State: ","white"))
print_state(goal_state)
print(colored("\n\nPlan Queue: ","white"))
print_state(steps)
print()