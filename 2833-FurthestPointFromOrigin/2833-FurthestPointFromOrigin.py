class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq = {}
        freq['L'] = moves.count('L')
        freq['R'] = moves.count('R')
        freq['_'] = moves.count('_')
        if freq['L'] >= freq['R']:
            return freq['L'] - freq['R'] + freq['_']
        else:
            return freq['R'] - freq['L'] + freq['_']
        
"
