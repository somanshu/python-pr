def climb_stairs(n, res):
    if n < 0:
        return

    if n == 0:
        print(res)
        return

    res.append(1)
    climb_stairs(n-1, res)
    res.pop(-1)
    res.append(2)
    climb_stairs(n-2, res)
    res.pop(-1)


climb_stairs(4, [])
