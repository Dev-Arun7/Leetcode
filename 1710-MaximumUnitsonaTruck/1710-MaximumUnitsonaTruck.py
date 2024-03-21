class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        total = 0
        boxes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
        for i, box in enumerate(boxes):
            if count + box[0] <= truckSize:
                count += box[0]
                total += box[0] * box[1]
            else:
                total += (truckSize - count) * box[1]
                break
        return total
        
[
