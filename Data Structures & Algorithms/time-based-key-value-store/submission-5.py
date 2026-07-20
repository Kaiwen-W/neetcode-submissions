class TimeMap:
    def __init__(self):
        # defaultdict with array of (value, timestamp)
        self.time_map = defaultdict(list) # key (person): list[(value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:
        # return largest timestamp_prev <= timestamp

        arr = self.time_map[key]
        
        l = 0
        r = len(arr) - 1

        if not arr: 
            return ""

        res = arr[0] # (timestamp, value)

        if res[0] > timestamp:
            return ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] > timestamp:
                r = mid - 1
            else:
                res = arr[mid]
                l = mid + 1
        
        return res[1]

