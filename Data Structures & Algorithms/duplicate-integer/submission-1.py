class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(0, len(nums)):
            temp = nums[i]
            if temp in seen:
                return True
            seen.add(temp)
        return False