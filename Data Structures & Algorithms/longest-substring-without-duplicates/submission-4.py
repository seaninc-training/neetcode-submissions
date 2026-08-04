class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        else:
            longest_ss = 0
            i = 0
            j = i + 1
            curr_ss = {s[i]}
            curr_length = 1

            while i < j and j <= len(s) - 1:
                if s[j] not in curr_ss:
                    curr_ss.add(s[j])
                    curr_length += 1
                    if j == len(s) - 1:
                        longest_ss = max(curr_length, longest_ss)
                    else:
                        j += 1
                else:
                    longest_ss = max(curr_length, longest_ss)
                    i +=1
                    j = i + 1 
                    curr_ss = {s[i]}    
                    curr_length = 1  
            return longest_ss


