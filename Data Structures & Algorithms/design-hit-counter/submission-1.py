class HitCounter:

    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] = self.hits.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        start = timestamp - 299 if timestamp >= 300 else 0
        total = 0
        for n in range(start, timestamp + 1):
            total += self.hits.get(n, 0)

        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
