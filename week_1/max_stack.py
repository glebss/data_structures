

def main():
    stack = []
    max_stack = []
    n = int(input())
    for _ in range(n):
        line = input()
        line = line.split()
        op = line[0]
        if op == 'push':
            v = int(line[1])
            stack.append(v)
            if not max_stack:
                max_stack.append(v)
            elif max_stack:
                if v >= max_stack[-1]:
                    max_stack.append(v)
        elif op == 'max':
            print(max_stack[-1])
        elif op == 'pop':
            last_el = stack.pop()
            if last_el == max_stack[-1]:
                max_stack.pop()

if __name__ == '__main__':
    main()