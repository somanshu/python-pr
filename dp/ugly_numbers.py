def ugly_number(n):
    u = [0] * n
    u[0] = 1

    i2 = i3 = i5 = 0
    multiple_of_2 = 2
    multiple_of_3 = 3
    multiple_of_5 = 5

    for i in range(1, n):
        u[i] = min(multiple_of_2, multiple_of_3, multiple_of_5)

        if u[i] == multiple_of_2:
            i2 += 1
            multiple_of_2 = u[i2] * 2

        if u[i] == multiple_of_3:
            i3 += 1
            multiple_of_3 = u[i3] * 3

        if u[i] == multiple_of_5:
            i5 += 1
            multiple_of_5 = u[i5] * 5

    return u[-1]


print(ugly_number(150))
