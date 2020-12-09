class Finder:
    file = open("Series_of_numbers.txt", "r")
    preamble_length = 25
    list_of_var = []

    for var in file:
        list_of_var.append(var.rstrip())

    a = 0
    temp_counter = 0
    small_list = []
    list_length = len(list_of_var)
    list_of_sum = []
    list_of_answer = []

    for _ in range(list_length - preamble_length):
        for var in range(a, a + preamble_length):
            small_list.append(list_of_var[temp_counter])
            temp_counter += 1

        temp_counter = a + 1
        temp_sum_var = list_of_var[a + preamble_length]

        print("Small list:", small_list)
        print("Temp sum:", temp_sum_var)
        list_of_sum.append(temp_sum_var)

        for var_fir in small_list:
            for var_sec in small_list:
                i = 0
                # print(var_fir, var_sec, temp_sum_var)
                if (int(var_fir) + int(var_sec)) == int(temp_sum_var):
                    list_of_answer.append(temp_sum_var)
                    print(var_fir,"+", var_sec, "=", temp_sum_var)
        small_list = []
        print()
        a += 1
        temp_sum_var = 0

    print(list_of_sum)
    print(set(list_of_answer))

    # print( set(list_of_answer).intersection(list_of_sum))

    j = 0
    for var in list_of_sum:
        if var not in list_of_answer:
            print(var)

    file.close()
