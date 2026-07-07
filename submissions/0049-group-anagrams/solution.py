class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort by "".join(sorted(word)) to get the alphabetical order of each one
        # then need to find out which elements are the same
        anagrams = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        return list(anagrams.values())
