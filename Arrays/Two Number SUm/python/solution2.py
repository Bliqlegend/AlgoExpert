# Using Dictionary O(n) Time Complexity
def twoNumberSum(array, targetSum):
        # Write your code here.
        nums = {}
        for num in array:
            match = targetSum - num
            if match in nums:
                return [match,num]
            else:
                nums[num] = True
        return []
