def productSum(arr):
    depth = 1
    for i in range(len(arr)):
        if type(arr[i]) != int:
            depth+=1
    return depth

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
d = productSum(arr)
print(d)
