# Computational Intelligence
## Lab1: Set Covering

I opted for a Greedy approach, as (of course) I don't think it's the best one, but I wanted to see how much it could be improved with respect to the Professor's implementation.

### Implementation
The details for each step are explained in the notebook. Most notably the cost function takes into account how many repetitions would be introduced by the evaluated choice: that is the metric of evaluation for each choice except for the first one, where the **longest** list is selected instead.

### Results
- Solution for N = 5:
    - Elements: 5

- Solution for N = 10:
    - Elements: 12

- Solution for N = 20:
    - Elements: 30

- Solution for N = 100:
    - Elements: 272

- Solution for N = 500:
    - Elements: 2452

- Solution for N = 1000:
    - Elements: 4185
