# O(1) AKA "Oh of 1",
# This is the best case scenario for time complexity, no matter how large the input,
# the algorithm will always take the same amount of time to complete.
import time

import matplotlib.pyplot as plt


def constant_time(items):
    # no matter how large the input, the same number of steps are taken
    result = items[0]
    result = result + 1
    return result


if __name__ == "__main__":

    input_sizes = [1, 10, 100, 1000, 10000, 1000000]
    times = []

    for input_size in input_sizes:
        inputs = [i for i in range(input_size)]
        start_time = time.time()
        constant_time(inputs)
        times.append(time.time() - start_time)

    fig, ax = plt.subplots()
    table_data = list(zip(input_sizes, times))
    table = ax.table(cellText=table_data, colLabels=["Input Size", "Time"], loc='center')
    plt.show()
