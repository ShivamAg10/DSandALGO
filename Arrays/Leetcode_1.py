class Solution:
    def twoSum(self, nums, target: int):
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i, h[y]]

# Time Complexity: O(n)
# Space Complexity: O(n)