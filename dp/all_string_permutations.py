# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/


def createString(strInp, index, visited, per):
    if len(per) == len(strInp):
        print(per)
        return

    visited[index] = True

    for i in range(len(strInp)):
        if not visited[i]:
            createString(strInp, i, visited, per + strInp[i])

    visited[index] = False


def permute(strInp):
    visited = [False for i in range(len(strInp))]

    for i in range(len(strInp)):
        createString(strInp, i, visited, strInp[i])


strInp = 'ABC'
permute(strInp)
