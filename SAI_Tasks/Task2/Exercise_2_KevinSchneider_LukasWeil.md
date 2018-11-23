
# Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347)  

## Task 1 - The Resolution Method

### a)

- C<sub>1</sub> ≡ (X ∨ F ∨ ¬M ∨ R)
- C<sub>2</sub> ≡ (¬F ∨ X ∨ B)
- C<sub>3</sub> ≡ (¬R ∨ ¬F ∨ X ∨ ¬B)
- C<sub>4</sub> ≡ (X ∨ F ∨ M)
- C<sub>5</sub> ≡ (X ∨ ¬M ∨ ¬R ∨ F)
- C<sub>6</sub> ≡ (¬F ∨ X ∨ R ∨ ¬A ∨ ¬B)
- C<sub>7</sub> ≡ ¬X

Knowledge W ≡  C<sub>1</sub> ∧ C<sub>2</sub> ∧ C<sub>3</sub> ∧ C<sub>4</sub> ∧ C<sub>5</sub> ∧ C<sub>6</sub> ∧ C<sub>7</sub>

Hypothesis H ≡ ¬(¬F ∨ X ∨ ¬B ∨ R ∨ A)

Proof that W |= H holds using the resolution method.

**Solution**:

Too proof that W |= H , show that W ∧ ¬H is not satisfiable.

¬H ≡ (¬F ∨ X ∨ ¬B ∨ R ∨ A)

C<sub>7</sub> is an atom which can resolve all X in C<sub>1</sub> - C<sub>6</sub>:

- C<sub>8</sub> ≡ C<sub>1</sub> ∧ C<sub>7</sub> → (F ∨ ¬M ∨ R)
- C<sub>9</sub> ≡ C<sub>2</sub> ∧ C<sub>7</sub> → (¬F ∨ B)
- C<sub>10</sub> ≡ C<sub>3</sub> ∧ C<sub>7</sub> → (¬R ∨ ¬F ∨ ¬B)
- C<sub>11</sub> ≡ C<sub>4</sub> ∧ C<sub>7</sub> → (F ∨ M)
- C<sub>12</sub> ≡ C<sub>5</sub> ∧ C<sub>7</sub> → (¬M ∨ ¬R ∨ F)
- C<sub>13</sub> ≡ C<sub>6</sub> ∧ C<sub>7</sub> → (¬F ∨ R ∨ ¬A ∨ ¬B)
- C<sub>14</sub> ≡ ¬H ∧ C<sub>7</sub> → (¬F ∨ ¬B ∨ R ∨ A)

Further Resolutions:

- C<sub>15</sub> ≡ C<sub>8</sub> ∧ C<sub>11</sub> → (F ∨ R)
- C<sub>16</sub> ≡ C<sub>11</sub> ∧ C<sub>12</sub> → (¬R ∨ F)
- C<sub>17</sub> ≡ C<sub>15</sub> ∧ C<sub>16</sub> → F
- C<sub>18</sub> ≡ C<sub>9</sub> ∧ C<sub>17</sub> → **B**
- C<sub>19</sub> ≡ C<sub>13</sub> ∧ C<sub>17</sub> -> (R ∨ ¬A ∨ ¬B)
- C<sub>20</sub> ≡ C<sub>14</sub> ∧ C<sub>14</sub> → (¬B ∨ R ∨ A)
- C<sub>21</sub> ≡ C<sub>20</sub> ∧ C<sub>19</sub> → (¬B ∨ R)
- C<sub>22</sub> ≡ C<sub>17</sub> ∧ C<sub>10</sub> → (¬B ∨ ¬R)
- C<sub>23</sub> ≡ C<sub>22</sub> ∧ C<sub>21</sub> → **¬B**
- C<sub>24</sub> ≡  C<sub>23</sub> ∧ C<sub>18</sub> → **()**

Therefore, W ∧ ¬H is not satisfiable and W |= H holds.

</br>

### b)

Determine whether the following formulas are satisfiable or not. If yes,
provide a model (i.e., an interpretation that satisfies the formula); if no,
prove that by applying the resolution method.

(S ∨ W) ∧ (S ∨ ¬W) ∧ (¬S ∨ W) ∧ (¬S ∨ ¬W)

**Solution**: The formula is not satisfiable:

- (S ∨ W) ∧ (S ∨ ¬W) -> S
- (¬S ∨ ¬W) ∧ (¬S ∨ W) -> ¬S
- ¬S ∨ S -> ()

(B ∨ ¬A) ∧ (¬B ∨ ¬X ∨ F) ∧ (¬Z ∨ X) ∧ (Z ∨ X ∨ P) ∧ (¬B ∨ ¬X ∨ ¬F) ∧ (Z ∨ X ∨ ¬P)

**Solution**: The formula is satisfiable. ¬B ¬A X ¬F ¬Z ¬P is a possible solution:

<pre>
B A X F Z P | (((((B V -A) ∧ ((-B V -X) V F)) ∧ (-Z V X)) ∧ ((Z V X) V P)) ∧ ((-B V -X) V -F)) ∧ ((Z V X) V -P)
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
0 0 1 0 0 0 |        1 1   1   1  1 0   1     1  1  1     1     1    1     1   1  1 0   1 1    1     1    1 1  
</pre>

## Task 2 - Unification

Unify the following pairs of clauses. First, select suitable candidates that may
be unifiable from each set, then apply the method described in the lecture.
Finally, apply the resulting substitution to the whole clause.

Hint: Imagine you are trying to apply the resolution rule. Only one literal needs to match.

{p(ƒ (X, Y), Z), q(a, X)} and {¬q(W, b), r(a, c)}

**Solution**:

- p(ƒ (X, Y), Z) cant be unified with ¬q(W, b) or r(a, c) because the predicate symbols dont match.
- q(a, X) and r(a, c) cant be unified because the predicate symbols dont match.

- S{a/W,b/X} is a unifier for ¬q(W, b) and q(a, X):

    S(q(a, X)) = q(W, X)

    S(¬q(W, b)) = ¬q(W, X)

    S(q(a, X)) = ¬S(¬q(W, b)).

- the substituted clauses are then {p(ƒ (X, Y), Z), q(W, X)} and {¬q(W, X), r(a, c)}, which have the resolvant:

    {p(ƒ (X, Y), Z),r(a, c)}

{q(ƒ (ƒ (X, Y), X)), ¬p(Z)} and {q(ƒ (ƒ (g(c), Z), g(Z)))}

- p(Z) cant be unified with q(ƒ (ƒ (X, Y), X)) because the predicate symbols dont match.

- q(ƒ (ƒ (X, Y), X)) and q(ƒ (ƒ (g(c), Z), g(Z))) are candidates for unification, but substitution of two different constants fails:

    | {q(ƒ (ƒ (X, Y), X)) =? q(ƒ (ƒ (g(c), Z), g(Z)))}| {} |
    |---|---|
    | {(ƒ (ƒ (X, Y), X) =? (ƒ (ƒ (g(c), Z), g(Z))} | {} |
    | {ƒ (X, Y) =? ƒ (g(c), Z) , X =? g(Z)}| {g(c)/X)} |
    | {Y =? Z} | ⊥ |

## Task 3 -

## Task 4 -

## Task 5 -