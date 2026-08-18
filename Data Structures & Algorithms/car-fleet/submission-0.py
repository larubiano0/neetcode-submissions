class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleet = 0
        time_to_beat = None

        for current_position, current_speed in sorted(zip(position, speed), reverse = True):
            if not num_fleet:
                num_fleet += 1
                time_to_beat = (target-current_position)/current_speed
            else:
                current_time = (target-current_position)/current_speed
                if current_time > time_to_beat:
                    num_fleet += 1
                    time_to_beat = current_time
        return num_fleet