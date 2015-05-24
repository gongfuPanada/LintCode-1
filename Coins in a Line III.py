"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no
more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n)
time?
"""
__author__ = 'Daniel'


class Solution:
    def firstWillWin_MLE(self, values):
        """
        DP formula:
        F_{i, j}^{1} = max(A_i + sum - F_{i+1, j}^{2},
                           A_j + sum - F_{i, j-1}^{2}
                           )

        Memory Limit Exceeded
        :param values: a list of integers
        :return: a boolean which equals to True if the first player will win
        """
        n = len(values)
        if n == 1:
            return True

        F = [[[0 for _ in xrange(n)] for _ in xrange(n)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n):
            for p in xrange(2):
                F[p][i][i] = values[i]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    F[p][i][j] = max(
                        values[i]+s[j+1]-s[i+1]-F[1^p][i+1][j],
                        values[j]+s[j]-s[i]-F[1^p][i][j-1]
                    )

        return F[0][0][n-1]>min(F[1][0][n-2], F[1][1][n-1])

    def firstWillWin(self, values):
        """
        optimize data structure

        :param values: a list of integers
        :return: a boolean which equals to True if the first player will win
        """
        n = len(values)
        if n == 1:
            return True
        SZ = 4
        F = [[[0 for _ in xrange(SZ)] for _ in xrange(SZ)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n):
            for p in xrange(2):
                F[p][i%SZ][i%SZ] = values[i]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    F[p][i%SZ][j%SZ] = max(
                        values[i]+s[j+1]-s[i+1]-F[1^p][(i+1)%SZ][j%SZ],
                        values[j]+s[j]-s[i]-F[1^p][i%SZ][(j-1)%SZ]
                    )

        return F[0][0][(n-1)%SZ] > min(F[1][0][(n-2)%SZ], F[1][1][(n-1)%SZ])


if __name__ == "__main__":
    print Solution().firstWillWin([3, 2, 2])
    print Solution().firstWillWin([1, 20, 4])