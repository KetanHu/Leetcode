class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = 0
        for i in accounts:
            sum_j = 0
            for j in i:
                sum_j += j
            if sum_j > wealth:
                wealth = sum_j
        return wealth
            