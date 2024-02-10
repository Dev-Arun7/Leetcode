class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6 , 'g':7, 'h':8}
        if dict[coordinates[0]] % 2 == int(coordinates[1]) % 2:
            return False
        else:
            return True 
        
"
