# Move weighting scale alternate under given constraints
# https://www.geeksforgeeks.org/move-weighting-scale-alternate-given-constraints/


def weighing(diff, prevWt, weights, steps, path):
    if steps == 0:
        return path

    for w in weights:
        if w != prevWt and w > diff:
            path.append(w)
            res = weighing(w - diff, w, weights, steps - 1, path)
            if res != None:
                return res
            path.pop(-1)

    return None


weights = [2, 3, 5, 6]
steps = 10
path = []
res = weighing(0, None, weights, steps, path)
print(res)
