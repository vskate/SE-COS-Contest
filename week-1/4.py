#There is a simple brute force solution -> to speed it up we can notice
# that once we have more or equal computers with linux to k we know exactly how long the rest will take

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    l = 1
    res = 0
    while l < k:
        l *= 2
        res += 1
    n-= l
    res += n//k + (n%k != 0)
    sys.stdout.write(f"{res}\n")

if __name__ == "__main__":
    main()