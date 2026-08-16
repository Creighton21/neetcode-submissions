class KthLargest:
    def create_max_heap(self, nums):
        res = [0]
        if nums:
            nums.sort(reverse=True)
            for num in nums:
                res.append(num)
        return res

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = self.create_max_heap(nums)

    def pop(self, simulated_heap):
        if len(simulated_heap) == 1:
            return simulated_heap
        if len(simulated_heap) == 2:
            simulated_heap.pop()
            return simulated_heap

        res = simulated_heap[1]
        simulated_heap[1] = simulated_heap.pop()
        i = 1
        while 2 * i < len(simulated_heap):
            if (2 * i + 1 < len(simulated_heap) and 
            simulated_heap[2 * i + 1] > simulated_heap[2 * i] and 
            simulated_heap[i] < simulated_heap[2 * i + 1]):
                tmp = simulated_heap[i]
                simulated_heap[i] = simulated_heap[2 * i + 1]
                simulated_heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif simulated_heap[i] < simulated_heap[2 * i]:
                tmp = simulated_heap[i]
                simulated_heap[i] = simulated_heap[2 * i]
                simulated_heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return simulated_heap

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

        simulated_heap = self.heap.copy()
        for j in range(self.k - 1):
            simulated_heap = self.pop(simulated_heap)
            
        return simulated_heap[1]