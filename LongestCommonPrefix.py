class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        count = len(strs[0])
        for i in range(count):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][0: i]

        return strs[0]


if __name__ == "__main__":
    answer = Solution()
    print(answer.longestCommonPrefix(["flower","flow","flight"]))