# There is an O(n) solution I believe but that is a little out of scope for this course
# Instead we can use a o(n^2), that runs on a simple basis it tries to take every single character as the middle of the palindrome, also every single pair of characters
# Final runtime is worst case 2*(n-1) * n
# Since we have to find all DISTINCT palindromes, we use a set to store them
import sys

def main():
    s = sys.stdin.readline().strip()
    palindromes = set()
    for i in range(0,len(s)):
        #Odd length palindromes
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if l != r:
                palindromes.add(s[l:r+1])
            l-=1
            r+=1
        l = i
        r = i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindromes.add(s[l:r+1])
            l-=1
            r+=1
    palindromes_list = sorted(list(palindromes))
    if len(palindromes_list) == 0:
        sys.stdout.write("No palindromes\n")
        return
    for palindrome in palindromes_list:
        sys.stdout.write(f"{palindrome}\n")

if __name__ == "__main__":
    main()