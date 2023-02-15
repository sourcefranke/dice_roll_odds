def read_file(file):
    path = f"random_csv/{file}.csv"

    result = {}
    with open(path, mode='r') as file:
        for row in file.readlines():
            splitter = row.split(',')
            result[int(splitter[0])] = float(splitter[1])
    return result


def one_die():
    return read_file("one_die")


def one_die_adv():
    return read_file("one_die_adv")


def two_dice():
    return read_file("two_dice")


def two_dice_adv():
    return read_file("two_dice_adv")


def four_dice():
    return read_file("four_dice")


def four_dice_adv():
    return read_file("four_dice_adv")
