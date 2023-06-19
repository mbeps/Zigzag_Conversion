class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        res: list[str] = []
        n: int = len(s)
        
        cycleLen: int = 2 * numRows - 2  # Number of elements in one cycle
        
        for i in range(numRows):
            for j in range(i, n, cycleLen):
                res.append(s[j])
                if i != 0 and i != numRows - 1 and j + cycleLen - 2*i < n:
                    res.append(s[j + cycleLen - 2*i])
        return "".join(res)
