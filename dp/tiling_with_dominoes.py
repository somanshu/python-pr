# tiling with dominos
# formula based solution
#  A[n] = A[n-2] + 2 * B[n-1]
#  B[n] = A[n-1] + B[n-2]


def get_count(cur_row, cur_col, fill):
    rows = 2
    columns = len(fill[0]) - 1

    # when current block is filled
    if fill[cur_row][cur_col] == 1:
        # check if can go down
        if cur_row < rows:
            return get_count(cur_row + 1, cur_col, fill)

        # check if can go right
        if cur_col < columns:
            return get_count(0, cur_col + 1, fill)

        # since completely filled increase count
        return 1

    # mark this block as filled
    fill[cur_row][cur_col] = 1

    res1 = 0
    res2 = 0

    # check if can go right
    if cur_col < columns:
        newfill = [row[:] for row in fill]
        newfill[cur_row][cur_col + 1] = 1

        if cur_row < rows:
            res1 = get_count(cur_row + 1, cur_col, newfill)
        else:
            res1 = get_count(0, cur_col + 1, newfill)

    # check if can go down
    if cur_row < rows and fill[cur_row + 1][cur_col] != 1:
        newfill = [row[:] for row in fill]
        newfill[cur_row + 1][cur_col] = 1

        if cur_row + 1 < rows:
            res2 = get_count(cur_row + 2, cur_col, newfill)
        elif cur_col < columns:
            res2 = get_count(0, cur_col + 1, newfill)
        else:
            res2 = 1

    return res1 + res2


n = 20
fill = [[0 for i in range(n)] for j in range(3)]

print(get_count(0, 0, fill))
