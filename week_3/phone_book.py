class PhoneBook:
    def __init__(self):
        self.book = {}
    
    def add(self, number, name):
        self.book[number] = name
    
    def delete(self, number):
        if self.book.get(number):
            del self.book[number]

    def find(self, number):
        if self.book.get(number):
            return self.book[number]
        return "not found"

if __name__ == '__main__':
    phone_book = PhoneBook()
    n = int(input())
    for _ in range(n):
        query = input().split()
        if query[0] == 'add':
            number, name = int(query[1]), query[2]
            phone_book.add(number, name)
        elif query[0] == 'del':
            number = int(query[1])
            phone_book.delete(number)
        elif query[0] == 'find':
            number = int(query[1])
            print(phone_book.find(number))
