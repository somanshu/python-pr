# https://www.geeksforgeeks.org/painting-fence-algorithm/
# Given n posts and k colors
# diff = no of ways when color of last
#         two posts is different
#  same = no of ways when color of last
#         two posts is same
#  total ways = diff + sum

# for n = 1
#     diff = k, same = 0
#     total = k

# for n = 2
#     diff = k * (k-1) //k choices for
#            first post, k-1 for next
#     same = k //k choices for common
#            color of two posts
#     total = k +  k * (k-1)

# for n = 3
#     diff = [k +  k * (k-1)] * (k-1)
#            (k-1) choices for 3rd post
#            to not have color of 2nd
#            post.
#     same = k * (k-1)
#            c'' != c, (k-1) choices for it

# Hence we deduce that,
# total[i] = same[i] + diff[i]
# same[i]  = diff[i-1]
# diff[i]  = (diff[i-1] + diff[i-2]) * (k-1)
#          = total[i-1] * (k-1)


# solution 1
def get_paint_count(n, k):
    total = k
    same, diff = 0, k

    for i in range(2, n+1):
        same = diff
        diff = total * (k - 1)
        total = same + diff

    return total


# solution 2
def get_paint_count2(n, k, av_k, isSameAsPrev):
    if n <= 0:
        return 1

    if n == 1:
        return av_k

    res1, res2 = 0, 0

    if isSameAsPrev:
        return get_paint_count2(n-1, k, k-1, False)

    res1 = av_k * get_paint_count2(n-1, k, 1, True)
    res2 = av_k * get_paint_count2(n-1, k, k-1, False)
    return res1 + res2


print(get_paint_count(5, 6))
print(get_paint_count2(5, 6, 6, False))
