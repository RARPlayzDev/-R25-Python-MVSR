def longest_unique_substring(s):
    char_set = set()       # To store unique characters
    left = 0
    max_len = 0
    longest_sub = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        # Check if current window is longest
        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest_sub = s[left:right+1]

    return longest_sub


# Example
string = "abcabcbb"
print("Longest substring without repeating characters:", longest_unique_substring(string))
