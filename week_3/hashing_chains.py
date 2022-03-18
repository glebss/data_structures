# python3

def hash_poly(string, m, p=1000000007, x=263):
    ans = 0
    for c in reversed(string):
        ans = (ans * x + ord(c)) % p
    return ans % m

class HashTable:
    def __init__(self, m):
        self.table = [[] for _ in range(m)]
    
    def add(self, string):
        n_cell = hash_poly(string, m)
        for el in self.table[n_cell]:
            if el == string:
                return
        self.table[n_cell].insert(0, string)

    def delete(self, string):
        n_cell = hash_poly(string, m)
        found = False
        for el in self.table[n_cell]:
            if el == string:
                found = True
                break
        if found:
            self.table[n_cell].remove(string)

    def find(self, string):
        n_cell = hash_poly(string, m)
        for el in self.table[n_cell]:
            if el == string:
                return "yes"
        return "no"

if __name__ == '__main__':
    m = int(input())
    N = int(input())
    table = HashTable(m)
    for _ in range(N):
        query = input().split()
        if query[0] == 'add':
            string = query[1]
            table.add(string)
        elif query[0] == 'del':
            string = query[1]
            table.delete(string)
        elif query[0] == 'find':
            string = query[1]
            print(table.find(string))
        elif query[0] == 'check':
            to_check = int(query[1])
            for el in table.table[to_check]:
                print(el, end=" ")
            print()