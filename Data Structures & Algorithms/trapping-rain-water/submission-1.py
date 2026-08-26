class Solution:
    def trap(self, height: List[int]) -> int:
        # min(lmax, rmax) - array[ i ] * 1
        n = len(height)
        left = 0
        right = n - 1
        lmax, rmax, water = 0, 0, 0

        while left < right:
            if height[left] < height[right]:
                lmax = max(lmax, height[left])
                water += (lmax - height[left])
                left += 1
            else:
                rmax = max(rmax, height[right])
                water += (rmax - height[right])
                right -= 1
        
        return water


