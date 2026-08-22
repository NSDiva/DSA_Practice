''' Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3. '''

# Solution 1: (Brute Force Approach) Complexity: O(n^2)

# Function to check for duplicates in array
def containsDuplicate(nums):
    # Loop through each element
    for i in range(len(nums)):
        # Compare with all future elements
        for j in range(i + 1, len(nums)):
            # If duplicate found
            if nums[i] == nums[j]:
                return True
    return False

# Solution 2: (Better Approach) Complexity: O(n log n)

# Function to check for duplicates using sorting
def containsDuplicate(nums):
    # Sort the list to bring duplicates together
    nums.sort()

    # Compare each element with its previous
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True  # Duplicate found

    return False  # No duplicates

# Solution 3: (Optimal Approach) Complexity: O(n)

# Function to check for duplicates using set
def containsDuplicate(nums):
    # Store unique elements in a set
    unique = set(nums)

    # If set has fewer elements, duplicates existed
    return len(unique) < len(nums)


# Sample input
nums = [1, 2, 3, 1]

# Call function and print result
res = containsDuplicate(nums)
print("true" if res else "false")
