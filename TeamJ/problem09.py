import sys
# I think there might be a better solution but the best I could come up with is O(N log N) where N - length of the string
def main():
    s = sys.stdin.readline().strip()
    lo = 0
    hi = len(s)
    res = 0
    while lo<=hi:    
        mid = lo + (hi-lo)//2
        if can(mid,s):
            res = mid
            lo = mid+1
        else:
            hi = mid-1
    sys.stdout.write(str(res) + '\n')

def can(mid,s):
    freq = [0]*26
    for i in range(0,mid):
        freq[ord(s[i])-ord('A')] += 1
    if max(freq) >= mid//2 + (mid%2):
        return True
    for i in range(mid,len(s)):
        freq[ord(s[i-mid])-ord('A')] -= 1
        freq[ord(s[i])-ord('A')] += 1
        if max(freq) >= mid//2 + (mid%2):
            return True
    return False
        

if __name__ == '__main__':
    main()