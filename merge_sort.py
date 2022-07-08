import time
import random

random.seed(1)

print("Merge Sort")

a = [random.randint(0, 100) for i in range(2)]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        R = arr[:mid]
        L = arr[mid:]

        merge_sort(R)
        merge_sort(L)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


st, pt = time.time(), time.process_time()
merge_sort(a)
end, end_pt = time.time(), time.process_time()


print("Execution Time: ", end - st)
print("CPU Time: ", end_pt - pt)
