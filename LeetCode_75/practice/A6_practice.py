class ReverseStrings:

    def reverseString(self, str:str) -> str:
        return " ".join(reversed(str.strip().split()))



if __name__ == "__main__":
    s = "the sky is blue"
    # expected output: "blue is sky the"
    print(ReverseStrings().reverseString(s))
    