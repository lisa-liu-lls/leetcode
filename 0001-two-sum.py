class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity: O(n)

        comps = {}
        for i, x in enumerate(nums):
            comp = target - x
            if comp in comps:
                return [comps[comp], i]
            else:
                comps[x] = i
