class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1

        l_arr = [height[0]]
        for i in range(1, len(height)):
            l_arr.append(max(l_arr[-1], height[i]))
        
        r_arr = [0] * len(height)
        r_arr[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            r_arr[i] = max(r_arr[i+1], height[i])
        
        max_water = 0

        for i in range(len(height)):
            max_water += min(l_arr[i], r_arr[i]) - height[i]

        return max_water

        
        