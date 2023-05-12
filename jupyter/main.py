from random_word import RandomWords
import random
int_list = []
float_list = []
str_list = []
w = RandomWords()

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

for i in range(500):
    int_list.append(random.randint(0,1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.get_random_word())

size = len(int_list)

%timeit -n 1 -r 1 -o quickSort(int_list[:], 0, size - 1)
%timeit -n 1 -r 1 -o quickSort(float_list[:], 0, size - 1)
%timeit -n 1 -r 1 -o quickSort(str_list[:], 0, size - 1)