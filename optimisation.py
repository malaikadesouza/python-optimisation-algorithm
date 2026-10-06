def compute_prefix_sum(A):
    prefix = [0]
    total = 0
    for x in A:
        total += x
        prefix.append(total)
    return prefix


def solve(n, k, A):
    prefix = compute_prefix_sum(A)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    cut = [[-1] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for length in range(1, n + 1):
        for groups in range(1, min(k, length) + 1):
            for last_cut in range(groups - 1, length):
                group_sum = prefix[length] - prefix[last_cut]
                total_cost = dp[last_cut][groups - 1] + group_sum ** 2
                if total_cost < dp[length][groups]:
                    dp[length][groups] = total_cost
                    cut[length][groups] = last_cut

    # reconstruct cuts
    cuts = [0] * (k + 1)
    i = n
    for g in range(k, 0, -1):
        cuts[g] = i
        i = cut[i][g]
    cuts[0] = 0

    return dp[n][k], cuts

# To read input
n = int(input())
k = int(input())
A = []
for i in input().split():
    A.append(int(i))

# Solving
cost, cuts = solve(n, k, A)
print(cost)
print(cuts)



# Code Description
#
# Finds prefix sums of array A in a single go -> gets the sum of any subarray in constant time.
# DP to find  min cost of dividing A into k adjacent groups (cost of a group = sum^2.
# Fill DP table, where dp[i][g] is min cost to split the first i elements into g groups.
# Each entry tries all valid cut positions and picks  one with the lowest cost.
# Will store the best cut in a cut table.
# Lastly, backtrack using cut table to reconstruct the positions of the cuts.



# Time Complexity Analysis
#
# n = length of input array A
# k = number of groups to split A into
#
# Computing prefix sums -> O(n)
# DP loop:
#   Outer loop for length (1 to n) -> O(n)
#   Middle loop for groups (1 to k) -> O(k)
#   Inner loop for last_cut (up to n) -> O(n)
#   Total time complexity of DP: O(n * k * n) = O(n^2 k)
# Reconstructing cut positions -> O(k)
# Overall time complexity -> O(n^2 k)



