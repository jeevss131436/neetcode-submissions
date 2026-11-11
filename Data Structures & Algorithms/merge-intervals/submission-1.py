class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]

        for current_start, current_end in intervals[1:]:
            previous_end = merged[-1][1]
            if current_start <= previous_end:
                merged[-1][1] = max(previous_end, current_end)
            else:
                merged.append([current_start, current_end])
        return merged