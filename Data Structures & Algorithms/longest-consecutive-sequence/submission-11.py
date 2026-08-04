class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_length = 1
                curr_num = num

                while (curr_num + 1) in num_set:
                    curr_length += 1
                    curr_num += 1
                
                longest = max(curr_length, longest)
        
        return longest
                
