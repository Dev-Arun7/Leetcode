class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []
        for row in image:
            temp = []
            for num in reversed(row):
                temp.append(1) if num == 0 else temp.append(0)
            flipped.append(temp)
        return flipped
        
[
