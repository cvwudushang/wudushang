class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        new=[]
        new.append(newInterval[0])
        new.append(newInterval[1])
        bool=False
        for it in intervals:
            if it[1]<newInterval[0]:
                answer.append(it)
            elif it[0]>newInterval[1]:
                if not bool:
                    answer.append(new)
                answer.append(it)
            else:
                new[0]=min(new[0],it[0])
                new[1]=max(new[1],it[1])
        if not bool:
            answer.append(new)
        return answer

    def rewo(self, a, b):
        c = []
        c.append(a)
        c.append(b)
        return c