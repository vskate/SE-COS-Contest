# Again a few issues with the statement, do you only work with whole kroner? if not - which is the case presumably what accuracy do we want?
# Also no limits for x and y, which could be an issue if they are very large
# There exists a better solution binary searching and using the Geometric series sum formula
# But since there are no limits for x and y, we cannot get the upper bound for the binary search :(
import sys 

def main():
    x, y = map(int, sys.stdin.readline().split())
    weeks = 0

    while y < x:
        if weeks%4 != 0:
            y += (y*0.05)
        elif weeks%4 == 0 and weeks > 1:
            y += (y*(-0.03))

        if y < x:
            weeks += 1

    sys.stdout.write(f"{weeks}\n")

if __name__ == "__main__":
    main()

