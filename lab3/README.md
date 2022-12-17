# Computational Intelligence

## Lab3: Nim

by Matteo Colucci (@MattColu) and Francesco Carlucci (@Francesco-Carlucci)

## 3.1: Expert System

An agent that plays with the optimal mathematical strategy, using nimsum.

## 3.2: Genetic Algorithm for Nim

The genetic algorithm generates rule-based agents combining 3 triples, each composed of one random element from each pool:
- Conditions (when to apply the rule)
- Places (on which heap to operate)
- Actions (how many elements to take)

Fitness is the win ratio against a purely random player. To check the correctness of the algorithm we introduced condition,
action and place of the expert system in the respective pools, and it did eventually converge to a nimsum agent. Without the xor operator, only by
combining our rules, it achieves a ~85% win ratio against a random agent.

Results:
Solution : genome=\[('even_elems', 'half', 'most'), ('odd_stacks', 'half', 'most'), ('even_stacks', 'all', 'most')] (fitness=87.8%)

## 3.3: MinMax

An implementation of the minmax algorithm for Nim. It's able to exhaustively solve the game up to
a size of 5 using alfa-beta pruning. For bigger sizes, at a configurable depth it starts exploiting random 
sampling, evaluating only a fraction of the possible branches.

## 3.4 Reinforcement Learning

A reinforcement learning strategy for Nim. It learns from multiple games classifying each state
in the game with a reward.
