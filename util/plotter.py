import matplotlib.pyplot as plt


def plot(data, random_data, title):
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
