class IsSubSequence:

    def isSubSequence(self, s: str, t: str) -> bool:
        l = 0
        counter = 0
        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                counter += 1
                l += 1
        return len(s) == counter

s = "axc"
t = "ahbgdc"
# Expected Output: true

print(IsSubSequence().isSubSequence(s, t))
