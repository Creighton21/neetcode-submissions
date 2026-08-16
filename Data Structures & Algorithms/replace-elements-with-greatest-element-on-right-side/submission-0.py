class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1

        current_max = arr[i]
        arr[i] = -1
        i -= 1

        while i >= 0:
            current = arr[i]
            arr[i] = current_max
            if current > current_max:
                current_max = current

            i -=1


        return arr