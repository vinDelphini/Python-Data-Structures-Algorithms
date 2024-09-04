class IsSubsequence:

    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0

        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                l += 1
        return l == len(s)


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    # Expected Output: true
    print(IsSubsequence().isSubsequence(s, t))
