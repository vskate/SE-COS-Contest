# Again no limit on n which might be an issue
# Easy to brute force in O(n^2), can be solved in O(log n) once you notice a pattern
# Every step we delete precisely half of the remaining elements
# We can always focus on just the first element of the array -> if we are currently going from the left we have to move it and if we are going from the right and the number of remaining elements is odd we have to move it as well.
# Where do we actually move it to we cannot simply increment it?
# This is the hardest observation to make, we keep track of a number we can call "turn", which starts at 0,
# Every time we need to move the position of the first element we do so by adding 2^turn to it
# Why 2^turn? The gaps are DOUBLING every time we remove half the elements

import sys

def main():
    n = int(sys.stdin.readline())
    turn = 0
    left = True
    first = 1
    while(n>1):
        if(left or n%2 == 1):
            first += 2**turn
        n = n//2
        turn += 1
        left = not left
    
    sys.stdout.write(str(first) + '\n')
    

if __name__ == '__main__':
    main()