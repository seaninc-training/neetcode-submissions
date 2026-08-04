class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr_length = 1
                curr_num = num

                while (curr_num + 1) in numSet:
                    curr_length += 1
                    curr_num += 1
                
                if curr_length > longest:
                    longest = curr_length
        
        return longest
                
