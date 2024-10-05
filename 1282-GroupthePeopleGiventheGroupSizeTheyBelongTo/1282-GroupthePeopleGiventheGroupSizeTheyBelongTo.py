    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        map = {}
        for num, size in enumerate(groupSizes):
            if size in map:
                if len(map[size][-1]) < size:
                    map[size][-1].append(num)
                else:
                    map[size].append([num]) 
            else:
                map[size] = [[num]]
        output = []
        for key, value in map.items():
            output.extend(value)
        return output
class Solution:
[
[3,3,3,3,3,1,3]
[2,1,3,3,3,2]
[[0,1,2],[3,4,6],[5]]
[[0,5],[1],[2,3,4]]
[[5],[0,1,2],[3,4,6]]
[[1],[0,5],[2,3,4]]
