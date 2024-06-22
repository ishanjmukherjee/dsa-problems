# My implementation after watching verbal explanation up to 9:17 in solution video
# https://www.youtube.com/watch?v=Pr6T-3yB9RM
# O(n) time complexity, where
# n : length of position

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetStack = []
        # create list of position-speed tuples
        pos_sp = [(position[i], speed[i]) for i in range(len(position))]
        # sort list by position
        pos_sp.sort(key=lambda p_sp: p_sp[0], reverse=True)
        for p_sp in pos_sp:
            # time = (target - position) / speed
            time = (target - p_sp[0]) / p_sp[1]
            # fleetStack is empty -> furthest car (automatically a fleet)
            if not fleetStack or time > fleetStack[-1]:
                fleetStack.append(time)
        return len(fleetStack)

# Reimplementing the official solution after looking at the code
# O(n) time complexity, where
# n : length of position

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse=True) # automatically sorts by first index of tuple
        print(ps)
        fleetStack = []
        for p, s in ps:
            time = (target - p) / s
            if not fleetStack or time > fleetStack[-1]:
                fleetStack.append(time)
        return len(fleetStack)
