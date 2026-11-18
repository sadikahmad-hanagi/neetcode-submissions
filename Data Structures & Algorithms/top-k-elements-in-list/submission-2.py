class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        freq = [ [] for i in range(len(nums) + 1)]

        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        

        for num, count in d1.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        




        
        
        



        