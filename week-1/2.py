#No maximum for n specified?
import sys
#Problem forms a directed graph we always can pick only those that have no edges coming into them
def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    counts = [0] * n
    pointers = {}

    for _ in range(0,m):
        a,b = map(int,sys.stdin.readline().split()) 
        counts[a] += 1
        if b not in pointers:
            pointers[b] = []
        pointers[b].append(a)
    
    res = []
    while True:
        found = False
        for i in range(0,n):
            if counts[i] == 0:
                found = True
                res.append(i)
                counts[i] = -1 # -1 means we have already added it to the result
                if i in pointers:
                    for j in pointers[i]:
                        counts[j] -= 1
        if not found:
            break
    if len(res) == n:
        print(res)
    else:
        print([])

if __name__ == "__main__":
    main()