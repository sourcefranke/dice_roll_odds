import matplotlib.pyplot as plt


def plot_data_random(data, random_data, title):
    """
    :param data: dictionary to be plotted
    :param random_data:
    :param title: individual title for the diagram
    """
    plt.title(title)
    plt.xlabel("Roll")
    plt.ylabel("Occurrence")
    plt.plot(data.keys(), data.values(), color="r", label='formula')
    plt.stem(random_data.keys(), random_data.values(), label='random')
    plt.legend()
    plt.show()


def plot_data_adv(data_normal, data_adv, title):
    """
    :param data_normal: dictionary to be plotted
    :param data_adv: same count of dice, just with advantage
    :param title: individual title for the diagram
    """
    plt.title(title)
    plt.xlabel("Roll")
    plt.ylabel("Occurrence")
    plt.plot(data_normal.keys(), data_normal.values(), color="b", label='normal')
    plt.plot(data_adv.keys(), data_adv.values(), color="r", label='advantage')
    plt.legend()
    plt.show()
