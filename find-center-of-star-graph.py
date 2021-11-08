class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num = len(edges)
        n = 1000000
        N = 0
        degree = [0] * (n + 1)
        for i in range(num):
            a, b = edges[i]
            degree[a - 1] += 1
            degree[b - 1] += 1
            if a > N:
                N = a
            if b > N:
                N = b
        for i in range(n + 1):
            if degree[i] == N - 1:
                return i + 1
        