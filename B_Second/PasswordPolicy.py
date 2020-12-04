def check_is_correct(first_index, second_index, letter, password):
    if password[first_index - 1] == letter and password[second_index - 1] != letter:
        return True
    elif password[first_index - 1] != letter and password[second_index - 1] == letter:
        return True
    else:
        return False


class PasswordPhilosophy:
    """
    Sample:
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc

        Each policy describes two positions in the password, where 1 means the first character, 2 means the second
    character, and so on.
    Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.


    Correct answer:
        588 passwords are valid!
    """

    file_with_passwords = open("Passwords.txt", "r")
    min_val = 0
    max_val = 0
    letter = ""
    password = ""
    quantity_of_valid_passwords = 0
    list_of_policies_and_passwords = []

    for var in file_with_passwords:
        list_of_policies_and_passwords = var.replace(":", "").replace("-", " ").replace("\n", "").split(" ")
        first_index = int(list_of_policies_and_passwords[0])
        second_index = int(list_of_policies_and_passwords[1])
        letter = list_of_policies_and_passwords[2]
        password = list_of_policies_and_passwords[3]

        if check_is_correct(first_index, second_index, letter, password):
            quantity_of_valid_passwords += 1
            print(list_of_policies_and_passwords)

    print(quantity_of_valid_passwords)

    file_with_passwords.close()
