# O(n) - Oh of n
# It means that the time it takes to complete the algorithm grows linearly with the size of the input.
import time

import matplotlib.pyplot as plt


def linear_time(inputs: [int]):
    results = [i * 2 for i in inputs]
    return results


if __name__ == "__main__":
    input_sizes = [1, 1000, 1000000]
    times = []

    for input_size in input_sizes:
        inputs = [i for i in range(input_size)]
        start_time = time.time()
        linear_time(inputs)
        times.append(time.time() - start_time)

    fig, ax = plt.subplots()
    ax.plot(input_sizes, times)
    plt.show()
