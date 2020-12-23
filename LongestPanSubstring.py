class Solution(object):
    mem = {}
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        
        left = s[0: len(s) - 1]
        right = s[1:len(s)]
        if left not in self.mem:
            self.mem[left] = self.longestPalindrome(left)
            
        if right not in self.mem:
            self.mem[right] = self.longestPalindrome(right)
        
        return self.mem[left] if len(self.mem[left]) > len(self.mem[right]) else self.mem[right]


if __name__ == "__main__":
    answer = Solution()
    print(answer.longestPalindrome("banana"))