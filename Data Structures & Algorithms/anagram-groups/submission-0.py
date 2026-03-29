class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict where each key is the sorted string
        # and value being a list of strings belonging to that group
        dict_sorted = {}

        # iterate through each string in the input list
        for word in strs:
            # sort the char in the word to form a key
            sorted_word = ''.join(sorted(word))
            # append the original word to the list correspoding to this key
            if sorted_word not in dict_sorted:
                dict_sorted[sorted_word] = [word]
            else:
                dict_sorted[sorted_word].append(word)
        
        # return all the VALUES of the dict
        return list(dict_sorted.values())
        