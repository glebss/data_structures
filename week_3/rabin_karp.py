# python3

def poly_hash(string, p=1000000007, x=263):
    ans = 0
    for c in reversed(string):
        ans = (ans * x + ord(c)) % p
    return ans  

def precompute_hashes(T, l, p=1000000007, x=263):
    H = [0 for _ in range(len(T)-l+1)]
    S = T[-l:]
    H[-1] = poly_hash(S, p=p, x=x)
    y = 1
    for _ in range(l):
        y = (y * x) % p
    for i in range(len(T)-l-1, -1, -1):
        H[i] = (x * H[i+1] + ord(T[i]) - y * ord(T[i+l])) % p
    return H

def rabin_karp(T, P, p=1000000007, x=263):
    result = []
    l = len(P)
    p_hash = poly_hash(P, p=p, x=x)
    H = precompute_hashes(T, l, p=p, x=x)
    for i in range(len(T)-l+1):
        if p_hash != H[i]:
            continue
        if P == T[i:l+i]:
            result.append(i)
    return result


if __name__ == '__main__':
    P = input()
    T = input()
    res = rabin_karp(T, P)
    print(*res)