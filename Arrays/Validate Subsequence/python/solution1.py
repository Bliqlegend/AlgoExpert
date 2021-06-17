# O(n) time complexity
def isValidSubsequence(array, sequence):
    # Write your code here.
	arid = 0
	sid = 0
	while arid < len(array) and sid < len(sequence):
		if array[arid] ==  sequence[sid]:
			sid+=1
		arid +=1
	return sid == len(sequence)
		