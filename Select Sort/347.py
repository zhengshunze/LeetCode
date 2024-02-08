class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        result = []
        for _ in range(k):
            max_freq = 0
            max_num = None
            for num, freq in freq_map.items():
                if freq > max_freq:
                   max_freq, max_num = freq,num
            if max_num is not None:
                result.append(max_num)
                del freq_map[max_num]
        
        return result
