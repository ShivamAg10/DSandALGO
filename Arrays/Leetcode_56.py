'''
    Merge Intervals

    Given an array of intervals where intervals[i] = [starti, endi], merge all 
    overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.

    Example 1:
        Input: 
            intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: 
            [[1,6],[8,10],[15,18]]
        Explanation: 
            Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    Example 2:
        Input: 
            intervals = [[1,4],[4,5]]
        Output: 
            [[1,5]]
        Explanation: 
            Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge(intervals):
    intervals.sort()
    answer = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] < start:
            start = intervals[i][0]
        if intervals[i][0] <= end:
            if end < intervals[i][1]:
                end = intervals[i][1]
        elif intervals[i][0] > start and intervals[i][0] > end:
            answer.append([start,end])
            start = intervals[i][0]
            end = intervals[i][1]
    answer.append([start,end])
        
    return answer

arr2D = [[1,4],[0,0]]

print(merge(arr2D))

