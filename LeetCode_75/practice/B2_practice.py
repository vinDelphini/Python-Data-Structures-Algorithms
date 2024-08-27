class IsSubsequence:

    def isSubsequence(self, s: str, t: str) -> str:
        l = 0
        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                l += 1
        return l == len(s)


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    # expected output: true
    print(IsSubsequence().isSubsequence(s, t))
    