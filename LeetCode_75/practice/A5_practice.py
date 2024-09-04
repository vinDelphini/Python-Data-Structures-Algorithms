class ReverseVowels:

    def reverseVowels(self, s:str) -> str:
        vowels = ("aeiou")
        l, r = 0, len(s) - 1    
        s = list(s)

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
    

if __name__ == "__main__":
    s = "leetcode"
    # Output: "leotcede"
    print(ReverseVowels().reverseVowels(s=s))
