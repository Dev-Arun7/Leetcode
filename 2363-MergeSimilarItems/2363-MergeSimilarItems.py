class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = {}
        new.extend(items1)
        new.extend(items2)
        for item in new:
        new = []
            if item[0] not in ret:

            else:
                ret[item[0]] += item[1]
        result = [[key, value] for key, value in sorted_ret.items()]
        return result
                ret[item[0]] = item[1]
        sorted_ret = dict(sorted(ret.items()))

[
