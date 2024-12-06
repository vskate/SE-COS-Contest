#Solution very similar to 2
import sys

def main():
    counts = {}
    pointers = {}
    items = set()
    
    for i in range(0,5):    
        line = sys.stdin.readline().strip()
        line = line.split()
        if len(line)>3:
            print("Invalid number of dependencies (2 max)")
            return
        for l in line:
            items.add(l)
        if counts.get(line[0]) is None:
            counts[line[0]] = 0
        else:
            print(f"Item {line[0]} already entered")
            return
        counts[line[0]] += len(line)-1
        for j in range(1,len(line)):
            if(line[j]==line[0]):
                print(f"Item {line[j]} cannot depend on itself")
                return
            pointers[line[j]] = (line[0])
    for i in items:
        if i not in counts:
            counts[i] = 0
    res = []
    while True:
        found = False
        for i in items:
            if counts[i] == 0:
                found = True
                res.append(i)
                counts[i] = -1
                if i in pointers:
                    counts[pointers[i]] -= 1
        if not found:
            break
    if len(res) == len(items):
        print(res)
    else:
        print("No valid sequence exists")



if __name__ == "__main__":
    main()