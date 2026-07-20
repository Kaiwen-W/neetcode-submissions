class TimeMap:
    def __init__(self):
        self.time_map = {} # key (person): (emotion, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key] = (value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        return self.time_map[key][0]
