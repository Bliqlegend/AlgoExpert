def OtwoNumberSum(arr,ts):
    o = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == ts and arr[i]!=arr[j]:
                return [arr[i],arr[j]]
    return []

def twoNumberSum(arr,ts):
    nums = {}
    for num in arr:
        match = abs(ts - num)
        if match in nums:
            return [num,match]
        nums[num] = True
    return []

arr = [int(ele) for ele in input().split()]
ts = int(input())
o = twoNumberSum(arr,ts)
print(o)
