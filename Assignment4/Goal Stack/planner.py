import predicates, operations

def print_state(state):
    for item in state:
        base_name = item.base_name()
        if(base_name is "ON"):
            print(" ON("+item.X+","+item.Y+")",end="")
        
        if(base_name is "ONTABLE"):
            print(" ONTABLE("+item.X+")",end="")
        if(base_name is "CLEAR"):
            print(" CLEAR("+item.X+")",end="")
        if(base_name is "HOLDING"):
            print(" HOLDING("+item.X+")",end="")
        if(base_name is "ARMEMPTY"):
            print(" ARMEMPTY",end="")
        if(base_name is "S"):
            print(" S("+item.X+","+item.Y+")",end="")
        if(base_name is "US"):
            print(" US("+item.X+","+item.Y+")",end="")
        if(base_name is "PU"):
            print(" PU("+item.X+")",end="")
        if(base_name is "PD"):
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
            print("outside",goal_stack)
            print_state(state_s0)
            # print( top_element  )
            print( "Outside, name: ",top_element.base_name())
            if(check_for_operation(top_element)):
                operator = goal_stack.pop()
                plan_queue.append(operator)
                print("operator: ", operator)
                for add_conditions in operator.add():
                    state_s0.append(add_conditions)

                
            elif(check_for_predicates(top_element)):
                print("predicate: ", top_element)

                is_true = False
                for predicate in state_s0:
                    if predicate.is_equal(top_element):
                        goal_stack.pop()
                        is_true = True
                        print("--SIMPLE POP--")

                if(not is_true):
                    print("Complex, not found in the state, so something")
                    new_operations_needed = top_element.perform_action(state_s0)
                    
                    if(new_operations_needed is None):
                        print(top_element.X)
                    #     flag = False
                        exit()

                    goal_stack.pop()
                    goal_stack.append(new_operations_needed[0])
                    for precondition in new_operations_needed[0].precondition():
                        goal_stack.append(precondition)
                        print("____________",precondition.base_name())

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
print_state(steps)