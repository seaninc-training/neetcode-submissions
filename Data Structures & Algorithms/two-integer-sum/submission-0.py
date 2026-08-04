class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = {}

        for i, num in enumerate(nums):
            num2 = target - num

            if num2 in viewed:
                return [viewed[num2], i]
            
            viewed[num] = i

        return []