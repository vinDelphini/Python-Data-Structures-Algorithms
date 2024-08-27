from typing import List

class CommonPrefix:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # sort the list of strings
        strs.sort()
    
        # take the first and last string 
        first, last = strs[0], strs[-1]
        
        # find common prefix between first and last string
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


strs = ["flower","flow","flight"]
print(CommonPrefix().longestCommonPrefix(strs=strs))
