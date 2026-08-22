''' Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter. '''

# Solution 1: (Brute Force Approach) Complexity: O(n^3 log(no. of unique triplets))

# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Store unique triplets
        st = set()

        # First loop for first element
        for i in range(n):
            # Second loop for second element
            for j in range(i + 1, n):
                # Third loop for third element
                for k in range(j + 1, n):
                    # If triplet sum is zero
                    if arr[i] + arr[j] + arr[k] == 0:
                        # Store sorted triplet to avoid duplicates
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        st.add(triplet)

        # Convert set to list of lists
        return [list(triplet) for triplet in st]

# Solution 2: (Better Approach) Complexity: O(n^2 log(no. of unique triplets))

# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Store unique triplets
        ans = set()

        # First loop for first element
        for i in range(n):
            # Set to store elements seen in this iteration
            hashset = set()

            # Second loop for second element
            for j in range(i + 1, n):
                # Calculate third element needed
                third = -(arr[i] + arr[j])

                # If third already in set, we found a triplet
                if third in hashset:
                    triplet = tuple(sorted([arr[i], arr[j], third]))
                    ans.add(triplet)

                # Add current element to set
                hashset.add(arr[j])

        # Convert set to list of lists
        return [list(triplet) for triplet in ans]

# Solution 3: (Optimal Approach) Complexity: O(n log n) + O(n^2)

# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Sort the array
        arr.sort()
        # Store final result
        ans = []

        # First loop for first element
        for i in range(n):
            # Skip duplicates for first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Two pointers
            left, right = i + 1, n - 1

            # Find pairs for current arr[i]
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans


# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)
