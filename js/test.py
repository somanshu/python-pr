def josephus(n, k):

    if (n == 1):
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        val = (josephus(n - 1, k) + k-1) % n + 1
        return val

# Driver Program to test above function


n = 5
k = 2

print("The chosen place is ", josephus(n, k))
