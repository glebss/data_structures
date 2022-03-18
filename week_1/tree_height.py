# python3

import sys
import threading

def compute_height(tree, root):
    if not tree[root]:
        return 1
    return 1 + max([compute_height(tree, r) for r in tree[root]])


def create_tree(n, parents):
    tree = [[] for _ in range(n)]
    root = None
    for i, p in enumerate(parents):
        if p == -1:
            root = i
            continue
        tree[p].append(i)
    return tree, root


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree, root = create_tree(n, parents)
    print(compute_height(tree, root))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**30)   # new thread will get stack of such size
threading.Thread(target=main).start()
