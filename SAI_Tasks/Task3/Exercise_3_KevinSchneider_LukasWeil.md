# Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347)  # Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347)  

## Task 1 - Clause Form

Transform the following formula of first order logic into the clause form by
applying the transformation algorithm from the lecture. Provide the clauses
as sets of literals.

$$
(\forall_{X}\forall_{Y}((\forall_{Z}p(X,Y,Z))\rightarrow (\exists_{P}q(Y,P))))\wedge\exists_{S}r(S)
$$

</br>

**Solution**:

1. Convert to negation normal form:

    $$
    \forall_{X}\forall_{Y}(\exists_{S}r(S) \wedge (\exists_{P}(q(Y,P) \vee \exists_{Z}\neg p(X,Y,Z))))
    $$

2. Skolemization:

    Move quantifiers outward:

    $$
    \forall_{X}\forall_{Y}(\exists_{S}r(S) \wedge (\exists_{P}(q(Y,P) \vee \exists_{Z}\neg p(X,Y,Z))))
    $$

    </br>
    </br>

    $$
    \forall_{X}\forall_{Y}(\exists_{P}(\exists_{S}r(S) \wedge (q(Y,P) \vee \exists_{Z}\neg p(X,Y,Z))))
    $$

    </br>
    </br>

    $$
    \forall_{X}\forall_{Y}(\exists_{P}(\exists_{S}r(S) \wedge \exists_{Z} (q(Y,P) \vee \neg p(X,Y,Z))))
    $$

    </br>
    </br>

    $$
    \forall_{X}\forall_{Y}(\exists_{P}(\exists_{Z}(\exists_{S}r(S) \wedge  (q(Y,P) \vee \neg p(X,Y,Z)))))
    $$

    </br>
    </br>

    $$
    \forall_{X}\forall_{Y}(\exists_{P}(\exists_{Z}(\exists_{S}(r(S) \wedge  (q(Y,P) \vee \neg p(X,Y,Z))))))
    $$

    </br>
    </br>

    Replace functions with skolem functions:

    </br>

    $$
    \forall_{X}\forall_{Y}(r(f_{1}(X,Y)) \wedge  (q(Y,f_{2}(X,Y)) \vee \neg p(X,Y,f_{3}(X,Y))))
    $$

    </br>

    Drop universal quantifiers:

    </br>

    $$
    r(f_{1}(X,Y)) \wedge  (q(Y,f_{2}(X,Y)) \vee \neg p(X,Y,f_{3}(X,Y)))
    $$

    </br>

    Distribute ORs inwards over ANDs

    </br>

    $$
    (r(f_{1}(X,Y))  \vee q(Y,f_{2}(X,Y))) \wedge  ((r(f_{1}(X,Y)) \vee \neg p(X,Y,f_{3}(X,Y))))
    $$

    </br>

    As set of literals:

    $$
    \left\{ \left \{r(f_{1}(X,Y)) , q(Y,f_{2}(X,Y)) \right \}, \left\{r(f_{1}(X,Y)) , \neg p(X,Y,f_{3}(X,Y))\right \}\right \}
    $$

## Task 2 -

## Task 3 -



## Task 4 -

Skript: Arztbesuch

Entitäten: 
	Reception
	Reception Room
	Chair in Waiting Room
	Waiting Room
	Doctors Room
	Alices Bed
	Medical Certificate
	Doctors Practice

Roles:

	A = Alice
	R = Receptionist
	D = Doctor
	E = Employer

Prerequisites:
	
	A is sick 
	A is worried
	A has no Medical Certificate
	D is at work

Postconditions:

	A is relieved
	A has Medical Certificate
	
Events: 
	
	Scene 1: Decisionmaking
		A Expel mucus
		A Conc
		A MBuild go to Doctor
		A PTrans A Doctors Practice
		A PTrans A Reception Room

	Scene 2: At the Gates
		A MTrans R personal information and information on disease
		R Speak A request to sit down in Waiting Room
		A MBuild sit down in Waiting Room
		A PTrans to Waiting Room
		A PTrans to Chair in Waiting Room
		A Move sit on Chair in Waiting Room

	Scene 3: Time has come
		D PTrans to Waiting Room
		D Speak call in Alice
		A Attend Eyes&Ears to D
		A MBuild go to Doctors Room
		A Move stand up
		A PTrans to Doctors Room
		D PTrans to Doctors Room

	Scene 4: Final Destination
		D Speak ask A about problems
		A Conc
		A MBuild what exactly are problems
		A Speak problems
		D Attend Ears to A
		D Propel As knee and As chest
		D Attend Eyes to As throat
		D Conc
		D MBuild Diagnosis
		D Speak Diagnosis to A
		D Speak to A stay in bed
		A Attend Ears to D
		D ATrans Medical Certificate

	Scene 5: Hiatus
		A MBuild relieve
		A MBuild go home
		A PTrans Outside Doctors Practice 
		A PTrans Bed





		




## Task 5 -