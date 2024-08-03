class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_map = {}
        arr_map = {}
        for num in target:
            if num in target_map:
                target_map[num] += 1
            else:
                target_map[num] = 1
        for num in arr:
            if num in arr_map:
                arr_map[num] += 1
            else:
                arr_map[num] = 1
        for num in target_map:
            if target_map[num] != arr_map.get(num, 0):
                return False
        return True
        
[
[1,2,3,4]
[2,4,1,3]
[7]
[7]
[3,7,9]
[3,7,11]
true
true
false
true
true
false
