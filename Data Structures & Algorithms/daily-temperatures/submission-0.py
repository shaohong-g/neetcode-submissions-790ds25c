class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack:
                prev = stack.pop()
                if temperatures[i] > temperatures[prev]:
                    output[prev] = i - prev
                else:
                    stack.append(prev)
                    break
            stack.append(i)
        return output