class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        lost = set()
        multi_lost = set()
        for player in matches:
            win.add(player[0])
            if player[1] in lost:
                lost.add(player[1])
                multi_lost.add(player[1])
            else:
        all_win = win - lost
        one_lost = lost - multi_lost
        return [sorted(list(all_win)), sorted(list(one_lost))]

[
[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
[[2,3],[1,3],[5,4],[6,4]]
[[1,2,10],[4,5,7,8]]
[[1,2,5,6],[]]
[[1,2,10],[4,5,7,8]]
[[1,2,5,6],[]]
