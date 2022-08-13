import random
import math
import asyncio

random.seed(0)


class FrequencyDistribution:
    def __init__(self):
        pass


# Global Variables
no_classes = 6
f = {}
upper_bound = []
lower_bound = []


def frequency(arr):
    if len(lower_bound) == 0 or len(upper_bound) == 0:
        print("Frequency Module: Empty List")
        return

    temp = arr.copy()
    for i in range(len(temp)):
        for j in range(no_classes):
            if lower_bound[j] <= temp[i] < upper_bound[j]:
                f[f"{lower_bound[j]}-{upper_bound[j]}"] += 1
    return f


def total_frequency():
    sum = 0
    for k, v in f.items():
        sum += v
    return sum


def groups(arr, shift=0):
    if 0 > shift or shift > 6:
        print("Groups Module: Shift should be 0 > shift > 6")
        return

    global f
    global upper_bound
    global lower_bound

    classes = minimum_number(arr.copy())
    cs = class_size(arr.copy())

    for i in range(no_classes):
        upper_bound.append(classes+cs-shift)
        lower_bound.append(classes-shift)
        classes += cs

    for i in range(no_classes):
        f[f"{lower_bound[i]}-{upper_bound[i]}"] = 0
    return


def display_classes():
    if len(lower_bound) == 0 or len(upper_bound) == 0:
        print("Display Classes Module: Empty List")
        return

    for i in range(no_classes):
        print(f"{lower_bound[i]}-{upper_bound[i]}")
    return


def class_size(arr):
    cs = min_max_number(arr.copy())
    return math.ceil((cs[1] - cs[0]) / no_classes)


def sort_data(arr):
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k = k + 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def min_max_number(arr):
    c_arr = arr.copy()
    if len(c_arr) <= 1500:
        print("Using Bubble Sort")
        temp = sort_data(c_arr)
        return temp[0], temp[-1]
    elif len(c_arr) > 1500:
        print("Using Merge Sort")
        temp = merge_sort(c_arr)
        return temp[0], temp[-1]


def maximum_number(arr):
    temp = arr.copy()
    m = temp[0]
    for i in range(len(temp)):
        if m < temp[i]:
            m = temp[i]
    return m


def minimum_number(arr):
    temp = arr.copy()
    m = temp[0]
    for i in range(len(temp)):
        if m > temp[i]:
            m = temp[i]
    return m


if __name__ == "__main__":
    print("--Frequency Distribution--")
    # Generating random age data
    rd = [random.randint(35, 90) for i in range(50)]
    print("Max: ", maximum_number(rd))
    print("Min: ", minimum_number(rd))
    print("Min & Max (sorted): ", min_max_number(rd))
    print("Class Size: ", class_size(rd))
    # sort_data(rd)
    groups(rd, shift=8)
    display_classes()

    print("Frequency: ", frequency(rd))
    print("Total frequency: ", total_frequency())



