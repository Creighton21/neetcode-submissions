class Solution:
    def simulateEatingRate(self, p, h, rate):
        if rate == 0: return False
        total_hours = 0
        for pile in p:
            total_hours += math.ceil(pile / rate)
        return total_hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r
        while l <= r:
            m = (l + r) // 2
            if self.simulateEatingRate(piles, h, m):
                min_rate = m
                r = m - 1
            else:
                l = m + 1
        return min_rate