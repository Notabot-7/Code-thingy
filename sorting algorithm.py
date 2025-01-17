import random

# def make_list(size):
#     return [random.randint(0, 100) for _ in range(size+1)]

# def bubble_sort(arr):
    # n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 print_array(arr)

# def print_array(arr):
#     for i in arr:
#         print(i, end=" ")
#     print()

# if __name__ == "__main__":
#     try:
#         x = int(input("Length of list: "))
#     except ValueError:
#         x = int(input("Length of list: "))
#     arr = make_list(x)
#     print_array(arr)
#     bubble_sort(arr)
#     print("Sorted array:")
#     print_array(arr)

def make_list(size):
    return [random.randint(0, 100) for _ in range(size+1)]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print_array(arr)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()
