def median(x):
    sorted_x = sorted(x)
    midpoint = len(x) // 2
    if len(x) % 2:
        return sorted_x[midpoint]
    else:
        return (sorted_x[midpoint]+sorted_x[midpoint-1])/2       


assert median([1]) == 1
assert median([1, 2]) == 1.5
assert median([1, 2, 3]) == 2
assert median([3,1,2]) == 2
assert median([3,1,4,2]) == 2.5

n = 9 #int(input())
arr = [3,7,8,5,12,14,21,13,18] #[int(v) for v in input().split()]
q2 = median(arr)
q1 = median([xi for xi in arr if xi < q2])
q3 = median([xi for xi in arr if xi > q2])
print(int(q1))
print(int(q2))
print(int(q3))
