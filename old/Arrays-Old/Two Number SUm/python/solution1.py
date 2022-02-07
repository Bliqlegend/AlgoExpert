
# O(n2) Time Complexity
# Using Double loop O(n2) Time Comlpexity

def twoNumberSum(array, targetSum):
	for i in range(0,len(array)):
		for j in range(i,len(array)):
			if i!=j:
				if array[i]+array[j]==targetSum:
					return [array[i],array[j]]
	return []