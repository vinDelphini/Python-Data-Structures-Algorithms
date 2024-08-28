class GreatestCommonDivisor:

    def divisorOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        
        def isDivisor(l):
            if l1 % l == 0 and l2 % l == 0:
                divisor = str1[:l]

                f1, f2 = l1 // l, l2 // l
                return divisor * f1 == str1 and divisor * f2 == str2
        
        for l in range(min(l1, l2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    # Expected Output: "ABC"
    print(GreatestCommonDivisor().divisorOfStrings(str1=str1, str2=str2))
