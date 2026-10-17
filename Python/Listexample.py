def main():
    numbers = [12, 45, 2, 67, 19, 8, 33]
    low_numbers=list()
    high_numbers=list()
    for num in numbers:
        if num<20:
            low_numbers.append(num)
        else:
            high_numbers.append(num)
    print(low_numbers)
    print(high_numbers)

main()