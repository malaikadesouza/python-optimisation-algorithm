# Python Optimisation Algorithm

A dynamic-programming solution to a constrained optimisation problem, implemented in Python.

## Overview

This project implements an algorithm for partitioning an array of integers into a specified number of adjacent groups while minimising the total cost of the partition.

The cost of each group is defined as the square of the sum of its elements. The algorithm determines both the minimum achievable cost and the positions at which the array should be partitioned.

## Approach

The solution uses dynamic programming to break the optimisation problem into smaller subproblems.

Key techniques include:

- **Prefix sums** to calculate the sum of any subarray in constant time.
- **Dynamic programming (tabulation)** to calculate the minimum cost for partitioning the first `i` elements into `g` groups.
- **Backtracking** through a separate cut table to reconstruct the optimal partition positions.

For each state, the algorithm evaluates the possible position of the previous partition and retains the one producing the lowest total cost.

## Complexity Analysis

Let:

- `n` be the number of elements in the input array.
- `k` be the required number of groups.

Prefix sums are calculated in `O(n)` time.

The dynamic-programming stage considers up to `n` elements, `k` groups and `n` possible previous partition positions, resulting in a time complexity of:

`O(n²k)`

Reconstructing the optimal partition requires `O(k)` time.

The overall time complexity is therefore **O(n²k)**.

## Running the Program

The program expects:

1. The number of elements, `n`.
2. The number of groups, `k`.
3. The array elements as space-separated integers.

Example input:

```text
5
2
1 2 3 4 5
```

Run the program using:

```bash
python optimisation.py
```

The program outputs the minimum partition cost followed by the optimal cut positions.
