class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        if s == t:
            return True

        hash_s = {}

        for i in s:
            hash_s[i] = hash_s.get(i, 0) + 1
        
        for i in t: 
            if i not in hash_s:
                return False
            if hash_s[i] == 0:
                return False
            hash_s[i] -= 1
        
        return True