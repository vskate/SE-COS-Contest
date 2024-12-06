import sys
#Simple solution - we can work from the proof of sums of arithmetic series - we pair each number, and the largest one has no pair
#Will be using sys for input and output as its much faster than input() and print()
# Will be running everything in main as it runs faster
def main():
    N = int(sys.stdin.readline())
    R = (N//2) + (N%2)
    sys.stdout.write(f"{R}\n")
    if N%2 == 1:
        sys.stdout.write(f"1 {N}\n")
    else:
        N+=1 # Just an easy way to handle even numbers
    for i in range(0,N//2):
        sys.stdout.write(f"2 {i+1} {N-i-1}\n")

if __name__ == "__main__":
    main()