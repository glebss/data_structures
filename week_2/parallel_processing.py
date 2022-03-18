
def parent(i):
    return (i - 1) // 2 
def left_child(i):
    return 2 * i + 1
def right_child(i):
    return 2 * i + 2

def sift_up(pqueue, i):
    while i > 0:
        parent_thread = pqueue[parent(i)]
        if parent_thread[-1] > pqueue[i][-1]:
            pqueue[i], pqueue[parent(i)] = pqueue[parent(i)], pqueue[i]
            i = parent(i)
        elif parent_thread[-1] == pqueue[i][-1] and parent_thread[0] > pqueue[i][0]:
            pqueue[i], pqueue[parent(i)] = pqueue[parent(i)], pqueue[i]
            i = parent(i)
        else:
            break

def sift_down(i, pqueue):
    min_index = i
    size = len(pqueue)
    l = left_child(i)
    if l < size:
        if pqueue[l][-1] < pqueue[min_index][-1]:
            min_index = l
        elif pqueue[l][-1] == pqueue[min_index][-1] and pqueue[l][0] < pqueue[min_index][0]:
            min_index = l
    r = right_child(i)
    if r < size:
        if pqueue[r][-1] < pqueue[min_index][-1]:
            min_index = r
        elif pqueue[r][-1] == pqueue[min_index][-1] and pqueue[r][0] < pqueue[min_index][0]:
            min_index = r
    if min_index != i:
        pqueue[i], pqueue[min_index] = pqueue[min_index], pqueue[i]
        sift_down(min_index, pqueue)

def extract_max(pqueue):
    result = pqueue[0]
    if len(pqueue) == 1:
        pqueue.pop()
        return result
    pqueue[0] = pqueue.pop()
    sift_down(0, pqueue)
    return result


def insert_thread(pqueue, thread):
    size = len(pqueue)
    pqueue.append(thread)
    size += 1
    sift_up(pqueue, size-1)

def build_priority_queue(n_threads):
    return [(i, 0) for i in range(n_threads)]

def main():
    n_threads, _ = tuple(map(int, input().split()))
    times = list(map(int, input().split()))
    pqueue = build_priority_queue(n_threads)
    for t in times:
        thread = extract_max(pqueue)
        insert_thread(pqueue, (thread[0], thread[-1]+t))
        print(*thread)

if __name__ == '__main__':
    main()
