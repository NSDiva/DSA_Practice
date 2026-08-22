''' Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
1. [4,5,6,7,0,1,2] if it was rotated 4 times.
2. [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times. '''

# Solution 1: (Brute Force Approach) Complexity: O(n)

class Solution:
    # Function to find the minimum element using linear search
    def findMin(self, nums):

        # Initialize answer with a large number
        min_val = float('inf')

        # Traverse each element
        for i in range(len(nums)):

            # Update minimum value
            min_val = min(min_val, nums[i])

        # Return the result
        return min_val

# Solution 2: (Optimal Approach) Complexity: O(log n)

class Solution:
    # Function to find the minimum element using binary search
    def findMin(self, nums):

        # Initialize low and high pointers
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:

            # Calculate mid index
            mid = low + (high - low) // 2

            # Check which half to discard
            if nums[mid] > nums[high]:

                # Minimum lies in right half
                low = mid + 1

            else:

                # Minimum lies in left half (including mid)
                high = mid

        # Return the minimum element
        return nums[low]

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)
