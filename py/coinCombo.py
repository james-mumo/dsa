def count_coin_change_ways(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: one way to make amount 0 (by choosing no coins)

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[amount]


# Example usage for making 20 cents with denominations {1c, 2c, 5c}
amount = 20
coins = [1, 2, 5]
ways = count_coin_change_ways(amount, coins)
print(f"Number of ways to make {amount} cents with {coins}: {ways}")
