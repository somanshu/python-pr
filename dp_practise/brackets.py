def gen_combination(brackets, result, countS, countE):
    if brackets == 0 and countE == countS:
        print("".join(result))
        return

    if countE == countS and countS > 0:
        result.append('(')
        gen_combination(brackets - 1, result, countS - 1, countE)
        result.pop(-1)
        return

    if countS > 0:
        result.append('(')
        gen_combination(brackets - 1, result, countS - 1, countE)
        result.pop(-1)

    if countE > 0:
        result.append(')')
        gen_combination(brackets - 1, result, countS, countE - 1)
        result.pop(-1)


gen_combination(6, [], 3, 3)
