class Solution:

    def get_freq_map(self, s: str) -> dict:
        freq_map = {}

        for i in s:
            if i not in freq_map.keys():
                freq_map[i] = 1
            else:
                freq_map[i] += 1
        
        return freq_map

    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        if s == t:
            return True

        s_f = self.get_freq_map(s)
        
        for i in t:
            if i not in s_f:
                return False
            if s_f[i] == 0:
                return False
            s_f[i] -= 1

        return True
