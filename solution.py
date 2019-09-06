from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i = 0
        j = len(intervals) - 1

        while i < j and not self.overlap(intervals[i], newInterval):
            i += 1

        while i <= j and not self.overlap(intervals[j], newInterval):
            j -= 1

        if (self.overlap(intervals[i], newInterval)):
            newInterval = self.merge(self.merge(
                intervals[i], newInterval), intervals[j])
            return intervals[:i] + [newInterval] + intervals[j + 1:]

        i = 0

        while i <= len(intervals) - 1 and intervals[i][0] < newInterval[0]:
            i += 1

        return intervals[:i] + [newInterval] + intervals[i:]

    def overlap(self, a: List[int], b: List[int]) -> bool:
        return a[0] <= b[1] and b[0] <= a[1]

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]
