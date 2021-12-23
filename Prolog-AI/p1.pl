% Question 1

% Some definitions,
% Checking List (L+L1): Intermediate list which has to be checked for prefix or suffix of the original list.
% Original List (L+L2): The original list to which the prefix or suffix are being matched with.

% Base case, when the Checking list is empty, then end then return.
is_prefix([],L2):-
    write('\nTRUE: Prefix matched').

% Recurssive calls when the first elements of the Checking list and the Original list are same
is_prefix([L|L1],[L|L2]) :- 
    write('\nHead is '),write(L),write(' '),
    write('\nRest of checking list is '),write(L1),write(' '),
    write('\nRest of main list is '),write(L2),write('\n'),
    is_prefix(L1,L2).

% Print FALSE: No Match when the first two elements are not same
is_prefix([L|L1],[M|L2]) :- 
    %L1 \= [],
    write('\nFALSE: No Match. '),write(L),write(' is not equal to '),write(M).

% Base case, when the two lists match, i.e. the two lists resulting from the recursive calls match
% Simply, when the passed in list matches with certain last section of the given original list
is_suffix(L1,L1):-
    write('\nTRUE: Suffix Matched '),write(L1).

% Keep the Checking list intact (L1) and keep on popping the top element from the remaining original list
% And call the function recursively, if we encounter the same last elements, then the above function shall be called printing a match
% Else if the remaining section of the original list (L2) becomes an empty list ([]), then print a no match
is_suffix(L1,[L|L2]) :- 
    is_suffix(L1,L2).

% Terminating case when the remaining section of the original list (L2) is empty, then print no match
is_suffix(L1,L2):-
    %L1 = [],
    write('\nFALSE: Suffix did not match. ').
