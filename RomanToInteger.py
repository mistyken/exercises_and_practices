class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        if "IV" in s:
            res += 4
            s = s.replace("IV", "")
        elif "IX" in s:
            res += 9
            s = s.replace("IX", "")

        if "XL" in s:
            res += 40
            s = s.replace("XL", "")
        elif "XC" in s:
            res += 90
            s = s.replace("XC", "")

        if "CD" in s:
            res += 400
            s = s.replace("CD", "")
        elif "CM" in s:
            res += 900
            s = s.replace("CM", "")

        for char in s:
            if char in value_dict:
                res += value_dict[char]

        return res


if __name__ == "__main__":
    answer = Solution()
    print(answer.romanToInt("MCMXCIV"))
