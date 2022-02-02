def isAnagram(str1, str2) :
    # write your code
    if len(str1) != len(str2):
        return False
    for i in sorted(str1):
        if i not in str2:
            return False
    for i in sorted(str2):
        if i not in str1:
            return False
    return True


def groupAnagrams(arr):
    flag = 0
    map = {}
    for i in arr:
        map[i] = 0
    o = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] != arr[j]:
                if isAnagram(arr[i],arr[j]):
                    o.append([arr[i],arr[j]])
                    map[arr[i]] = 1
                    map[arr[j]] = 1
    for i in arr:
        if map[i]!=1:
            o.append([i])
    return o

arr = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
o = groupAnagrams(arr)
print(o)