class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for i in nums:
            hm[i] += 1
        
        hm = sorted(hm, key=hm.get, reverse=True)

        return hm[:k]