def PrimeList(N):
    # 1. 处理边界情况：小于2的数没有质数，直接返回空字符串
    if N <= 2:
        return ""
    # 2. 初始化筛子：is_prime是长度为N的列表，True表示初始认为是质数，False为非质数
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数，提前标记
    # 3. 执行筛法：从最小质数2开始，标记其所有倍数为非质数
    for i in range(2, int(N ** 0.5) + 1):  # 只需遍历到N的平方根，后续非质数已被标记
        if is_prime[i]:  # 若i是质数，标记i的倍数（从i²开始，避免重复标记）
            is_prime[i*i : N : i] = [False] * len(is_prime[i*i : N : i])
    # 4. 提取质数并格式化：筛选出is_prime中为True的索引（即质数），转为字符串后用空格连接
    prime_list = [str(num) for num, flag in enumerate(is_prime) if flag]
    return " ".join(prime_list)
