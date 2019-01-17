# Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347) 

## Task 1 - Water Jug Problem

The image below describes the water jug problem from the lecture. Its goal is
to get from the initial state (S, both jugs empty) to the final state (Z, 2 gallons
of water in the large jug and small jug empty) by applying a chain of allowed
actions (transitions).

![Task1](pics/Task1.png)

(a) Formally define the state space K of the problem give and give S, Z ∈ K.
Assume that jugs can only hold  ∈ N0 gallons up to their capacity.
(b) Formally define all unambiguous transitions as mathematical functions
(i.e., ". . . pour some water . . . " has multiple outcomes, so it cannot be
defined as a function). It should also not be possible to apply transitions
that don’t alter the current state (like emptying an empty jug). Specify the
applicable value range for each function as cases with appropriate conditions, e.g.:

_e_<sub>4</sub>(x,y)= { (0,y), if x<0 (empty)

(a)

	x = amount of water in the 4-Gallons jug

	y = amount of water in the 3-Gallons jug

	K = (x,y) | x ? {0, 1,2,3,4}, y ? {0,1,2,3}

	S = (0,0)

	Z = (2,0)

(b)

	f3(x,y) = {(x, 3), if y < 3 (fill 3G)
	f3(x,y) = {(4, y), if x < 4 (fill 4G)
	e3(x,y) = {(x, 0), if y > 0 (empty 3G)
	e4(x,y) = {(0, y), if x > 0 (empty 4G)

## Task 2 - Search complexity

Theoretical analysis can be very useful to choose the best search method
given the constraints of a specific application and environment.
a) Define "optimal" and "complete" in the context of search methods.
b) Explain why the following statements hold:
    * Breadth-First Search (BFS) has exponential space complexity in depth.
    * Depth-First Search (DFS) is not optimal and not complete, but Iterative
Deepening DFS (IDS) is.
c) Give formulas based on depth d and branching factor b of a regular tree
for the worst-case number of nodes visited by BFS and IDS. What is the
overhead of IDS over BFS?

## Task 3 -

The following search tree is given.

![Task3](pics/Task3.png)

a) Find S and V. List the sequence of nodes visited along the way using:
 Breadth-First Search (BFS)
 Depth-First Search (DFS)
 Iterative Deepening Depth-First Search (IDS)
b) What is the outcome of Limited Depth-First Search for different limits?

## Task 4 -

The following map is given. Paths are bidirectional

![Task4](pics/Task4.png)

a) Use the A* search algorithm to find the lowest-cost route from node A to J,
with traversal costs on the map as actual cost and euclidean distance for
estimated remaining cost. Create a search tree in the following notation:

    ![Task4.2](pics/Task4.2.png)

    B marks the node. (1) is the sequence number. Numbers from top to bottom are: traversal cost up to this point, estimated remaining cost, combined cost.
    When you reach a node that is already in the tree and it is not cheaper to
    reach now, mark this new node with × in place of a sequence number and
    ignroe it.

b) Give the optimal path from A to J with total traversal cost.

## Task 5 -

see "Exercise_5_KevinSchneider_LukasWeil.py"