''' Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3. '''

# Solution 1: (Brute Force) Complexity: O(n^2)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

# Solution 2: (Sorting) Complexity: O(n log n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False

# Solution 3: (Hash Set) Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Solution 4: (Hash Map) Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

if __name__ == "__main__":
      print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
      print(Solution().containsDuplicate([1, 2, 3, 4]))  # False