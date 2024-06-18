# O(log n) - Logarithmic algorithms grow sub-linearly as the input grows
import random
import time

from matplotlib import pyplot as plt


# A classic example of a logarithmic algorithm is the binary search algorithm
# To elaborate, given a sorted list of n elements, a linear search would take O(n) time to find an element in the list
# by checking each element. The binary search takes advantage of the fact that the list is sorted. Each loop, 
# binary search bisects the list and determines whether the element is in the first or second half of the list.


def binary_search(arr: list[int], value: int) -> int | None:
    # Get the left and right edges of the array
    left, right = 0, len(arr) - 1
    # Get the middle index of the array
    mid = (left + right) // 2

    # if the middle element equals the value, return the index
    if arr[mid] == value:
        return mid

    # if the middle element is less than the value, the value must be in the greater half of the sorted array
    if arr[mid] < value:
        # we know the element (if present) will be at index greater or equal to our new left value below
        left = mid + 1
        # recursively call binary search, pass the second half of the array. preserve index by adding 'left' 
        return left + binary_search(arr[left:], value)
    elif arr[mid] > value:
        # if the middle element is greater than, we know the value (if present) must be in the first half of the array
        # just slice the array in half and recursively call binary search
        return binary_search(arr[0:mid], value)
    else:
        return None


if __name__ == "__main__":
    input_sizes = [10 ** i for i in range(1, 6)]
    times = []

    for input_size in input_sizes:
        inputs = [i for i in range(input_size)]
        random_search_value = random.randint(0, input_size)
        start_time = time.time()
        binary_search(inputs, random_search_value)
        times.append(time.time() - start_time)

    fig, ax = plt.subplots()
    ax.plot(input_sizes, times)
    plt.show()
