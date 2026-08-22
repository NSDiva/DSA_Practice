''' There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4 '''

# Solution 1: (Brute Force Approach) Complexity: O(n)

class Solution:
    # Function to search target in rotated sorted array using brute force
    def search(self, nums, target):

        # Loop through each element in the array
        for i in range(len(nums)):

            # If current element matches target, return index
            if nums[i] == target:
                return i

        # If not found, return -1
        return -1

# Solution 2: (Optimal Approach) Complexity: O(log n)

class Solution:
    # Function to search target in rotated sorted array using binary search
    def search(self, nums, target):
        # Set initial search space
        low = 0
        high = len(nums) - 1

        # Run loop while valid search space exists
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If target found at mid, return index
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # If target lies in left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1


# Driver code
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

obj = Solution()
index = obj.search(nums, target)

print(index)
