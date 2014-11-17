if __name__ == "__main__":
    limit = 10**5
    T = 10**6
    partitions = [1]+[0]*limit
    for k in range(1, limit+1):
        for n in range(k, limit+1):
            partitions[n] += partitions[n-k]
        if partitions[k] % T == 0:
            print("PE78 Ans: %d" % k)
            break