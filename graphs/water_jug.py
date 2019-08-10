# 2 jugs and make a quantity using them
# Operations
# 1. Fill
# 2. Empty
# 3. Pour


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


def water_jug(x, y, maxX, maxY, d, visited):
    if x == d or y == d:
        return [Point(x, y)]

    if visited[Point(x, y)]:
        return None

    visited[Point(x, y)] = True

    res = None

    # fill x
    if x != maxX:
        res = water_jug(maxX, y, maxX, maxY, d, visited)

        if res != None:
            res.append(Point(x, y))
            return res

    # fill y
    if y != maxY:
        res = water_jug(x, maxY, maxX, maxY, d, visited)

        if res != None:
            res.append(Point(x, y))
            return res

    # empty x
    if x != 0:
        res = water_jug(0, y, maxX, maxY, d, visited)

        if res != None:
            res.append(Point(x, y))
            return res

    # empty y
    if y != 0:
        res = water_jug(x, 0, maxX, maxY, d, visited)

        if res != None:
            res.append(Point(x, y))
            return res

    # pour x into y
    if x > 0 and y < maxY:
        if x >= maxY - y:
            res = water_jug(x + y - maxY, maxY, maxX, maxY, d, visited)

            if res != None:
                res.append(Point(x, y))
                return res
        else:
            res = water_jug(0, y + x, maxX, maxY, d, visited)

            if res != None:
                res.append(Point(x, y))
                return res

    # pour y into x
    if y > 0 and x < maxX:
        if y >= maxX - x:
            res = water_jug(maxX, x + y - maxX, maxX, maxY, d, visited)

            if res != None:
                res.append(Point(x, y))
                return res
        else:
            res = water_jug(x + y, 0, maxX, maxY, d, visited)

            if res != None:
                res.append(Point(x, y))
                return res

    return None


maxX = 4
maxY = 3
d = 2
visited = {}
for i in range(maxX + 1):
    for j in range(maxY + 1):
        visited[Point(i, j)] = False

res = water_jug(0, 0, maxX, maxY, d, visited)
for point in res:
    print(f"({point.x}, {point.y})", end='\n')
