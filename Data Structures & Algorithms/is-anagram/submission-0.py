class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # keep track of frequency of each char (char:freq) by having two hash tables
        dict_s = {}
        dict_t = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        # compare the freq of each char in s and t
        if dict_s == dict_t:
            return True
        return False
