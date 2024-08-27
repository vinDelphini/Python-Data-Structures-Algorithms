class ReverseVowels:

    def reverseVowels(self, str: str) -> str:
        str = list(str)
        l, r = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        while l < r:
            if str[l] not in vowels:
                l += 1
            elif str[r] not in vowels:
                r -= 1
            else:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1
        return "".join(str)


if __name__ == "__main__":
    s = "hello"
    # expected output: "holle"
    print(ReverseVowels().reverseVowels(str=s))
