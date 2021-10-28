class Block:
    def __init__(self,value):
        self.value = value
        self.on_table = True
        self.clear_top = True

class Table:
    def __init__(self):
        self.on = {}
        self.on_table = []
        self.clear_top = []
        self.holding = []

    def hold(self, X):
        if(self.arm_empty()):
            if(X.on_table or X.clear_top):
                self.holding.append(X)
    
    def clear(self, X):
        if(not X.clear_top):
            X.clear_top = True
    
    def arm_empty(self):
        if(len(self.holding) is 0):
            return True
        return False
    
    def put_down(self):
        # precondition: arm is not empty
        if(not self.arm_empty()):
            X = self.holding[0]
            
            # del contition: nothing in holding list and arm is empty now 
            self.holding.pop()
            
            # post condtion: X is on table
            X.on_table = True
            self.clear(X)

            # post condtion: X is on table list
            self.on_table.append(X)

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
                for block in self.on_table:
                    if block.value is X.value:
                        X = block
                self.on_table.remove(X)
           
                
    def stack_now(self, X, Y):
        # precondition: y has empty top and x is being in the arm now i.e. hold(x)
        if(Y.clear_top == True and X.value == self.holding[0].value):  

            # del condition: top of y is not clear now
            Y.clear_top = False

            # del condition: X is being popped and arm is empty now
            self.holding.pop()

            # post condition: added (X,Y) to on dictionary
            self.on[Y] = X

    def unstack_now(self, X, Y):
        unstackable = False
        # precondition: x,y is in the on dictionary
        for key, value in self.on.items():
            if(Y.value is key.value and X.value is value.value):
                Y = key
                X = value
                unstackable = True

        # precondition: x has clear top and arm is empty    
        if(unstackable and X.clear_top == True and self.arm_empty()):
            
            # del condition: remove (X,Y) from on dictionary
            self.on.pop(Y)

            # post condition: holding X now and arm is not empty
            self.hold(X)

            # post condition: top of Y is now empty
            self.clear(Y)
