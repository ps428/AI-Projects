# Facts

loves(romeo, juliet).

loves(juliet, romeo) :- loves(romeo, juliet).

male(albert).
male(john).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).

female(alice).
female(betsy).
female(diana).

happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).

near_water(bob).

# Rules now

runs(albert) :-
    happy(albert).

dances(alice) :-
    happy(alice),
    with_albert(alice).

does_alice_dances :- dances(alice),
    write("When Alice is happy and with Albert, she dances.").

swims(bob) :-
    happy(bob),
    near_water(bob).

# Special example here :
# If I don't , i.e. and operator then even not definition of a function works pretty well,

swims_with_error(bill) :-
    happy(bill),
    near_water_error(bill).

swims(bill) :-
    happy(bill).

swims(bill) :-
    near_water_error(bill).
