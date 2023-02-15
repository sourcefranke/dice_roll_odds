def cartesian(die, number_dice=1, acc_func=lambda x, y: x + y):
    """
    :param die: list of possible values of one die roll
    :param number_dice: how many dice to be used
    :param acc_func: function for accumulating the values from both dice
    :return: list of all possible combinations of results for the dice roll
    """
    if number_dice < 1:
        return []

    if number_dice == 1:
        return die

    accumulated = []
    for x in cartesian(die, number_dice - 1, acc_func):
        for y in die:
            accumulated.append(acc_func(x, y))

    return accumulated


def group_numbers(unordered):
    """
      :param unordered: contains results of die rolls in an unstructured way
      :return: grouped dictionary - key: distinct result, value: count of occurrence
      """
    grouped = {}
    for x in unordered:
        if x in grouped.keys():
            grouped[x] = grouped[x] + 1
        else:
            grouped[x] = 1

    return grouped


def odds(grouped):
    """
      :param grouped: dictionary of possible outcomes with their number of occurrence
      :return: a dictionary with distinct results and their probability of occurrence
      """
    total = sum(grouped.values())

    result = {}
    for k in grouped.keys():
        result[k] = grouped[k] / total

    return result


def calc(die, number_dice=1, roll_func=lambda d, n: cartesian(d, n)):
    """
    :param die: list of possible values of one die roll
    :param number_dice: how many dice to be used
    :param roll_func: function for determining all possible combinations
    :return: a dictionary with distinct results and their probability of occurrence
    """
    unordered = roll_func(die, number_dice)
    grouped = group_numbers(unordered)
    return odds(grouped)


def advantage(die, number_dice):
    """
    :param die: list of possible values of one die roll
    :param number_dice: how many dice to be used
    :return: all combinations possible
    """
    return cartesian(cartesian(die, number_dice), 2, max)
