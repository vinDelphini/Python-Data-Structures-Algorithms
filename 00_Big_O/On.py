def print_items(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

if __name__=="__main__":

    numbers = print_items(10)
    for number in numbers:
        print(number)
