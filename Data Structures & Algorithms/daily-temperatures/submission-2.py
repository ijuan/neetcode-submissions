class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                s_temp, s_index = stack.pop()
                res[s_index] = (i - s_index)
            stack.append([t, i])
        return res

        

