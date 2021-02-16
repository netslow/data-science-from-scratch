def median(x):
    sorted_x = sorted(x)
    midpoint = len(x) // 2
    if len(x) % 2:
        return sorted_x[midpoint]
    else:
        return (sorted_x[midpoint]+sorted_x[midpoint-1])/2       

def split_half(li):
    sorted_li = sorted(li)
    midpoint = len(li) // 2
    if len(li) % 2:
        return (sorted_li[:midpoint], sorted_li[midpoint+1:])
    else:
        return (sorted_li[:midpoint], sorted_li[midpoint:])


assert split_half([1,2,3]) == ([1], [3])
assert split_half([4, 3, 1, 2]) == ([1,2], [3,4])

n = int(input())
X = [int(x) for x in input().split()]
F = [int(f) for f in input().split()]
# n = 20
# X = [int(x) for x in "6 12 8 10 20 16".split()]
# X = [int(x)
    #  for x in "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10".split()]
# F = [int(f) for f in "5 4 3 2 1 5".split()]
# F = [int(f)
    #  for f in "1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20".split()]

arr = [xi for x, f in zip(X,F) for xi in [x] * f ]
assert len(arr) == sum(F)

sorted_arr = sorted(arr)
q2 = median(arr)
left, right = split_half(sorted_arr)
q1 = median(left)
q3 = median(right)
inquartile_range = q3 - q1
print("{:.1f}".format(inquartile_range))





