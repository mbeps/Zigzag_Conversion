class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of empty strings for each row
        zigzag: list[str] = ['' for _ in range(numRows)]
        row, step = 0, 1

        # Iterate over the string
        for char in s:
            # Add the current character to the current row
            zigzag[row] += char
            
            # If we've reached the top or bottom of the zigzag, change direction
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
                
            # Move to the next row
            row += step

        # Join all rows to get the result
        return ''.join(zigzag)
