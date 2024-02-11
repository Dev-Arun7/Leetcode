class Solution:
····def·rowAndMaximumOnes(self,·mat:·List[List[int]])·->·List[int]:
········index·=·0
········count·=·0
········for·i,·row·in·enumerate(mat):
············temp·=·row.count(1)
············if·temp·>·count:
················count·=·temp
················index·=·i
········return·[index,·count]
        
[
