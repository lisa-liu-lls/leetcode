class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1] = [output[-1][0], max(intervals[i][1], output[-1][1])]
            else:
                output.append(intervals[i])            
        return output
