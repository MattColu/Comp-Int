# Computational Intelligence
## Lab2: Set Covering with Evolutionary Algorithms

I based my approach on the Professor's implementation of the one-max algorithm

### Implementation
The details for each step are explained in the notebook.
Other than what was included in the Professor's implementation, I've included an early stopping criterion, according to which the `evolution` function is exited if the best Individual hasn't changed for $ {total \# of generations} \over 10 $ generations.

### Results
- Solution for N = 5:
    - Elements: 5

- Solution for N = 10:
    - Elements: 10

- Solution for N = 20:
    - Elements: 26

- Solution for N = 100:
    - Elements: 201