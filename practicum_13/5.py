def primes_less_than_n(n: int) -> set[int]:
    numbers = set(range(2, n))
    for i in range(2, int(n**0.5) + 1):
        if i in numbers:
            multiples = set(range(i*i, n, i))
            numbers -= multiples

    return numbers


print(primes_less_than_n(30))
