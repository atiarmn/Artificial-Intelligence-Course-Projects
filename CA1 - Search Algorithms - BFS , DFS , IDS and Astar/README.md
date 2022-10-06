# Search Algorithms Project

## Objective:
To design and compare the performance of informed and uninformed search algorithms such as BFS, IDS, A-star and Weighted A-star in a simulation of the Snake game.

## Implementation:
In this project, we simulated a snake game in which a snake with an initial body length of 1 was supposed to find the most efficient path to eat all the seeds in the game table using Python programming language. The game environment information -such as table dimensions, snake's initial location, seeds location and their score (can be 1 or 2, and seeds with a score of 2 should be eaten twice)- are described by the user in a sample input file.  
  
These are some basic rules of this game:  
* The snake will grow from its tail side by eating the seeds.
* The snake cannot collide with its own body. In other words, moving in such a direction wouldn't be considered a possible move. 
* There are no barriers on the game table. The snake will enter from the opposite side of the table by exiting from one of the edges.  

After the game environment and rules being implemented, multiple search algorithms were executed and their performance were discussed by comparing their execution time, number of the visited states, **consistency and admissibility** ; BFS and IDS as uninformed search algorithms and A-star and Weighted A-star as informed search algorithms with 2 different heuristics for each of them. 
  
These heuristics were defined as follows:
* h1: the number of the seeds left uneaten in the table.
* h2: the total score of the seeds left in the table.

## Results:
An analytic comparison between these algorithms is included in the report file in Persian. The table below, which is the result of running the algorithms on test1.txt input file, can be informative enough to compare these algorithms and gain some insights about them.

![alt text]([https://github.com/moeinsh78/Artificial-Intelligence-Course-Projects/blob/master/Search/table.JPG](https://github.com/atiarmn/Artificial-Intelligence-Course-Projects/blob/master/CA1%20-%20Search%20Algorithms%20-%20BFS%20%2C%20DFS%20%2C%20IDS%20and%20Astar/result.png)

For example, the time-inefficiency of the IDS algorithm is evident due to the huge number of visited states. More importantly, it can be seen that Weighted A-star algorithm is not admissible since it has failed to find the shortest path, although it enhances the execution time significantly.
