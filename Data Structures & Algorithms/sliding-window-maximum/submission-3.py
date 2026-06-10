import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap_out = []
        heap_in = []
        result = []

        for i in range(k-1):
            heapq.heappush(heap_in, -1 * nums[i])

        for i in range(k-1, len(nums)):
            heapq.heappush(heap_in, -1 * nums[i])
            curr_max = heap_in[0]

            while len(heap_out) != 0:
                last_exception = heap_out[0]
                if last_exception == curr_max:
                    heapq.heappop(heap_in)
                    heapq.heappop(heap_out)
                    curr_max = heap_in[0]
                else:
                    break
            
            heapq.heappush(heap_out, -1 * nums[i - k + 1])
            result.append(-1 * curr_max)
        return result