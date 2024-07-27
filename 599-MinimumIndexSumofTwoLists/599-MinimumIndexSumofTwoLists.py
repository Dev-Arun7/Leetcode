
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        result = []
        
        for i, restaurant1 in enumerate(list1):
            if restaurant1 in list2:
                j = list2.index(restaurant1)
                index_sum = i + j
                
                if index_sum < min_sum:
                    result = [restaurant1]
                    min_sum = index_sum
                elif index_sum == min_sum:
                    result.append(restaurant1)
        
        return result

["Shogun","Tapioca Express","Burger King","KFC"]
[
[
[
