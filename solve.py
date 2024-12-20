# nums = [1, 9, 4, 3, 6]

# min_v = nums[0]
# min_index = 0

# for i in range(1, len(nums)):
#     if nums[i] < min_v:
#         min_v = nums[i]
#         min_index = i
# print(min_v)

# k = 5

# Pascal = []
# for i in range(k):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = Pascal[i - 1][j - 1] + Pascal[i - 1][j]
#     Pascal.append(row)
# print(Pascal)

# Решение 22 задачи через поиск в глубину DFS
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         def backtrack(S='', left=0, right=0):
#             # Если достигнута длина строки 2 * n, добавить комбинацию в результат
#             if len(S) == 2 * n:
#                 result.append(S)
#                 return

#             # Добавлять открытую скобку, если осталось место
#             if left < n:
#                 backtrack(S + '(', left + 1, right)

#             # Добавлять закрытую скобку, если это сохраняет правильную структуру
#             if right < left:
#                 backtrack(S + ')', left, right + 1)

#         result = []
#         backtrack()
#         return result

# solution = Solution()
# n = 100
# print(solution.generateParenthesis(n))

# решение с помощью stack
# class Solution:
#     def generateParenthesis(self, n):
#         self.n = n
#         self.stack = []
#         self.res = []

#         self.backtrack(0, 0)
#         return self.res

#     def backtrack(self, opened, closed):
#         if opened == closed == self.n:
#             self.res.append("".join(self.stack))
#             return

#         if opened < self.n:
#             self.stack.append("(")
#             self.backtrack(opened + 1, closed)
#             self.stack.pop()

#         if closed < opened:
#             self.stack.append(")")
#             self.backtrack(opened, closed + 1)
#             self.stack.pop()


# sol = Solution()
# print(sol.generateParenthesis(2))

# решение 1863 суть задачи в определении XOR всех чисел. Надо 1 6
# определить ХОР 1, 6, 1 6.

# реилзиция через dfs

class Solution(object):
    def subsetXORSum(self, nums):
        def dfs(i, total):
            if i == len(nums):
                return total
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
        return dfs(0, 0)

sol = Solution()
nums = [1, 5, 6]
print(sol.subsetXORSum(nums))