from typing import List

class LongestCommonPrefix:

    def commonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str1, str2 = strs[0], strs[-1]
        i = 0
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1
        return str1[:i]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    # Expecred Output: "fl"
    print(LongestCommonPrefix().commonPrefix(strs=strs))
