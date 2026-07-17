class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        elif len(nums) == 1:
            return False
        elif nums[0] == nums[1]:
            return True
        
        freq_map = []

        for i in nums:
            if i not in freq_map:
                freq_map.append(i)
            else:
                return True
        
        return False