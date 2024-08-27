class GCDStrings:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def isDivisor(i):
            if l1 % i or l2 % i:
                False
            candidate = str1[:i]
            f1, f2 = l1 // i, l2 // i
            return candidate * f1 == str1 and candidate * f2 == str2

        for i in range(min(l1, l2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""


if __name__ == "__main__":
    str1 = "ABABABAB"
    str2 = "ABAB"
    # expected output: "ABAB"
    print(GCDStrings().gcdOfStrings(str1=str1, str2=str2))
