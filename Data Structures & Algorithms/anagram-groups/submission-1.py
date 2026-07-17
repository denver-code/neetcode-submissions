class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in strs:
            si = "".join(sorted(i))
            hm[si].append(i)
        
        return list(hm.values())