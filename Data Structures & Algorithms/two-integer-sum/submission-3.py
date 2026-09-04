class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}
        output = []
    
        index = 0
        for i in nums:
            if i in total.keys():
                return[total[i], index]
            else:
                total[target - i] = nums.index(i)
                index += 1


            
        

        

            