if __name__ == '__main__':
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    val = 200
    # Dynamic Programming :-)
    ways = [1] + [0]*val
    for coin in coins:
        for i in range(coin, 201, 1):
                ways[i] += ways[i-coin]
    print(ways[val])
