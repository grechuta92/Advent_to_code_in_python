class Passport:
    """
    How many passport are valid?

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    VALID:

    Passport validation:
    All information: ecl, pid, eyr, hcl, byr, iyr, cid, hgt
    Obligatory information:

    North Pole Credentials (without cid):
    All information: ecl, pid, eyr, hcl, byr, iyr, hgt

    """
    file_original = open("Documents_data.txt", "r", encoding="UTF-8")
    file_converted = open("Documents_data_copy.txt", "r", encoding="UTF-8")
    file_cid = open("cid_country.txt", "r", encoding="UTF-8")
    list_of_original_var = []
    list_of_cid = []

    counter_valid_passport = 0
    counter_var = 0

    for var in file_converted:
        list_of_original_var.append(var.rstrip("\n").split(":"))

    for var in file_cid:
        list_of_cid.append(var.lstrip("0").rstrip("\n").split("\t"))

    is_birthday = False
    is_issue_year = False
    is_expiration_year = False
    is_height = False
    is_hair_color = False
    is_eye_color = False
    is_passport_id = False
    is_cid = True

    for var in list_of_original_var:
        if var[0] != "":
            if var[0] == "ecl" or var[0] == "pid" or var[0] == "eyr" or var[0] == "hcl" or var[0] == "byr" or \
                    var[0] == "iyr" or var[0] == "hgt" or var[0] == "cid":
                if var[0] == "byr" and 1920 <= int(var[1]) <= 2002:
                    is_birthday = True
                    continue
                elif var[0] == "iyr" and 2010 <= int(var[1]) <= 2020:
                    is_issue_year = True
                    continue
                elif var[0] == "eyr" and 2020 <= int(var[1]) <= 2030:
                    is_expiration_year = True
                    continue
                elif var[0] == "hcl" and var[1].startswith("#") and len(var[1]) == 7:
                    # c0946f
                    for temp_var in var[1]:
                        if not (ord(temp_var) == 35 or 97 <= ord(temp_var) <= 102 or 48 <= ord(temp_var) <= 57):
                            is_hair_color = False
                            break
                        else:
                            is_hair_color = True
                            continue
                elif var[0] == "ecl" and (var[1] == "amb" or var[1] == "blu" or var[1] == "gry" or var[1] == "grn" or
                                          var[1] == "hzl" or var[1] == "oth"):
                    is_eye_color = True
                    continue
                elif var[0] == "pid" and var[1].isdigit() and len(var[1]) == 9:
                    is_passport_id = True
                    continue
                elif var[0] == "hgt":
                    if var[1][:-2] != "":
                        value = int(var[1][:-2])
                    if var[1][-2:] == "cm" and (150 <= value <= 193):
                        is_height = True
                        continue
                    elif var[1][-2:] == "in" and (59 <= value <= 76):
                        is_height = True
                        continue
                    else:
                        is_height = False

                elif var[0] == "cid":
                    for val in list_of_cid:
                        if val[0] == var[1]:
                            is_cid = True
                            break
                        else:
                            is_cid = False

        if var != "" and is_birthday and is_issue_year and is_expiration_year and is_hair_color and is_eye_color \
                and is_passport_id and is_height and is_cid:
            # print("var od 0", var[0])
            # print(var)
            counter_valid_passport += 1
            print(counter_valid_passport)

        if var[0] == "":
            print("byr:", is_birthday, end="    ")
            print("iyr:", is_issue_year, end="    ")
            print("eyr:", is_expiration_year, end="    ")
            print("hcl:", is_hair_color, end="    ")
            print("ecl:", is_eye_color, end="    ")
            print("pid:", is_passport_id, end="    ")
            print("cid:", is_cid, end="    ")
            print("hgt:", is_height, end="\n\n")

            is_birthday = False
            is_issue_year = False
            is_expiration_year = False
            is_hair_color = False
            is_eye_color = False
            is_passport_id = False
            is_cid = True
            is_height = False

    print("\n\nNumber of valid passport is:", counter_valid_passport)

    file_original.close()
    file_converted.close()
    file_cid.close()
