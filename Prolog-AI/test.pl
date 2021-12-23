% Question 1

is_prefix([],Ys).
is_prefix([X|Xs],[X|Ys]) :- 
    write('\nHead is '),write(X),write(' '),
    write('\nRest of checking list is '),write(Xs),write(' '),
    write('\nRest of main list is '),write(Ys),write('\n'),
    is_prefix(Xs,Ys).

is_suffix(Xs,Xs):-
    write('match '),write(Xs).

is_suffix(Xs,[Y|Ys]) :- 
    is_suffix(Xs,Ys).

% Question 2

%bst construct
add(X,nil,t(X,nil,nil)).
add(X,t(Root,L,R),t(Root,L1,R)) :- X < Root, add(X,L,L1).
add(X,t(Root,L,R),t(Root,L,R1)) :- X > Root, add(X,R,R1).
% if we consider repetative values
%add(X,t(Root,L,R),t(Root,L1,R)) :- add(X,L,L1).

construct(List,T) :- constructw(List,T,nil).

constructw([],T,T).
constructw([N|Ns],T,T0) :- add(N,T0,T1), constructw(Ns,T,T1).
 	
%test_symmetric(L) :- construct(L,T), symmetric(T).

%...testing....

    
mirror(t(L,Root,R),t(R,Root,L)):-
    mirror(L),
    mirror(R).

% almost done
adds(X,nil,t(X,nil,nil)).
adds(X,t(Root,L,R),t(Root,L1,R)) :- L=nil,adds(X,L,L1).
adds(X,t(Root,L,R),t(Root,L,R1)) :- R=nil,adds(X,R,R1).
adds(X,t(Root,L,R),t(Root,L1,R)) :- adds(X,L,L1).

insert(L,T) :- insert(L,T,nil).

insert([],T,T).
insert([N|Ns],T,T0) :- adds(N,T0,T1), insert(Ns,T,T1).



%for base case, we can try to represent the tree as an array
T1 is t(a,t(b,t(d,nil,nil),t(e,nil,nil)),t(c,nil,t(f,t(g,nil,nil),nil))).

% from notes
% b_node(Left_subtree, Node, Right_subtree).
b_n(Left, Node, Right);

b_n(L, 20, R);
L = b_n(b_n(void, 16, void),30,b_n(void,14,void));
R = b_n(void,47,b_n(void,10,void)).

count(void,0).
count(b_n(void,_,void),1).
count(b_n(L,V,R),N):-count(L, N1),count(R, N2), N is 1+N1+N2.


is_tree(void).
is_tree(b_n(L,_,R)):-
    is_tree(L),
    is_tree(R).

wr(X):-
    write(X).

addNode(t(nil,X,Y),V):- 
    write(X),
    write(Y),
    write(V),
    t(V,X,Y),   
    write(' Hakunana Matatata '),
    t(V,X,Y).

