with open("file1.txt") as f1:
    with open("file2.txt") as f2:
        f1_list = [int(number.strip()) for number in f1.readlines()]
        f2_list = [int(number.strip()) for number in f2.readlines()]

        common_numbers = [number for number in f1_list if number in f2_list]

print(common_numbers)