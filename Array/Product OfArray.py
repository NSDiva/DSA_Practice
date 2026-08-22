''' Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6] '''

# Solution 1: (Brute Force Approach) Complexity: O(n^2)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    ans[i] *= nums[j]
        return ans

# Solution 2: (Better Approach) Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = [1] * n
        
        # Fill the left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            
        # Fill the right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            
        # Construct the final answer
        for i in range(n):
            ans[i] = left[i] * right[i]
        
        return ans

# Solution 3: (Optimal Approach) Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Pass 1: Calculate left products directly into ans
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
            
        # Pass 2: Calculate right products on the fly and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
            
        return ans

if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]