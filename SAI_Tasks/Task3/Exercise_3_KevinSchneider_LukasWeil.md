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

## Task 2 -

## Task 3 -

## Task 4 -

## Task 5 -