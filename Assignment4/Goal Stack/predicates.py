# Defining all the predicates in this file.
# Keeping a Predicate class and extending its child nodes
# CLEAR, ARMEMPTY, HOLDING, ONTABLE, ON
import operations

class Predicate:
    # to store the string representation of the given predicate: like on(a,b) for on predicate
    def string_representation(self):
        pass
    
    # to check for equality with any other object(predicate)
    def is_equal(self, testing_object):
        return self.__dict__ == testing_object.__dict__ and self.__class__ == testing_object.__class__

    # to know the base name of the predicate, on or clear or holding etc
    def base_name(self):
        pass

    # to get the operations/actions to be executed to achieve the given predicate
    def perform_action(self, state_s0):
        pass


class CLEAR(Predicate):
    def __init__(self, X):
        self.X = X
    
    #CLEAR(X)
    def string_representation(self):
        return "CLEAR("+self.X+")"
    
    def is_equal(self, testing_object):
        return super().is_equal(testing_object)

    def base_name(self):
        return "CLEAR"
    
    def perform_action(self, state_s0):
        for predicate in state_s0:
            # print(predicate.X, predicate.base_name())
            # if predicate.base_name is "ON":
            #     print("asdsad") 
            if predicate.base_name() == "ON" and predicate.Y == self.X:
                # print("TRUE ya nahi")
                return [operations.US(predicate.X, predicate.Y)]
        # return None


class ARMEMPTY(Predicate):
    def __init__(self):
       pass
    
    def string_representation(self):
        return "ARMEMPTY()"
    
    def is_equal(self, testing_object):
        return super().is_equal(testing_object)
    
    def base_name(self):
        return "ARMEMPTY"
    
    def perform_action(self, state_s0 = []):
        for predicate in state_s0:
            if predicate.base_name() == "HOLDING":
                return [operations.PD(predicate.X)]
        return None


class HOLDING(Predicate):
    def __init__(self, X):
        self.X = X
    
    def string_representation(self):
        return "HOLDING("+self.X+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)
    
    def base_name(self):
        return "HOLDING"
    
    def perform_action(self, state_s0):
        # print("HOLDING", self.X)
        for predicate in state_s0:
            if predicate.base_name() == "ONTABLE" and predicate.X == self.X:
                return [operations.PU(self.X)]

        else:
            for predicate in state_s0:
                if predicate.base_name() == "ON" and predicate.X==self.X:
                    return [operations.US(self.X, predicate.Y)]

class ONTABLE(Predicate):
    def __init__(self,X):
        self.X = X

    def string_representation(self):
        return "ONTABLE("+self.X+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)

    def base_name(self):
        return "ONTABLE"
    
    def perform_action(self, state_s0):
        return [operations.PD(self.X)]

class ON(Predicate):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def string_representation(self):
        return "ON("+self.X+","+self.Y+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)
    
    def base_name(self):
        return "ON"

    def perform_action(self, state_s0):
        return [operations.S(self.X, self.Y)]