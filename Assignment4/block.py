from termcolor import colored


class Block:
    def __init__(self,value):
        self.value = value
        self.on_table = True
        self.clear_top = True

class Table:
    def __init__(self):
        self.on_dict = {}
        self.on_table_list = []
        self.clear_top_list = []
        self.holding_list = []

    def hold(self, X):
        if(self.arm_empty()):
            if(X.on_table or X.clear_top):
                self.holding_list.append(X)
    
    def clear(self, X):
        if(not X.clear_top):
            X.clear_top = True
    
    def arm_empty(self):
        if(len(self.holding_list) is 0):
            return True
        return False
    
    def put_down(self):
        # precondition: arm is not empty
        if(not self.arm_empty()):
            X = self.holding_list[0]
            
            # del contition: nothing in holding list and arm is empty now 
            self.holding_list.pop()
            
            # post condtion: X is on table
            X.on_table = True
            self.clear(X)

            # post condtion: X is on table list
            self.on_table_list.append(X)

    def pick_up(self, X):
        # precondition: arm is empty
        if(self.arm_empty()):
            # precondition: empty top and on table, not in any stack
            if(X.clear_top == True) and X.on_table == True:
                
                # post condition: holding now and arm is not empty
                self.hold(X)
                # del contition: not on table now
                X.on_table = False

                # del contition: not on table list now
                for block in self.on_table_list:
                    if block.value is X.value:
                        X = block
                self.on_table_list.remove(X)
                
    def stack_now(self, X, Y):
        # precondition: y has empty top and x is being in the arm now i.e. hold(x)
        if(Y.clear_top == True and X.value == self.holding_list[0].value):  

            # del condition: top of y is not clear now
            Y.clear_top = False

            for block in self.clear_top_list:
                    if block.value is Y.value:
                        Y = block
            self.clear_top_list.remove(Y)

            # del condition: X is being popped and arm is empty now
            self.holding_list.pop()

            # post condition: added (X,Y) to on dictionary
            self.on_dict[Y] = X

    def unstack_now(self, X, Y):
        unstackable = False
        # precondition: x,y is in the on dictionary
        for key, value in self.on_dict.items():
            if(Y.value is key.value and X.value is value.value):
                Y = key
                X = value
                unstackable = True


        # precondition: x has clear top and arm is empty    
        if(unstackable and X.clear_top == True and self.arm_empty()):
            
            # del condition: remove (X,Y) from on dictionary
            self.on_dict.pop(Y)

            # post condition: holding X now and arm is not empty
            self.hold(X)

            # post condition: top of Y is now empty
            self.clear(Y)
            self.clear_top_list.append(Y)
            
    # Main functions
    def PD(self):
        self.put_down()
    
    def PU(self, A):
        X = Block(A)
        self.pick_up(X)
    
    def S(self, A, B):
        X = Block(A)
        Y = Block(B)

        self.stack_now(X,Y)

    def US(self, A, B):
        X = Block(A)
        Y = Block(B)

        self.unstack_now(X,Y)

    def add_block(self, A):
        X = Block(A)
        self.clear_top_list.append(X)
        self.on_table_list.append(X)


    def print_table(self):
        print('\n-----------------------------------------------------------\n')

        for key, value in self.on_dict.items():
            print("ON: [",key.value,", ",value.value,"]")

        print()
        for block in self.on_table_list:
            print("ONT: [",block.value,"]")

        print()
        if(len(self.holding_list) is not 0):
            for hold in self.holding_list:
                print("HOLD: ",colored(hold.value,'red'))
        else:
            print("AE")

        print()
        for block in self.clear_top_list:
            print("CLR: [",block.value,"]")

        print('----------------------------------------------------------------\n')
        pass
        
