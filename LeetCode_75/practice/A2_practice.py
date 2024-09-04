class GreatestCommonDivisor:

    def greatestCommonDivisor(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def isDivisor(l):
            if l1 % l and l2 % l:
                False
            common = str1[:l]
            
            f1, f2 = l1 // l, l2 // l
            return common * f1 == str1 and common * f2 == str2
        
        for i in range(min(l1, l2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""
        

if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    # Expected Output: "AB"
    print(GreatestCommonDivisor().greatestCommonDivisor(str1=str1, str2=str2))
