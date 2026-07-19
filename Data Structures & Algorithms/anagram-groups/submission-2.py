class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in strs:
            hm["".join(sorted(i))].append(i)

        return list(hm.values())