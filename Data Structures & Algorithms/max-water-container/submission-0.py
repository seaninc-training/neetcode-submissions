class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        for i, h in enumerate(heights):
            j = len(heights) - 1

            while i < j:
                box_w = j - i
                box_h = min(heights[i], heights[j])

                if (box_w * box_h) > max_area:
                    max_area = box_w * box_h
                else:
                    j -= 1
                    continue
        
        return max_area


