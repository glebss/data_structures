import sys
import threading

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        

def in_order_traversal(node):
    global nodes
    if node.left != -1:
        in_order_traversal(nodes[node.left])
    print(node.key, end=" ")
    if node.right != -1:
        in_order_traversal(nodes[node.right])

def pre_order_traversal(node):
    global nodes
    print(node.key, end=" ")
    if node.left != -1:
        pre_order_traversal(nodes[node.left])
    if node.right != -1:
        pre_order_traversal(nodes[node.right])

def post_order_traversal(node):
    global nodes
    if node.left != -1:
        post_order_traversal(nodes[node.left])
    if node.right != -1:
        post_order_traversal(nodes[node.right])
    print(node.key, end=" ")

def main():
    n = int(input())
    global nodes
    nodes = []
    for _ in range(n):
        key, left, right = list(map(int, input().split()))
        nodes.append(Node(key, left, right))
    
    # in-order traversal
    in_order_traversal(nodes[0])
    print()
    # pre-order traversal
    pre_order_traversal(nodes[0])
    print()
    # post-order traversal
    post_order_traversal(nodes[0])
    print()


# if __name__ == '__main__':
#     main()

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()