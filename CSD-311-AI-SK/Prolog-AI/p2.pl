% Question 2

% Some definitions
% t(New_node,Left_child,Right_child) => New_node is node value, Left_child is Left child, Right_child is right child of the node New_node

% Adding a node to generic tree

% Base case, when the tree is no_child, add the node New_node to the tree and put left child and right child as no_child
adds(New_node,no_child,t(New_node,no_child,no_child)):-
    write('\nBase case: Adding new node '),write(New_node),nl.


% Here L1 is the new tree created as a consequence of addition of the node New_node to the tree
% If the left child of the node is no_child, add the new node to the left child of is_tree
adds(New_node,t(Root,Left_child,Right_child),t(Root,L1,Right_child)) :- 
    Left_child=no_child,
    adds(New_node,Left_child,L1).

% If the right child of the node is no_child, add the new node to the right child of it
adds(New_node,t(Root,Left_child,Right_child),t(Root,Left_child,R1)) :- 
    Right_child=no_child,
    adds(New_node,Right_child,R1).

% For a general case when the two childs of the node are filled, recursively call the left child and add there
adds(New_node,t(Root,Left_child,Right_child),t(Root,L1,Right_child)) :- 
    adds(New_node,Left_child,L1).

% Making the tree via list

% If the input to the insert function is a list and a variable, then call another function update_insert and make the third parameter as no_child indicating a vacant tree
insert(List,T) :- 
    update_insert(List,T,no_child).

% Base case for update_insert function. to stop the recursive calls, if the list is empty, return the tree T itself
update_insert([],T,T).

% Recursive calls for update_insert function, This slices the first element (N) of the list, 
% Then it calls the adds function with the first element N and returns the T1 tree after addition of the element N to the tree  T0,
% Then we make the recursive call of the update_insert function with the rest of list ( Ns ) as the new list
update_insert([L|List],T,T0) :- 
    adds(L,T0,T1), 
    update_insert(List,T,T1).


%-------------------------------------------------------------------------------------
% Adding a node to BST

% Base case, when the tree is no_child, add the node New_node to the tree and put left child and right child as no_child
add(New_node,no_child,t(New_node,no_child,no_child)):-
    write('\nBase case: Adding new node '),write(New_node),nl.

% If the new node, New_node is less than the Root node, then pass the left child (Left_child) of the Root node recursively to the function add
% Here L1 is the new tree created as a consequence of addition of the node New_node to the tree
add(New_node,t(Root,Left_child,Right_child),t(Root,L1,Right_child)) :- 
    write('\nChecking: '),write(New_node),write(' < '),write(Root),write(' or not.\n'),
    New_node < Root, 
    add(New_node,Left_child,L1).

% If the new node, New_node is greater than the Root node, then pass the right child (Right_child) of the Root node recursively to the function add
add(New_node,t(Root,Left_child,Right_child),t(Root,Left_child,R1)) :- 
    write('\nChecking: '),write(New_node),write(' > '),write(Root),write(' or not.\n'),
    New_node > Root, 
    add(New_node,Right_child,R1).

% If we consider duplicate values, then add to the left child recursively
%add(New_node,t(Root,Left_child,Right_child),t(Root,L1,Right_child)) :- 
%    add(New_node,Left_child,L1).


% Making the tree via list

% If the input to the construct function is a list and a variable, then call another function update_construct and make the third parameter as no_child indicating a vacant tree
construct(List,T) :- 
    update_construct(List,T,no_child).


% Base case for update_construct function. to stop the recursive calls, if the list is empty, return the tree T itself
update_construct([],T,T).

% Recursive calls for update_construct function, This slices the first element (N) of the list, 
% Then it calls the add function with the first element N and returns the T1 tree after addition of the element N to the tree  T0,
% Then we make the recursive call of the update_construct function with the rest of list ( Ns ) as the new list
update_construct([L|List],T,T0) :- 
    add(L,T0,T1), 
    update_construct(List,T,T1).

% Add a new element to a tree represened by list
add_to_list(New_Node, List, Tree):-
    construct(List, T),
    add(New_Node, T, T2),
    write(T2).

%-------------------------------------------------------------------------------------
% Mirror function

% Base case when the the childern are no_child, don''t swap the tree
make_mirror(t(Root, Left_child, Right_child), t(Root, Left_child, Right_child)):-
    Left_child = no_child,
    Right_child = no_child.

% If the left child is no_child, swap the no_child value with right child of the node
make_mirror(t(Root, Left_child, Right_child), t(Root, R1, Left_child)):-
    Left_child = no_child,
    Right_child \= no_child,
    make_mirror(Right_child, R1).

% If the right child is no_child, swap the no_child value with left child of the node
make_mirror(t(Root, Left_child, Right_child), t(Root, Right_child, L1) ):-
    Left_child \= no_child,
    Right_child = no_child,
    make_mirror(Left_child,L1).

% Recursive calls, when the the childern of the node are not no_child, then recursively call the make_mirror function to left and right child of the tree
make_mirror(t(Root, Left_child, Right_child), t(Root, R1, L1) ):-
    Left_child \= no_child,
    make_mirror(Left_child,L1),
    Right_child \= no_child,
    make_mirror(Right_child, R1).

% basic mirror function that return the same tree if list is no_child
make_mirror(no_child,R).

% if the list has values, then firstly create a tree through the insert function,
% Then take the generated tree and pass that tree to the make tree function
% At last, print the mirrored tree
mirror(List, Tree):-

    % for bst construction
    %construct(List, T),
    % for general tree
    insert(List, T),
    write('Original: '),write(T),nl,
    make_mirror(T, T_mirrored),
    write('Mirrored: '),write(T_mirrored).
