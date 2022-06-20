
##Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

#For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".






def palindrome(s:str) -> bool:
    return s == s[::-1]
def longestpalindrome(s:str) -> int:
    n = len(s)
    for i in range(n):
        for j in range(i+1):
            if palindrome(s[j:n-i+j]):
                return s[j:n-i+j], n-i
                
longestpalindrome("aabcdcb")
longestpalindrome('bananas')
