class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        output = r
        while l <= r:
            mid = (l+r) // 2

            o_h = sum([math.ceil(x / mid) for x in piles])

            if o_h > h:
                l = mid + 1
            else:
                output = mid
                r = mid - 1
        return output
