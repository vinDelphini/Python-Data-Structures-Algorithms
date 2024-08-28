class IsSubsequence:

    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for i in range(len(t)):
            if l < len(s) and s[l] == t[i]:
                l += 1
        return l == len(s)


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    # Expected Output: true
    print(IsSubsequence().isSubsequence(s=s, t=t))
