class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm: dict = defaultdict(int)

        for n in nums:
            hm[n] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        print(buckets)

        for n, o in hm.items():
            print(n, o)
            buckets[o].append(n)
        
        result = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result