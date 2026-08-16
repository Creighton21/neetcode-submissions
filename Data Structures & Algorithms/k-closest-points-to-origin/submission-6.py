class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_to_origin = {}
        for i, point in enumerate(points):
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            distance_to_origin[i] = distance
        print(distance_to_origin)
        k_smallest_idx = []
        k_smallest_vals = []
        for key, val in distance_to_origin.items():
            if len(k_smallest_idx) < k:
                k_smallest_idx.append(key)
                k_smallest_vals.append(val)

            elif val < max(k_smallest_vals):
                index = k_smallest_vals.index(max(k_smallest_vals))
                print(key)
                print(index)
                k_smallest_idx[index] = key
                k_smallest_vals[index] = val
            
        return [points[i] for i in k_smallest_idx]