''' Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6] '''

# Solution 1: (Brute Force) Complexity: O(n^2)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            output.append(product)
        return output

# Solution 2: (Prefix and Suffix Product) Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        pre = [0] * n
        suff = [0] * n
        pre[0] = 1
        suff[n - 1] = 1
        
        # Calculate prefix products
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
            
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
            
        # Multiply prefix and suffix products to get the result
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i] * suff[i]
            
        return ans

# Solution 3: (Using Left and Right Product Arrays) Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        left_Product = [0] * n
        right_Product = [0] * n
        
        left_Product[0] = 1
        for i in range(1, n):
            left_Product[i] = left_Product[i-1] * nums[i-1]
            
        right_Product[n-1] = 1
        for i in range(n-2, -1, -1):
            right_Product[i] = right_Product[i+1] * nums[i+1]
            
        for i in range(n):
            ans[i] = left_Product[i] * right_Product[i]
            
        return ans

if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
