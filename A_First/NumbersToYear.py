class FileInput:
    """
    Find three numbers that sum to 2020, multiply them and print the result.
    """
    file = open("Numbers.txt", "r")
    number_list = []
    first_number = 0
    second_number = 0
    third_number = 0

    for val in file:
        number_list.append(val.replace("\n", ""))
    file.close()

    for var_1 in number_list:
        for var_2 in number_list:
            for var_3 in number_list:
                if int(var_1) + int(var_2) + int(var_3) == 2020:
                    first_number = var_1
                    second_number = var_2
                    third_number = var_3

    multiplication = int(first_number) * int(second_number) * int(third_number)
    print(first_number + " + " + second_number + " + " + third_number + " = 2020")
    print("Multiplication is:", multiplication)


