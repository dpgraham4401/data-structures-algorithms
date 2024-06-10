# O(1) AKA "Oh of 1",
# This is the best case scenario for time complexity, no matter how large the input,
# the algorithm will always take the same amount of time to complete.
import time


def constant_time(items):
    # no matter how large the input, the same number of steps are taken
    result = items[0]
    result = result + 1
    return result


if __name__ == "__main__":
    small_input = [1, 2, 3, 4, 5]
    large_input = [i for i in range(1000000)]

    start = time.time()
    constant_time(small_input)
    end = time.time()
    print("Small input time: ", end - start)

    start = time.time()
    constant_time(large_input)
    end = time.time()
    print("large input time: ", end - start)
