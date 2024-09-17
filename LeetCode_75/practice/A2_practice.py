class GreatestCommonDivisor:

    def GCDStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def isDivisor(l):
            if l1 % l == 0 or l2 % l == 0:
                candidate = str1[:l]
            f1, f2 = l1 // l, l2 // l
            return f1 * candidate == str1 and f2 * candidate == str2
        
        for i in range(min(l1, l2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""

if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    print(GreatestCommonDivisor().GCDStrings(str1, str2))
    