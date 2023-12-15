class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for i in paths:
            start.add(i[0])
            end.add(i[1])
        destination = end - start
        return destination.pop()
        
[
