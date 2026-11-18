class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}

        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        
        arr = []
        for num, count in d1.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res



        
        
        

        return 

        