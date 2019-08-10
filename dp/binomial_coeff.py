def binomial_coeff(n, k):
    c = [0 for i in range(n+1)]
    c[0] = 1

    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    for i in range(1, n+1):
        j = min(i, k)

        while j > 0:
            c[j] = c[j] + c[j-1]
            j -= 1

    return c[k]


def binomial_coeff_2(n, k, bc):
    if k > n:
        return 0

    if bc[n][k] > 0:
        return bc[n][k]

    if k == 0 or k == n:
        bc[n][k] = 1
        return 1

    bc[n][k] = binomial_coeff_2(n-1, k-1, bc) + binomial_coeff_2(n-1, k, bc)
    return bc[n][k]


bc = [[0 for i in range(3)] for j in range(5)]
print(binomial_coeff_2(4, 2, bc))
