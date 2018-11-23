child(Child,Parent) :-
	father(Parent,Child);
	mother(Parent,Child).

daughter(Child,Parent) :-
	child(Child,Parent),
	female(Child).

son(Child,Parent) :-
	child(Child,Parent),
	male(Child).


% TASK4b
grandfather(Grandpa,Grandchild) :-
	father(Grandpa,Child),
	child(Grandchild,Child).

% TASK4c
sister(Sister,Sibling) :-
	daughter(Sister,Parent),
	child(Sibling,Parent).

% TASK3
female(helen).
female(francine).
female(sabrina).
female(vivian).

male(alfred).
male(bob).
male(edward).
male(gary).

father(alfred,bob).
father(alfred,helen).
father(alfred,francine).
father(alfred,gary).
father(bob,sabrina).

mother(helen,edward).
mother(helen,daniel).
mother(helen,iris).
mother(helen,judy).
mother(francine,vivian).

/** <Task4a>
?- child(Child,alfred).
?- daughter(Daughter,helen).
?- grandfather(Grandfather,edward).
*/
