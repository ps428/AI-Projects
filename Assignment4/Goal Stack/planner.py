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
    i=0
    for item in state:
        i+=1
        # print("-----",i,"---",item)
        base_name = item.base_name()
        if(base_name == "ON"):
            print(colored("ON("+item.X+","+item.Y+")",'magenta'),end="")
        
        if(base_name == "ONTABLE"):
            print(colored("ONTABLE("+item.X+")","yellow"),end="")
        if(base_name == "CLEAR"):
            print(colored("CLEAR("+item.X+")",'cyan'),end="")
        if(base_name == "HOLDING"):
            print(colored("HOLDING("+item.X+")",'red'),end="")
        if(base_name == "ARMEMPTY"):
            print(colored("ARMEMPTY",'blue'),end="")
        if(base_name == "S"):
            print("S("+item.X+","+item.Y+")",end="")
        if(base_name == "US"):
            print("US("+item.X+","+item.Y+")",end="")
        if(base_name == "PU"):
            print("PU("+item.X+")",end="")
        if(base_name == "PD"):
            print("PD("+item.X+")",end="")
        
        if(i<len(state)):
            print(", ",end="")

def print_stack(state):
    state = state.copy()
    state.reverse()
    for item in state:
        base_name = item.base_name()
        if(base_name == "ON"):
            print(colored(" ON("+item.X+","+item.Y+")",'magenta'))
        if(base_name == "ONTABLE"):
            print(colored(" ONTABLE("+item.X+")","yellow"))
        if(base_name == "CLEAR"):
            print(colored(" CLEAR("+item.X+")",'cyan'))
        if(base_name == "HOLDING"):
            print(colored(" HOLDING("+item.X+")",'red'))
        if(base_name == "ARMEMPTY"):
            print(colored(" ARMEMPTY",'blue'))
        if(base_name == "S"):
            print(" S("+item.X+","+item.Y+")")
        if(base_name == "US"):
            print(" US("+item.X+","+item.Y+")")
        if(base_name == "PU"):
            print(" PU("+item.X+")")
        if(base_name == "PD"):
            print(" PD("+item.X+")")

def print_conjoined_sub_goals(state):
    i=0
    for item in state:
        i+=1
        base_name = item.base_name()
        if(base_name == "ON"):
            print(colored(" ON("+item.X+","+item.Y+")",'magenta'),end="")
        
        if(base_name == "ONTABLE"):
            print(colored(" ONTABLE("+item.X+")","yellow"),end="")
        if(base_name == "CLEAR"):
            print(colored(" CLEAR("+item.X+")",'cyan'),end="")
        if(base_name == "HOLDING"):
            print(colored(" HOLDING("+item.X+")",'red'),end="")
        if(base_name == "ARMEMPTY"):
            print(colored(" ARMEMPTY",'blue'),end="")
        if(base_name == "S"):
            print(" S("+item.X+","+item.Y+")",end="")
        if(base_name == "US"):
            print(" US("+item.X+","+item.Y+")",end="")
        if(base_name == "PU"):
            print(" PU("+item.X+")",end="")
        if(base_name == "PD"):
            print(" PD("+item.X+")",end="")

        if(i<len(state)):
            print(" AND",end="")

    print( " <-- Conjoined Sub Goals")
    
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

class GSP:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_operations(self):
        #final operations needed: PLAN QUEUE
        plan_queue = []

        #stack of sub goals and operators
        goal_stack = []

        # state 0, state of the game
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
            print()
            print()
            print(colored("-----\nCURRENT STATE: ","white"),end="")
            print_state(state_s0)
            print()
            print()
            
            # If we encounter a list as the top element, 
            # This means that this list has the pre conditions needed for a particular operator
            # So we add these list elements to the stack 
            if type(top_element) is list:
                
                # print("ii_________",goal_stack)
                
                # pop the list from the stack 
                conjurned_goal = goal_stack.pop()
                
                # print("_________",goal_stack)
                # print("\n_________",conjurned_goal)
                print(colored("GOAL STACK: ","white"))

                goal_state_before_addition = goal_stack.copy()
                print_stack(conjurned_goal)

                # add the preconditions to the goal stack
                # if only one precondition, then don't repeat for subgoals
                if(len(conjurned_goal)>1):
                    print_conjoined_sub_goals(conjurned_goal)
                for goal in conjurned_goal:
                    if goal not  in state_s0:
                        goal_stack.append(goal)
                # print("_________",goal_stack)
                print_stack(goal_state_before_addition)
                print()

                continue
                
            else:
                # if we don;t encounter the preconditions, then simply prrrint the stack
                print(colored("GOAL STACK: ","white"))
                print_stack(goal_stack)

            
            print()
            print()
            # print the plan queue, if it is greater then 1 else print a dash (-)
            if (len(plan_queue))>1:
                print("PLAN QUEUE: ",end="")
                print_state(plan_queue[:len(plan_queue)-1])
            else:
                print("PLAN QUEUE: -",end="")

            print()
            print()
            
            # if the top element is an operation, then
            if(check_for_operation(top_element)):
                # print the operator
                print(colored("\nOperator: ","white"),end="")
                print_state([top_element])
                print()

                #print its preconditions, add and delete conditions
                print(colored("Preconditions are: ",'white'),end="")
                print_state(top_element.precondition())
                print()
                print(colored("Add list is (Conditions that will become true): ",'white'),end="")
                print_state(top_element.add())
                print()
                print(colored("Delete list is (Conditions that will become false): ",'white'),end="")
                print_state(top_element.delete())
                print()
                print()

                # the new updated goal stack post application of the preconditions of the given operator
                # and their conjoined sub goal
                print(colored("Changed Goal Stack",'white'))
                # print_stack(top_element.precondition())
                print_conjoined_sub_goals(top_element.precondition())
                print_stack(goal_stack)
                
                # set the last element of the goal stack, (pop) as the operator
                operator = goal_stack[-1]

                preconditions_met = True

                #if preconditions are met, 
                if preconditions_met:   
                    # pop the operator from the goal stack
                    goal_stack.pop()     
                    #enqueue the operator the the plan queue
                    plan_queue.append(operator)
                    

                    # update the current state as per the add and delete list of the operator
                    # print("operator: ", operator)
                    for delete_conditions in operator.delete():
                        for predicate in state_s0:
                            if predicate.is_equal(delete_conditions):
                                state_s0.remove(predicate)
                    for add_conditions in operator.add():
                        state_s0.append(add_conditions)

                    
            # if the top element is a predicate or subgoal
            elif(check_for_predicates(top_element)):
                # print("predicate: ", top_element)
                # print the predicate/subgoal
                print(colored("\n\nPredicate: ","white"),end="")
                print_state([top_element])
                print()
                            
                is_true = False
                # if the predicate is true in the current state, 
                # then simply pop it from the goal stack
                for predicate in state_s0:
                    if predicate.is_equal(top_element):
                        print(colored("This is true in the current state. So we simply pop it from the goal stack.",'white'))
                        goal_stack.pop()
                        is_true = True
                        # if predicate.base_name() is not "ARMEMPTY":
                            # print("--SIMPLE POP--",predicate.base_name(), top_element.base_name(),predicate.X,top_element.X)

                # if the predicate was not true in the current state, 
                # then find the operator that will make this particular predicate true
                if(not is_true):
                    # print("Complex, not found in the state, so something")
                    # pop the predicate from the goal stack
                    goal_stack.pop()
                    
                    # get the operations needed for making the predicate true
                    new_operations_needed = top_element.perform_action(state_s0)
                   
                    print(colored("This is false in the current state. So we will pop it and we need to make it true by:",'white'))

                    # print the needed operator
                    if(new_operations_needed is None):
                        # print(top_element.X)
                        flag = False
                        print("ERROR")
                        exit()
                    print_state(new_operations_needed)
                    print(colored("\nSo we will push this new operator in the stack along with its preconditions.",'white'))
                  
                    # push the newly found operators needed to make the predicate true
                    goal_stack.append(new_operations_needed[0])

                    # push thee list of preconditions needed for operator selected
                    goal_stack.append(new_operations_needed[0].precondition())
                    # print(goal_stack)
                    
        if flag==False:
            print("\n--------------------------------------\nNO SOLUTIONS FOUND")
            return None
        return plan_queue


