def PrimeList(N):
    if N <= 2:
        return ""
    
    # 初始化一个布尔数组，初始时都认为是质数
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 0和1不是质数
    
    for current in range(2, int(N ** 0.5) + 1):
        if sieve[current]:
            # 将current的倍数标记为非质数
            sieve[current*current : N : current] = [False] * len(sieve[current*current : N : current])
    
    # 收集所有质数
    primes = [str(i) for i, is_prime in enumerate(sieve) if is_prime]
    return " ".join(primes)# 在此文件中实现 PrimeList 函数
