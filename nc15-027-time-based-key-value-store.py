# My solution after looking at __init__ and set() of official text solution (I hadn't
# noticed that timestamps are inserted in strictly increasing order)
# O(1) insertion and O(log n) lookup time complexity, where
# n : number of timestamps stored under a single key

class TimeMap:

    def __init__(self):
        # dictionary to store timestap-value tuples
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.dic[key]
        l, r = 0, len(values) - 1
        maxIdx = float('-inf')
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] <= timestamp:
                maxIdx = mid
                l = mid + 1
            else:
                r = mid - 1
        return values[maxIdx][1] if maxIdx > float('-inf') else ""

# Reimplenenting official solution
# Same as my solution, but uses slightly less memory (though same space complexity)
# (Though I win some points because I use a defaultdict, whereas the official 
# solution has to use a conditional in set() and the get method on a Python dict
# with a default [] value. I also get some points for sensibly making the timestamp
# the first element of the tuple; it makes sense for the sorted thing to come first.)

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.dic[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] <= timestamp:
                ans = values[mid][1] # directly storing the string
                l = mid + 1
            else:
                r = mid - 1
        return ans
