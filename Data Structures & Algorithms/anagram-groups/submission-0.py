from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in strs:
            word_sort = tuple(sorted(i))
            output[word_sort].append(i)
        return list(output.values())





        