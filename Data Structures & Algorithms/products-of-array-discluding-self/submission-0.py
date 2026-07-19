class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i1, n in enumerate(nums):
            target = 1
            for i2, j in enumerate(nums):
                if i2 == i1:
                    continue
                target *= j
            result.append(target)
        return result