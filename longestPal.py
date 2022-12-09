# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7. //"dccbccd"

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

test_string = "aaabbbbbcx"
test_string = "aaabbbbcx"

def buildLongestPal(string: str):
    mapping = {}
    for s in string:
        if s not in mapping:
            mapping[s] = 1
        else:
            mapping[s] += 1
    holder = ""
    longest_odd_key_at = None
    for key in mapping:
        if mapping[key] % 2 == 0:
            holder =  key * (mapping[key] // 2) + holder + key * (mapping[key] // 2)
        else:
            if not longest_odd_key_at:
                longest_odd_key_at = key
            if mapping[key] > mapping[longest_odd_key_at]:
                longest_odd_key_at = key
    if longest_odd_key_at:
        holder = holder[:len(holder) // 2] + (longest_odd_key_at * mapping[longest_odd_key_at]) + holder[len(holder) // 2:]
    return holder

print(buildLongestPal(test_string))