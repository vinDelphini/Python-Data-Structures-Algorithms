haystack = "hello"
needle = "ll"

needle_length = len(needle)

i = 0
for j in range(needle_length, len(haystack)):
    if needle == haystack[i:j]:
        print(i)

    