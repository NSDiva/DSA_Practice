''' Given an integer array nums, find a that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6. '''

# Solution 1: (Brute Force Approach) Complexity: O(n^2)

class Solution:
    # This function finds the maximum product of any contiguous subarray using brute force
    def maxProduct(self, nums):
        # Initialize the answer with the first element
        maxProd = nums[0]

        # Outer loop picks the starting index
        for i in range(len(nums)):
            # Initialize current product to 1
            prod = 1

            # Inner loop picks the ending index
            for j in range(i, len(nums)):
                # Multiply current number to product
                prod *= nums[j]

                # Update maximum product if needed
                maxProd = max(maxProd, prod)

        # Return the result
        return maxProd

# Solution 2: (Optimal Approach - 1) Complexity: O(n)

# This function returns the maximum product subarray using prefix and suffix traversal
class Solution:
    def maxProductSubArray(self, nums):
        # Store length of array
        n = len(nums)

        # Initialize prefix and suffix products
        pre, suff = 1, 1

        # Initialize answer as negative infinity
        ans = float('-inf')

        # Traverse from both front and back
        for i in range(n):
            # Reset prefix if zero
            if pre == 0:
                pre = 1

            # Reset suffix if zero
            if suff == 0:
                suff = 1

            # Multiply prefix with front element
            pre *= nums[i]

            # Multiply suffix with back element
            suff *= nums[n - i - 1]

            # Update maximum product so far
            ans = max(ans, pre, suff)

        # Return the result
        return ans

# Solution 3: (Optimal Approach - 2) Complexity: O(n)

class Solution:
    # This function returns the maximum product
    # of any contiguous subarray using optimized approach
    def maxProduct(self, nums):
        res = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        # Traverse from second element
        for i in range(1, len(nums)):
            curr = nums[i]

            # Swap max and min if current is negative
            if curr < 0:
                maxProd, minProd = minProd, maxProd

            # Update max and min product
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            # Update result
            res = max(res, maxProd)

        return res


# Sample usage
nums = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProduct(nums))
