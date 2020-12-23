class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        prev = nums[0]
        maxim = prev
        for i in range(1, len(nums)):
            prev = max(nums[i] + prev, nums[i])
            maxim = max(maxim, prev)
        return maxim
    

if  __name__ == "__main__":
    answer = Solution()
    print(answer.maxSubArray([-1, 0, -2]))