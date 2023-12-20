class·Solution:
····def·singleNumber(self,·nums:·List[int])·->·List[int]:
········result·=·[]
········result·=·[x·for·x·in·nums·if·nums.count(x)·==·1]
········return·result
        
[
