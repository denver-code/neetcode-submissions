class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for i in nums:
           freq[i] += 1
           if freq[i] > 1:
            return True
        
        return False