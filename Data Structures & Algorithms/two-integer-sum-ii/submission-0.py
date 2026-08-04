class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        viewed = {}

        for i, num in enumerate(numbers):
            num2 = target - num

            if num2 in viewed:
                return [viewed[num2] + 1, i + 1]
            
            viewed[num] = i

        return []