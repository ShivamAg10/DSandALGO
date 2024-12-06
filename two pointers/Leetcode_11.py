# Container with most Water

class Solution:
    def maxArea(self, height):
        maxArea = 0
        left = 0
        right = len(height)-1

        while left < right:
            waterArea = min(height[left], height[right]) * (right - left)
            maxArea = max(waterArea, maxArea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea