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
    def delete(self):
        pass
    
    # to store add post conidtions
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
        return [predicates.Clear(self.Y), predicates.Holding(self.X)]
    
    def delete(self):
        return [predicates.Clear(self.Y), predicates.Holding(self.X)]

    def add(self):
        return [predicates.ArmEmpty()(), predicates.On(self.X, self.Y)]


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
        return [predicates.ArmEmpty(), predicates.On(self.X, self.Y), predicates.Clear(self.X) ]

    def delete(self):
        return [predicates.ArmEmpty(), predicates.On(self.X, self.Y)]

    def add(self):
        return [predicates.Clear(self.Y), predicates.Holding(self.X)]


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
        return [predicates.Clear(self.X), predicates.OnTable(self.X), predicates.ArmEmpty()]

    def delete(self):
        return [predicates.ArmEmpty(), predicates.OnTable(self.X)]

    def add(self):
        return [predicates.Holding(self.X)]



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
        return [predicates.Holding(self.X)]
    
    def delete(self):
        return [predicates.Holding(self.X)]

    def add(self):
        return [predicates.ArmEmpty(), predicates.OnTable(self.X)]




