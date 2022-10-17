# Computational Intelligence
## Lab1: Set Covering

I based my approach on the Professor's implementation of the generic search algorithm

### Implementation
The details for each step are explained in the notebook. Most notably the cost function takes into account how many repetitions would be introduced by the evaluated choice, but its application differs from the one provided by the Professor, as the cost for each state is decided entirely by the cost function, instead starting from the cost of the previous one.

### Results
- Solution for N = 5:
    - Elements: 7
    - Nodes: 28

- Solution for N = 10:
    - Elements: 11
    - Nodes: 706

- Solution for N = 20:
    - Elements: 46
    - Nodes: 751

- Solution for N = 100:
    - Elements: ?
    - Nodes: ?

- Solution for N = 500:
    - Elements: ?
    - Nodes: ?

- Solution for N = 1000:
    - Elements: ?
    - Nodes: ?

---
I know that the results are sub-optimal to say the least, but I had already devoted a decent amount of my time devising a greedy algorithm, and only subsequently decided to try this search based algorithm.
