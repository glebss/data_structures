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

def is_bst(node, mini, maxi):
    global nodes
    if node.key > maxi or node.key < mini:
        return False
    
    if node.left != -1:
        ret = is_bst(nodes[node.left], mini, node.key-1)
        if not ret:
            return False
    
    if node.right != -1:
        ret = is_bst(nodes[node.right], node.key, maxi)
        if not ret:
            return False
    
    return True

def main():
    n = int(input())
    if n == 0:
        print('CORRECT')
        return
    global nodes
    nodes = []
    for _ in range(n):
        key, left, right = list(map(int, input().split()))
        nodes.append(Node(key, left, right))


    if is_bst(nodes[0], -2147483648, 2147483647):
        print('CORRECT')
    else:
        print('INCORRECT')
    

threading.Thread(target=main).start()
