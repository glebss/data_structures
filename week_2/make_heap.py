N_SWAPS = 0
swaps = []

def left_child(i):
    return 2 * i + 1
def right_child(i):
    return 2 * i + 2

def sift_down(i, arr):
    min_index = i
    size = len(arr)
    l = left_child(i)
    if l < size and arr[l] < arr[min_index]:
        min_index = l
    r = right_child(i)
    if r < size and arr[r] < arr[min_index]:
        min_index = r
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        global N_SWAPS, swaps
        N_SWAPS += 1
        swaps.append((i, min_index))
        sift_down(min_index, arr)



def build_heap(arr):
    size = len(arr)
    for i in range((size-1) // 2, -1, -1):
        sift_down(i, arr)
    print(N_SWAPS)
    for swap in swaps:
        print(*swap)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    build_heap(arr)
    
if __name__ == '__main__':
    main()
