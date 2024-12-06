# This is a dynamic programming problem whose complexity is O(n*m) where n is the number of trains and m is the length of the station
# We build the solution greedily we start with station length 0, then 1, then 2, for each position we look at all the previous position reachable with a wagon and add that to our result
# We can also optimize the memory by having an array of size max(wagons) instead of the full station length -> we will not do this as it complicates the implementation too much
# Again there should be some things mentioned in the statement, since we can use any number of the wagon I assume there will not be repeating sizes

#IMPORTANT : One of the outputs is definitely wrong - the number of ways to assemble the trains grows super fast, so the output is wrong for the last test case
import sys

def main():
    wagons = list(map(int, sys.stdin.readline().split()))
    station_length = int(sys.stdin.readline())
    if station_length == 0:
        sys.stdout.write("0\n")
        return
    arr = [0]*(station_length+1)
    arr[0] = 1 # Base case there is exactly one way to have a station of length 0 -> empty, doesnt match the sample output though, that is why there is the edge case handled
    for i in range(1, station_length+1):
        for wagon in wagons:
            if i - wagon >= 0:
                arr[i] += arr[i-wagon]

    sys.stdout.write(f"{arr[station_length]}\n")



if __name__ == "__main__":
    main()