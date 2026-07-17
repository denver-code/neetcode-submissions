class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for i in nums:
            hm[i] += 1
        return heapq.nlargest(k, hm.keys(), key=hm.get)
        hm = sorted(hm, key=hm.get, reverse=True)

        return hm[:k]