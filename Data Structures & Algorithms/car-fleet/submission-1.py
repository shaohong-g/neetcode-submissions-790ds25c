class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position, speed), reverse=True)

        result = 1
        prev_spd = (target - fleet[0][0]) / fleet[0][1]
        for i in range(1, len(fleet)):
            curr_spd = (target - fleet[i][0]) / fleet[i][1]

            if curr_spd > prev_spd:
                result += 1
                prev_spd = curr_spd
        return result
