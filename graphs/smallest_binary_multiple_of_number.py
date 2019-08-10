# Find the smallest binary digit multiple of given number
# https://www.geeksforgeeks.org/find-the-smallest-binary-digit-multiple-of-given-number/


def getSmallestBinary(number):
    string = '1'
    queue = []
    queue.append(string)

    while len(queue) > 0:
        s = queue.pop(0)

        if int(s) % number == 0:
            return s

        queue.append(s+'0')
        queue.append(s+'1')


n = 21

res = getSmallestBinary(n)
print(res)
