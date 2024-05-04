    def numRescueBoats(self, people: List[int], limit: int) -> int:
class Solution:
        people.sort() 
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            boats += 1
        boats = 0
            if l <= r and remain >= people[l]:
                l += 1
        return boats
        
[
