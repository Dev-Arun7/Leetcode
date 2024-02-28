class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        for i in range(start, destination):
            clockwise += distance[i]
        clockwise = 0

        anticlockwise = total - clockwise

        return clockwise if clockwise < anticlockwise else anticlockwise
        if start > destination:
            start, destination = destination, start
            
        
[
