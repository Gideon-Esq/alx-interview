def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        """ Precompute the prime numbers up to max_num using Sieve of Eratosthenes. """
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_num**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_num + 1, i):
                    primes[j] = False
        return primes

    def count_prime_moves(n, primes):
        """ Count the number of valid prime moves for a given n. """
        count = 0
        visited = [False] * (n + 1)
        for i in range(2, n + 1):
            if primes[i] and not visited[i]:
                count += 1
                for j in range(i, n + 1, i):
                    visited[j] = True
        return count

    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
