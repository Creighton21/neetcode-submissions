class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        while True:

            if len(max_heap) <= 1:
                break
            x = heapq.heappop(max_heap) * -1
            y = heapq.heappop(max_heap) * -1

            if x == y:
                continue
            elif x < y:
                heapq.heappush(max_heap, -1 * (y-x))
            else:
                heapq.heappush(max_heap, -1 * (x-y))

        if max_heap:
            return max_heap[0] * -1
        return 0