
mirror(t(Root, L, R), t(Root, L, R)):-
    L = nil,
    R = nil.

mirror(t(Root, L, R), t(Root, R1, L)):-
    L = nil,
    R \= nil,
    mirror(R, R1).

mirror(t(Root, L, R), t(Root, R, L1) ):-
    L \= nil,
    mirror(L,L1),
    R = nil.

mirror(t(Root, L, R), t(Root, R1, L1) ):-
    L \= nil,
    mirror(L,L1),
    R \= nil,
    mirror(R, R1).



mirror(nil,R).

make_mirror(List, Tree):-

    % for bst construction
    %construct(List, T),
    % for general tree
    insert(List, T),
    mirror(T, T_mirrored),
    write(T_mirrored).


% for bst
add(X,nil,t(X,nil,nil)).
add(X,t(Root,L,R),t(Root,L1,R)) :- X < Root, add(X,L,L1).
add(X,t(Root,L,R),t(Root,L,R1)) :- X > Root, add(X,R,R1).
% if we consider repetative values
%add(X,t(Root,L,R),t(Root,L1,R)) :- add(X,L,L1).

construct(List,T) :- constructw(List,T,nil).

constructw([],T,T).
constructw([N|Ns],T,T0) :- add(N,T0,T1), constructw(Ns,T,T1).


% for general tree
adds(X,nil,t(X,nil,nil)).
adds(X,t(Root,L,R),t(Root,L1,R)) :- L=nil,adds(X,L,L1).
adds(X,t(Root,L,R),t(Root,L,R1)) :- R=nil,adds(X,R,R1).
adds(X,t(Root,L,R),t(Root,L1,R)) :- adds(X,L,L1).

insert(L,T) :- insert(L,T,nil).

insert([],T,T).
insert([N|Ns],T,T0) :- adds(N,T0,T1), insert(Ns,T,T1).
