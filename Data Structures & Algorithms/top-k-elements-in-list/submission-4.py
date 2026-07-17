class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for n, c in hm.items():
            buckets[c].append(n)

        result = []
        for n in range(len(buckets)-1, 0, -1):
            for i in buckets[n]:
                result.append(i)
                if len(result) == k:
                    return result