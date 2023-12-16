class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        result = []
        result_dict = dict(zip(heights, names))
        sorted_dict = dict(sorted(result_dict.items(), reverse=True))
        print(result_dict)
        for i in sorted_dict.values():
            result.append(i)
        return result

[
