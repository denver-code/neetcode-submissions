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
        t_f = self.get_freq_map(t)

        if s_f.keys() != t_f.keys():
            return False
        
        for k in s_f.keys():
            if s_f[k] != t_f[k]:
                return False

        return True
