class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return nums
        elif len(nums) == 1:
            return [] if val in nums else nums
        
        i = 0
        while i < len(nums):
            if nums[i] != val:
                break
            i += 1
                
        j = i + 1
        while j < len(nums):
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums[i:j]

if __name__ == "__main__":
    answer = Solution()
    print(answer.removeElement([3,2,2,3], 3))