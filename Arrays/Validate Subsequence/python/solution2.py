
# O(n) time complexity

def isValidSubsequence(array, sequence):
        # Write your code here.
        seqID = 0
        for num in array:
            if seqID == len(sequence):
                break
            if num == sequence[seqID]:
                seqID+=1
        return seqID == len(sequence)
