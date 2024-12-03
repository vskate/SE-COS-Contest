"""
5. Palindromic substrings
You are given a string s. Your task is to find all distinct palindromic substrings that have a length
of 2 or more. A palindromic substring is a sequence of characters in the string that reads the
same forwards and backwards, such as "aba" or "madam".
Once you’ve found all the palindromic substrings, you should sort them in alphabetical order
(lexicographical order) and print them, each on a new line. If no palindromic substrings of length
2 or more exist, simply print "No Palindromes".
Input
The input should contain a string, which consists of palindromes (or not).
Output
Your program should write all the palindromes that are within the string input and sort them in
alphabetical order.
"""

def findPalindromicSubstrings(s):
    substrings = {
    s[start:start + length]
    for length in range(1, len(s) + 1)
    for start in range(len(s) - length + 1)
    }

    final = []

    for i in substrings:
        if i == i[::-1] and len(i) >= 2:
            final.append(i)

    final.sort()

    return final

def printout(ls):
    if len(ls) == 0:
        print("No palindromes")
    else:
        for i in ls:
            print(i)

printout(findPalindromicSubstrings('hahaha'))
printout(findPalindromicSubstrings('alphabetical'))
printout(findPalindromicSubstrings('commodore64'))
printout(findPalindromicSubstrings('uwu'))
printout(findPalindromicSubstrings('sys'))
