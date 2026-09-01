class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        mx = arr[len(arr)-1]
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                arr[len(arr)-1] = -1
            else:
                tmp = arr[i]
                arr[i] = mx
                mx = max(tmp, mx)

        return arr
