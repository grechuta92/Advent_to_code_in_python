import math


class Seats:
    """
    ex. FBFBBFFRLR:

    F - Front
    B - Back
    L - Left
    R - Right

    7 first letters:
    F OR B

    Plane has 128 rows [0-127]

    Start by considering the whole range, rows 0 through 127.
    FBFBB:
        F means to take the lower half, keeping rows 0 through 63.
        B means to take the upper half, keeping rows 32 through 63.
        F means to take the lower half, keeping rows 32 through 47.
        B means to take the upper half, keeping rows 40 through 47.
        B keeps rows 44 through 47.
        F keeps rows 44 through 45.
        The final F keeps the lower of the two, row 44.

    3 last letters:
    L OR R

    Plane has 8 columns [0-7]

    Start by considering the whole range, columns 0 through 7.
    RLR:
        R means to take the upper half, keeping columns 4 through 7.
        L means to take the lower half, keeping columns 4 through 5.
        The final R keeps the upper of the two, column 5.

    That means: row 44, column 5

    seat Id:
        seat_number * 8 + column = seat_Id
        44 * 8 + 5 = 357

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

    Find your seat number id, knowing that first and the last of id's doesn't exist!

    ANSWER IS:
    548!

    """

    file_boarding_passes = open("boarding_passes.txt", "r", encoding="UTF-8")

    list_of_passes = []

    for var in file_boarding_passes:
        list_of_passes.append(var)

    file_boarding_passes.close()

    number_of_rows = 128
    number_of_columns = 7
    row_low = 0
    row_high = int(number_of_rows)
    column_low = 0
    column_high = int(number_of_columns)

    final_row = 0
    final_column = 0

    seat_id = 1
    list_of_seats_id = []

    for var in list_of_passes:
        for letter in var:
            if row_high != row_low:
                if letter == "F":
                    row_high = math.ceil(row_high - (row_high - row_low) / 2) - 1
                elif letter == "B":
                    row_low = math.ceil((row_high - (row_high - row_low) / 2))
            else:
                final_row = row_high
                row_low = 0
                row_high = int(number_of_rows)

            if column_low != column_high:
                if letter == "L":
                    column_high = math.ceil(column_high - (column_high - column_low) / 2) - 1
                elif letter == "R":
                    column_low = math.ceil(column_high - (column_high - column_low) / 2)
            else:
                final_column = column_high
                column_low = 0
                column_high = int(number_of_columns)
        row_high = int(number_of_rows)
        row_low = 0

        seat_id = final_row * 8 + final_column
        list_of_seats_id.append(seat_id)

    list_of_seats_id.sort()

    print(list_of_seats_id[-1])

    for var in range(89, 989):
        if var not in list_of_seats_id:
            print("Your seats is: ", var)


