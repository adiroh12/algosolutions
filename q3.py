#1

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    if amount != 0:
        return -1  
    return count

def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 6, 10]
amount = 12
print(greedy_coin_change(coins, amount))  #חמדני

print(dp_coin_change(coins, amount))  #אופטימלי



#2

def minimize_penalty(w, L):
    n = len(w)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0  

    for i in range(n - 1, -1, -1):
        line_length = 0
        for j in range(i, n):
            line_length += w[j]
            if j > i:
                line_length += 1
            if line_length > L:
                break
            penalty = L - line_length
            dp[i] = min(dp[i], penalty + dp[j + 1])

    return dp[0]
    
    
w = [3, 2, 2, 5]
L = 6
print(minimize_penalty(w, L))
