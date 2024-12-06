#Super unclear statement, had to decipher inputs
#The inputs and outputs are not decisive, such as these
# C A
# C B
# Item ‘C’ already entered
# A B C
# B C A
# C A B
# E F G
# F G E
# No valid sequence exists
# The output for the second one should be Item 'B' already entered according to the first one as it is an invalid sequence to begin with
#Otherwise solution very similar to 2
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
        if counts.get(line[len(line)-1]) is None:
            counts[line[len(line)-1]] = 0
        counts[line[len(line)-1]] += len(line)-1
        for j in range(0,len(line)-1):
            if line[j] in pointers:
                print(f"Item {line[j]} already entered")
                return
            if(line[j]==line[len(line)-1]):
                print(f"Item {line[j]} cannot depend on itself")
                return
            pointers[line[j]] = (line[len(line)-1])
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