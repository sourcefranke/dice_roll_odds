import csv
import collections
import numpy.random as r

from util.calculation import odds, group_numbers


def roll(size=1):
    return sum([*r.randint(low=1, high=7, size=(size,))])


def series(range_size=1, roll_size=1):
    results = []
    for i in range(range_size):
        results.append(roll(roll_size))
    return results


def series_adv(range_size=1, roll_size=1):
    results = []
    for i in range(range_size):
        results.append(
            max(
                roll(roll_size),
                roll(roll_size)
            )
        )
    return results


def write_file(file, func, size):
    path = f"../random_csv/{file}.csv"
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        result = collections.OrderedDict(sorted(odds(group_numbers(func(size))).items()))
        for k in result:
            writer.writerow([k, result[k]])
    return result


def create_random_data():
    write_file("one_die", lambda s: series(s), 2500)
    write_file("one_die_adv", lambda s: series_adv(s), 2500)
    write_file("two_dice", lambda s: series(s, 2), 5000)
    write_file("two_dice_adv", lambda s: series_adv(s, 2), 5000)
    write_file("four_dice", lambda s: series(s, 4), 10000)
    write_file("four_dice_adv", lambda s: series_adv(s, 4), 10000)


if __name__ == "__main__":
    create_random_data()
