
###Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

##For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".




def longest_substring(string, k):
    start, end = 0, k
    max_len = k
    # The string has to be continous, so we check slices of the string
    while end <= len(string):
        # If the substring is good
        if len(set(string[start:end])) <= k:
            # If the substring is the best so far, store it's length
            current_len = end - start
            if current_len >= max_len:
                max_len = current_len
            # Try to make the substring longer
            end += 1
        else:
            # Else try to make the substring shorter
            start += 1
    return max_len

z=longest_substring("abcba", 2)
print(z)
