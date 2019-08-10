# Assembly Line Scheduling
# 1. Two assembly lines, 1 and 2, each with stations from 1 to n.
# 2. A car chassis must pass through all stations from 1 to n
# 	 in order(in any of the two assembly lines). i.e. it cannot jump from station i to station j
#    if they are not at one move distance.
# 3. The car chassis can move one station forward in the same line, or one station diagonally in the other line.
#    It incurs an extra cost ti, j to move to station j from line i. No cost is incurred for movement in same line.
# 4. The time taken in station j on line i is ai, j.
# 5. Si, j represents a station j on line i.


def get_min_time(cur_station, cur_line, a, t, e, x, mem):
    last_station = len(a[0]) - 1

    if cur_station == last_station:
        return a[cur_line][cur_station] + x[cur_line]

    if mem[cur_line][cur_station] != 0:
        return mem[cur_line][cur_station]

    time = 0

    if cur_station == 0:
        time += e[cur_line]

    time += a[cur_line][cur_station]

    # same line
    t1 = time + get_min_time(cur_station + 1, cur_line, a, t, e, x, mem)

    # switch line
    newline = 0 if cur_line == 1 else 1
    t2 = time + t[cur_line][cur_station + 1] + \
        get_min_time(cur_station + 1, newline, a, t, e, x, mem)

    mem[cur_line][cur_station] = min(t1, t2)
    return mem[cur_line][cur_station]


def carAssembly(a, t, e, x):

    NUM_STATION = len(a[0])
    T1 = [0 for i in range(NUM_STATION)]
    T2 = [0 for i in range(NUM_STATION)]

    T1[0] = e[0] + a[0][0]  # time taken to leave
    # first station in line 1
    T2[0] = e[1] + a[1][0]  # time taken to leave
    # first station in line 2

    # Fill tables T1[] and T2[] using
    # above given recursive relations
    for i in range(1, NUM_STATION):
        T1[i] = min(T1[i-1] + a[0][i],
                    T2[i-1] + t[1][i] + a[0][i])
        T2[i] = min(T2[i-1] + a[1][i],
                    T1[i-1] + t[0][i] + a[1][i])

    # consider exit times and return minimum
    return min(T1[NUM_STATION - 1] + x[0],
               T2[NUM_STATION - 1] + x[1])


a = [
    [4, 5, 3, 2],
    [2, 10, 1, 4]
]
t = [
    [0, 7, 4, 5],
    [0, 9, 2, 8]
]
e = [10, 12]
x = [18, 7]
mem = [[0 for i in range(len(a[0]))] for j in range(2)]

t1 = get_min_time(0, 0, a, t, e, x, mem)
t2 = get_min_time(0, 0, a, t, e, x, mem)


print(min(t1, t2))
print(carAssembly(a, t, e, x))
