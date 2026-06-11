# Day 49: Dynamic Programming Basics

# Q1: Fibonacci using DP
n = int(input("Enter n: "))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print("Fibonacci:", dp[n])

print("---------------------------")

# Q2: Print Fibonacci Series using DP
n = int(input("Enter number of terms: "))

dp = [0] * n

if n > 1:
    dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print("Series:", dp)

print("---------------------------")

# Q3: Climbing Stairs
n = int(input("Enter stairs: "))

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print("Ways:", dp[n])

print("---------------------------")

# Q4: Minimum Cost Climbing Stairs
cost = [10, 15, 20]

n = len(cost)

dp = [0] * n

dp[0] = cost[0]
dp[1] = cost[1]

for i in range(2, n):
    dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

print("Minimum Cost:",
      min(dp[n - 1], dp[n - 2]))

print("---------------------------")

# Q5: House Robber Problem
houses = [2, 7, 9, 3, 1]

n = len(houses)

dp = [0] * n

dp[0] = houses[0]
dp[1] = max(houses[0], houses[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1],
                houses[i] + dp[i - 2])

print("Maximum Loot:", dp[-1])

print("---------------------------")

# Q6: Maximum Sum Subarray (Kadane's Algorithm)
arr = list(map(int, input("Enter numbers: ").split()))

current = maximum = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print("Maximum Subarray Sum:", maximum)

print("---------------------------")

# Q7: Coin Change (Minimum Coins)
coins = [1, 2, 5]

amount = int(input("Enter amount: "))

dp = [float("inf")] * (amount + 1)

dp[0] = 0

for coin in coins:

    for i in range(coin, amount + 1):
        dp[i] = min(dp[i],
                    dp[i - coin] + 1)

if dp[amount] == float("inf"):
    print("Not Possible")
else:
    print("Minimum Coins:", dp[amount])

print("---------------------------")

# Q8: Longest Increasing Subsequence
arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

dp = [1] * n

for i in range(n):

    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i],
                        dp[j] + 1)

print("LIS Length:", max(dp))

print("---------------------------")

# Q9: Count Paths in Grid
rows = int(input("Rows: "))
cols = int(input("Columns: "))

dp = [[1] * cols for _ in range(rows)]

for i in range(1, rows):

    for j in range(1, cols):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print("Total Paths:",
      dp[rows - 1][cols - 1])

print("---------------------------")

# Q10: Factorial using DP
n = int(input("Enter number: "))

dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]

print("Factorial:", dp[n])
