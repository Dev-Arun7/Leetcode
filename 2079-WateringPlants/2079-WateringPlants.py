
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        bucket = capacity
        
        for i in range(len(plants)):
            # If there's enough water in the bucket to water the current plant
            if bucket >= plants[i]:
                step += 1  # Step to the next plant
                bucket -= plants[i]  # Water the plant
            else:
                # Go back to the start to refill, and return to the current plant
                step += (i * 2) + 1  # Go back to the start and return to the current plant
                bucket = capacity - plants[i]  # Refill the bucket and water the plant
        
        return step
[
[2,2,3,3]
5
[1,1,1,4,2,3]
4
[7,7,7,7,7,7,7]
8
14
30
49
14
30
49
