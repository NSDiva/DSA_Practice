''' You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. '''

# Solution 1: (Brute Force Approach) Complexity: O(n^2)

class Solution:
    # Function to find maximum water container
    def maxArea(self, height):
        n = len(height)
        max_area = 0

        # Loop through all pairs of lines
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate area formed by lines at i and j
                area = min(height[i], height[j]) * (j - i)
                # Update max_area if current area is larger
                max_area = max(max_area, area)

        return max_area

# Solution 2: (Optimal Approach) Complexity: O(n)

class Solution:
    # Function to find maximum water container
    def maxArea(self, height):
        n = len(height)
        max_area = 0
        left = 0
        right = n - 1

        # Use two pointers to find the maximum area
        while left < right:
            # Calculate area formed by lines at left and right pointers
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if current area is larger
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    obj = Solution()
    res = obj.maxArea(height)
    print(res)  # Output: 49