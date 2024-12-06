#Another N log N solution, however I believe there isn't a better solution than this one

import sys

def main():
    n = int(sys.stdin.readline())
    planks = list(map(int, sys.stdin.readline().split()))
    if n < 4:
        sys.stdout.write('0\n')
        return
    res = 0
    lo = 1
    hi = 10**9
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if can(mid,planks,n):
            res = mid
            lo = mid+1
        else:
            hi = mid-1
    sys.stdout.write(str(res*res) + '\n')

def can(mid,planks,n):
    count = 0
    for i in range(0,n):
        count += planks[i]//mid
    return count >= 4

if __name__ == '__main__':
    main()