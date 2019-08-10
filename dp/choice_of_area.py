# Choice of area
# Initial value of Power A = 20
# Initial value of Power B = 8

# Area X (3, 2) : If you step into Area X,
#                 A increases by 3,
#                 B increases by 2

# Area Y (-5, -10) : If you step into Area Y,
#                    A decreases by 5,
#                    B decreases by 10

# Area Z (-20, 5) : If you step into Area Z,
#                   A decreases by 20,
#                   B increases by 5

# It is possible to choose any area in our first step.
# We can survive at max 5 unit of time by following
# these choice of areas :
# X -> Z -> X -> Y -> X


class area():
    def __init__(self, a, b):
        self.a = a
        self.b = b


def get_survive(a, b, prev, x, y, z, memory):
    if a <= 0 or b <= 0:
        return ''

    curr = area(a, b)

    if curr in memory.keys():
        return memory[curr]

    if prev == x:
        res1 = 'Y' + get_survive(a + y.a, b + y.b, y, x, y, z, memory)
        res2 = 'Z' + get_survive(a + z.a, b + z.b, z, x, y, z, memory)

        sol = res1 if len(res1) > len(res2) else res2
        key = area(a, b)
        memory[key] = sol
        return sol

    if prev == y:
        res1 = 'X' + get_survive(a + x.a, b + x.b, x, x, y, z, memory)
        res2 = 'Z' + get_survive(a + z.a, b + z.b, z, x, y, z, memory)

        sol = res1 if len(res1) > len(res2) else res2
        key = area(a, b)
        memory[key] = sol
        return sol

    if prev == z:
        res1 = 'X' + get_survive(a + x.a, b + x.b, x, x, y, z, memory)
        res2 = 'Y' + get_survive(a + y.a, b + y.b, y, x, y, z, memory)

        sol = res1 if len(res1) > len(res2) else res2
        key = area(a, b)
        memory[key] = sol
        return sol

    res1 = 'X' + get_survive(a + x.a, b + x.b, x, x, y, z, memory)
    res2 = 'Y' + get_survive(a + y.a, b + y.b, y, x, y, z, memory)
    res3 = 'Z' + get_survive(a + z.a, b + z.b, z, x, y, z, memory)

    if len(res1) > len(res2) and len(res1) > len(res3):
        key = area(a, b)
        memory[key] = res1
        return res1

    if len(res2) > len(res3):
        key = area(a, b)
        memory[key] = res2
        return res2

    key = area(a, b)
    memory[key] = res3
    return res3


x = area(3, 2)
y = area(-5, -10)
z = area(-20, 5)
a = 20
b = 8
memory = dict()
print(get_survive(a, b, None, x, y, z, memory))
