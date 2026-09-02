from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = dict(Counter(nums).most_common(k))
        return list(top_k.keys())
