# python3
import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**27) 

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def in_order_traversal(node):
    global nodes, res
    if node.left != -1:
        in_order_traversal(nodes[node.left])
    res.append(node.key)
    if node.right != -1:
        in_order_traversal(nodes[node.right])

def check_increasing(res):
    for i in range(1, len(res)):
        if res[i-1] >= res[i]:
            return False
    return True

def main():
    n = int(input())
    if n == 0:
        print('CORRECT')
        return
    global nodes, res
    nodes, res = [], []
    for _ in range(n):
        key, left, right = list(map(int, input().split()))
        nodes.append(Node(key, left, right))
    
    # check whether res is increasing
    in_order_traversal(nodes[0])
    if check_increasing(res):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()