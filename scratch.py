def what_square(pos):
    row, col = pos
    print(str(row) + " " + str(col))

    row_st = row // 3 * 3
    col_st = col // 3 * 3
    print("\tcheck rows " + str(row_st) + " through " + str(row_st + 2))
    print("\tcheck cols " + str(col_st) + " through " + str(col_st + 2))
    print("-" * 15)


# what_square((2, 5))
# what_square((3, 5))
# what_square((4, 5))
# what_square((5, 5))
# what_square((6, 5))


def get_input_file():
    arr = []
    file = open("input.txt", 'r')
    for line in file:
        arr2 = []
        for word in line.split():
            arr2.append(word)
        arr.append(arr2)

    print(arr)

get_input_file()