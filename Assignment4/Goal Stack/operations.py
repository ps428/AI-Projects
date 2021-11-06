# Defining all the operations in this file.
# Keeping a Operations class and extending its child nodes
# S, US, PU, PD

import predicates

class Operations:
     # to store the string representation of the given predicate: like on(a,b) for on predicate
    def string_representation(self):
        pass
    
    # to check for equality with any other object(predicate)
    def is_equal(self, testing_object):
        return self.__dict__ == testing_object.__dict__ and self.__class__ == testing_object.__class__

    # to know the base name of the predicate, on or clear or holding etc
    def base_name(self):
        pass

    # to store preconditions
    def precondition(self):
        pass
    
    # to store delete post conditions
    # Should become false after execution
    def delete(self):
        pass
    
    # to store add post conidtions
    # Should become true after execution
    def add(self):
        pass

class S(Operations):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def string_representation(self):
        return "S("+self.X+","+self.Y+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)
    
    def base_name(self):
        return "S"
    
    def precondition(self):
        return [predicates.CLEAR(self.Y), predicates.HOLDING(self.X)]
    
    def delete(self):
        return [predicates.CLEAR(self.Y), predicates.HOLDING(self.X)]

    def add(self):
        return [predicates.ARMEMPTY(), predicates.ON(self.X, self.Y)] # TODO x should be clear nows


class US(Operations):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def string_representation(self):
        return "US("+self.X+","+self.Y+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)

    def base_name(self):
        return "US"

    def precondition(self):
        return [predicates.ARMEMPTY(), predicates.ON(self.X, self.Y), predicates.CLEAR(self.X) ]

    def delete(self):
        return [predicates.ARMEMPTY(), predicates.ON(self.X, self.Y)]# TODO x should not be clears

    def add(self):
        return [predicates.CLEAR(self.Y), predicates.HOLDING(self.X)]


class PU(Operations):
    def __init__(self, X):
        self.X = X
    
    def string_representation(self):
        return "PU("+self.X+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)

    def base_name(self):
        return "PU"

    def precondition(self):
        return [predicates.CLEAR(self.X), predicates.ONTABLE(self.X), predicates.ARMEMPTY()]

    def delete(self):
        return [predicates.ARMEMPTY(), predicates.ONTABLE(self.X)] # TODO x should not be clear

    def add(self):
        return [predicates.HOLDING(self.X)]



class PD(Operations):
    def __init__(self, X):
        self.X = X
    
    def string_representation(self):
        return "PD("+self.X+")"

    def is_equal(self, testing_object):
        return super().is_equal(testing_object)

    def base_name(self):
        return "PD"

    def precondition(self):
        return [predicates.HOLDING(self.X)]
    
    def delete(self):
        return [predicates.HOLDING(self.X)]

    def add(self):
        return [predicates.ARMEMPTY(), predicates.ONTABLE(self.X)]# TODO x should be clear now




