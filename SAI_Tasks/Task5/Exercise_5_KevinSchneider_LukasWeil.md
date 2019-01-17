# Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347)  # Introduction to Symbolic AI  Tasks WS 2018/19

Kevin Schneider (389667)  
Heinrich Lukas Weil (389347)  

## Task 1 -
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

## Task 2 -

## Task 3 -
![Task3](pics/Task3.png)
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